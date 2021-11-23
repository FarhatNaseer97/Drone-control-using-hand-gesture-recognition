# first of all import the socket library
import socket
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import time
from tensorflow.keras.models import load_model	

# next create a socket object
s = socket.socket()		
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345		

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
host = socket.gethostname() 
s.bind((host, port))		
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)	
print ("socket is listening")

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

# Initialize the webcam
cap = cv2.VideoCapture(0)
#Capturing frames from webcam
f = cap.get(cv2.CAP_PROP_FPS)
# Establish connection with client.
print("Waiting to connect to other script")
comm, addr = s.accept()	
print ('Got connection from', addr )
# a forever loop until we interrupt it or
# an error occurs
START_TIME = time.time()
FPS = 0
FRAME_COUNTER = 0
while True:

    # Read each frame from the webcam
    FRAME_COUNTER += 1
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Get hand landmark prediction
    result = hands.process(framergb)

    # print(result)
    
    className = ''
     # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            # print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]# get the state information
    
    print(className)
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow("Output", frame) 
    SECONDS = time.time() - START_TIME
    # calculating the frame rate
    FPS = FRAME_COUNTER/SECONDS
    #print(FPS)
    print('Time delay from server is %d' %SECONDS)
    

    # send a thank you message to the client. encoding to send byte type.
    comm.send(str(className).encode())
    if cv2.waitKey(1) == ord('q'):
        # Close the connection with the client
        c.close()
        # Breaking once connection closed
        break
