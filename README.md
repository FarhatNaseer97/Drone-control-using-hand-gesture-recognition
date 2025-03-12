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

**Runnig the code**<br/>
Clone the repository
1. Open the terminal using ctrl+Alt+Tab<br/>
2. cd Drone-control-using-hand-gesture-recognition
3. pip install -r requirements
2. Run the Server.py file by typing the below command in terminal<br/>
```
python3 server.py
```
3. open another tab in the terminal and run the clinet.py in terminal by typing the given command.<br/>
 ```
 python3 client.py
 ```
 
