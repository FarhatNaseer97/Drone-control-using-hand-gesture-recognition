# Import socket module
import socket
from threading import Thread
import multiprocessing
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
from pyparrot.Minidrone import Mambo
import time

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 12345	
# connect to the server on local computer
host = socket.gethostname() 
s.connect((host, port))

mamboAddr = "E0:14:5F:6C:3D:FE"
mambo = Mambo(mamboAddr, use_wifi=False)
print("trying to connect")
success = mambo.connect(num_retries=5)
print("connected: %s" % success)
x=0

while True:

    # receive data from the server and decoding to get the string.
    className = str(s.recv(1024).decode())
    x += 1
    #print(x)
    if className:
        print("data coming")
    else:
        print("no data")
    print("Class Name:" + className[-1])
    # Because of delay, a lot of data is sent, so i am using the last alphabet
    # it can also be dont other ways, think of a better solution
    #START_TIME = time.time()
    
    if (className[-1] == "f"):
        print("Take off")
        START_TIME =0
        #mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        #mambo.smart_sleep(2)
        START_TIME = time.time()
        mambo.safe_takeoff(1)
        #time.sleep(1)
        #print("flying state is %s" % mambo.sensors.flying_state)
        #print("Flying direct: going up")
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
        print("mambo takeoff")
        SECONDS = time.time() - START_TIME
        print('The delay from clent in Takeoff is SECONDS %f' % SECONDS)
        #print(SECONDS)
    elif (className[-1] == "p"):
        #print("mambo Landing")
        START_TIME = time.time()
        print("landing")
        #print("flying state is %s" % mambo.sensors.flying_state)
        mambo.safe_land(1)
        #mambo.smart_sleep(5)
        SECONDS = time.time() - START_TIME
        print('The delay from client in  landing is SECONDS %f' %SECONDS)
        
    #time.sleep(9) # remove this delay when you add mambo code
    
    
    


# close the connection
s.close()
