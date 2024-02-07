package main

import (
	"fmt"
	"net"
	"os"
	"strings"
)

func main() {
	arguments := os.Args
	if len(arguments) == 1 {
		fmt.Println("Please provide a port number!")
		return
	}

	PORT := ":" + arguments[1]
	addr, err := net.ResolveUDPAddr("udp", PORT)
	if err != nil {
		fmt.Println("Error resolving address:", err)
		return
	}

	conn, err := net.ListenUDP("udp", addr)
	if err != nil {
		fmt.Println("Error listening:", err)
		return
	}
	defer conn.Close()

	fmt.Println("Server listening on", addr)

	var sender, receiver *net.UDPAddr

	for {
		buffer := make([]byte, 1024)
		n, addr, err := conn.ReadFromUDP(buffer)
		if err != nil {
			fmt.Println("Error reading from client:", err)
			continue
		}

		clientAddr := addr.String()
		message := string(buffer[:n])

		if strings.ToLower(message) == "sender" {
			fmt.Println("Sender client connected:", clientAddr)
			sender = addr
		} else if strings.ToLower(message) == "receiver" {
			fmt.Println("Receiver client connected:", clientAddr)
			receiver = addr
		}

		// Forward messages from sender to receiver
		if sender != nil && receiver != nil && addr.String() == sender.String() {
			_, err := conn.WriteToUDP(buffer[:n], receiver)
			if err != nil {
				fmt.Println("Error forwarding data to receiver:", err)
			}
			fmt.Printf("Forwarded message from sender %s to receiver %s\n", clientAddr, receiver.String())
		}

		if sender != nil && receiver != nil && addr.String() == receiver.String() {
			_, err := conn.WriteToUDP(buffer[:n], sender)
			if err != nil {
				fmt.Println("Error forwarding data to sender:", err)
			}
			fmt.Printf("Forwarded message from receiver %s to sender %s\n", clientAddr, sender.String())
		}
	}
}
