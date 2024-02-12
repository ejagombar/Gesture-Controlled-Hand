package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"os"

	"github.com/tarm/serial"
)

type FingerData struct {
	ThumbAngle    uint8
	Thumb         uint8
	Index         uint8
	Middle        uint8
	Ring          uint8
	Pinky         uint8
	LedColour     [3]uint8
	LedBrightness uint8
	ServoData     uint8
	checkSum      uint16
}

func main() {
	arguments := os.Args
	if len(arguments) < 2 {
		fmt.Println("Please provide host:port SerialPort.")
		return
	}

	CONNECT := arguments[1]
	serverAddr, err := net.ResolveUDPAddr("udp", CONNECT)
	if err != nil {
		fmt.Println("Error resolving server address:", err)
		return
	}

	conn, err := net.DialUDP("udp", nil, serverAddr)
	if err != nil {
		fmt.Println("Error connecting to server:", err)
		return
	}
	defer conn.Close()

	// Identify as a sender
	_, err = conn.Write([]byte("client1"))
	if err != nil {
		fmt.Println("Error identifying as a sender:", err)
		return
	}

	go listen(conn, arguments[2])

	for {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print(">> ")
		text, _ := reader.ReadString('\n')
		data := []byte(text + "\n")

		_, err = conn.Write(data)

		if err != nil {
			fmt.Println(err)
			return
		}
	}
}

func unpackData(buffer []byte) (*FingerData, error) {
	var receivedData FingerData

	if len(buffer) < 13 {
		return nil, fmt.Errorf("Buffer too short")
	}

	receivedData.ThumbAngle = buffer[0]
	receivedData.Thumb = buffer[1]
	receivedData.Index = buffer[2]
	receivedData.Middle = buffer[3]
	receivedData.Ring = buffer[4]
	receivedData.Pinky = buffer[5]
	receivedData.LedColour[0] = buffer[6]
	receivedData.LedColour[1] = buffer[7]
	receivedData.LedColour[2] = buffer[8]
	receivedData.LedBrightness = buffer[9]
	receivedData.ServoData = buffer[10]
	receivedData.checkSum = uint16(buffer[11])<<8 | uint16(buffer[12])

	return &receivedData, nil
}

func checkSumMatch(fingerData FingerData) bool {
	sum := int(fingerData.ThumbAngle) + int(fingerData.Thumb) + int(fingerData.Index) + int(fingerData.Middle) + int(fingerData.Ring) + int(fingerData.Pinky)
	return sum == int(fingerData.checkSum)
}

func listen(conn *net.UDPConn, port string) {
	c := &serial.Config{Name: port, Baud: 115200}
	s, err := serial.OpenPort(c)
	if err != nil {
		log.Fatal(err)
	}

	for {
		buffer := make([]byte, 1024)
		n, _, err := conn.ReadFromUDP(buffer)
		if err != nil {
			fmt.Println("Error reading from server:", err)
			return

		}
		received, err := unpackData(buffer[:n])
		if err != nil {
			fmt.Println("Error unpacking data:", err)
		}

		if received != nil {

			if !checkSumMatch(*received) {
				print("---CHECKSUM MISMATCH---\n")
			}

			print("Thumb Angle: ", received.ThumbAngle, "\n")
			print("Thumb: ", received.Thumb, "\n")
			print("Index: ", received.Index, "\n")
			print("Middle: ", received.Middle, "\n")
			print("Ring: ", received.Ring, "\n")
			print("Pinky: ", received.Pinky, "\n")
			print("Led Colour: ", received.LedColour[0], received.LedColour[1], received.LedColour[2], "\n")
			print("Led Brightness: ", received.LedBrightness, "\n")
			print("Servo Data: ", received.ServoData, "\n")

			data := []byte{received.ThumbAngle, received.Thumb, received.Index, received.Middle, received.Ring, received.Pinky, received.LedColour[0], received.LedColour[1], received.LedColour[2], received.LedBrightness, received.ServoData}

			_, err = s.Write(data)
			if err != nil {
				log.Fatal(err)
			}

		}
	}
}
