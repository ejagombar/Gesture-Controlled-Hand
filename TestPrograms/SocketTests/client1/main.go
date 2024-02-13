package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	arguments := os.Args
	if len(arguments) == 1 {
		fmt.Println("Please provide host:port.")
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
	_, err = conn.Write([]byte("sender"))
	if err != nil {
		fmt.Println("Error identifying as a sender:", err)
		return
	}

	// go listen(conn)

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

func listen(conn *net.UDPConn) {
	for {
		buffer := make([]byte, 1024)
		n, _, err := conn.ReadFromUDP(buffer)
		if err != nil {
			fmt.Println("Error reading from server:", err)
			return
		}
		received := string(buffer[:n])
		fmt.Println("Received:", received)
	}
}
