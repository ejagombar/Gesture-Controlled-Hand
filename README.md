# Gesture-Control-Hand
This project is part for my Masters, where I am building a low-cost, all-in-one robitic hand, capable of being controlled via gesture controll over the internet in real time. Scroll down for demo.

## Project Technical Overview
![ProjectDiagram](https://github.com/ejagombar/Gesture-Controlled-Hand/assets/77460324/3519acfa-fe36-4d3a-9b0f-c322262c6780)
1)	Microcontroller embedded in the robotic hand. This will control the servo motors used to actuate the 5 fingers on the hand. It will also be able to handle any other peripherals that could be added in the future.
2)	A single board computer (SBC) such as a Raspberry Pi. It will receive a stream of movement and positional data over the network from the client that will be relayed to the robotic hand and robotic arm. Data will be sent from the SBC to the microcontroller in the robotic hand over either USB or I2C.
3)	The scope of this project does not extend to building a full robotic arm. However, the project will be designed so that an arm could be connected to the SBC and sent the stream of positional data received by the SBC. Attaching the robotic hand to an arm would allow for more degrees of movement and flexibility.
4)	A camera module will be connected to the SBC. This will stream live video footage back to the client application, allowing the user to see the actions of the robot remotely and in real time.
5)	Initially, IP addresses will be used so that the client is able connect to the SBC. A stretch goal of this project is to allow access to the robot from anywhere with an internet connection and to facilitate this, a server is needed to manage the connection. This server could be hosted using a cloud provider such as Azure and AWS or hosted locally.
6)	Client desktop application. This will run on the user’s PC and will handle the computer vision aspect of project. The user will require a PC or laptop with a webcam to capture the gestures. This movement data will be sent to the SBC over the network. At the same time, the video stream from the SBC will be displayed in the desktop application to allow the user to see the real-time movements of the robotic hand.

# Early Demonstration





https://github.com/ejagombar/Gesture-Controlled-Hand/assets/77460324/56474491-1496-44e8-9ca9-bb5c1d3c240b

If the video doesnt work, it can be viewed [here.](https://www.youtube.com/watch?v=kY19f_uoSKw)

The communication now works over UDP.


# Hand Construction
![PXL_20240130_221141786](https://github.com/ejagombar/Gesture-Controlled-Hand/assets/77460324/cbd5fb9b-b147-44c1-809e-e02e45d25195)
![PXL_20240130_221131466 MP](https://github.com/ejagombar/Gesture-Controlled-Hand/assets/77460324/a2186e96-cf62-461c-b006-eb32f00b4746)

## Repo Overview
- The CAD and .obj files for the robotic hand can be found in the "3D Models" folder.
- The desktop application can be found under QT/Application
- The code running on the microcontroller can be found under ESP32.
