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

	var client1, client2 *net.UDPAddr

	for {
		buffer := make([]byte, 1024)
		n, addr, err := conn.ReadFromUDP(buffer)
		if err != nil {
			fmt.Println("Error reading from client:", err)
			continue
		}

		clientAddr := addr.String()
		message := string(buffer[:n])

		if strings.ToLower(message) == "client1" {
			fmt.Println("Client1 connected:", clientAddr)
			client1 = addr
		} else if strings.ToLower(message) == "client2" {
			fmt.Println("Client2 connected:", clientAddr)
			client2 = addr
		}

		if client1 != nil && client2 != nil && addr.String() == client1.String() {
			_, err := conn.WriteToUDP(buffer[:n], client2)
			if err != nil {
				fmt.Println("Error forwarding data to client2:", err)
			}
			fmt.Printf("Forwarded message from client1 %s to client2 %s\n", clientAddr, client2.String())
		}

		if client1 != nil && client2 != nil && addr.String() == client2.String() {
			_, err := conn.WriteToUDP(buffer[:n], client1)
			if err != nil {
				fmt.Println("Error forwarding data to client1:", err)
			}
			fmt.Printf("Forwarded message from client2 %s to client1 %s\n", clientAddr, client1.String())
		}
	}
}
