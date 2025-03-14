# Drone-control-using-hand-gesture-recognition

**Overview:**<br/>
This project implements a real-time hand gesture recognition system to control a drone using computer vision and web sockets. By leveraging OpenCV and MediaPipe, the system detects and tracks hand gestures, which are then translated into drone commands. Web sockets are used to ensure smooth movement and reduce lag between data frames, providing a seamless control experience.

**Features:**<br/>
- Hand Gesture Recognition: Uses OpenCV and MediaPipe to detect and interpret hand gestures.
- Smooth Movement: Optimized for minimal latency in transmitting control commands.
- WebSocket Communication: Ensures low-latency, real-time drone control.
- Flexible & Extendable: Can be adapted for various types of drones and expanded with additional gestures.

**Hardware setup:**<br/>
Turn on bluetooth of your Laptop and  turn on your mambo-drone.

**Software setup**<br/>
Clone the repository
1. Open the terminal using ctrl+Alt+Tab<br/>
2. Clone the repository
   ```
   git clone https://github.com/FarhatNaseer97/Drone-control-using-hand-gesture-recognition.git
   ```
4. cd Drone-control-using-hand-gesture-recognition
5. pip install -r requirements
6. Run the Server.py file by typing the below command in terminal<br/>
```
python3 server.py
```
6. open another tab in the terminal and run the clinet.py in terminal by typing the given command.<br/>
 ```
 python3 client.py
 ```
**Research paper**<br/>
This project is based on research published in IEEE:
<a href="https://ieeexplore.ieee.org/document/9828347" target="_blank">Deep Learning-Based Unmanned Aerial Vehicle Control with Hand Gesture and Computer Vision</a> 

**Contributing**<br/>
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.
