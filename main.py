import sys
import cv2
import numpy as np
import time
from matplotlib import pyplot as plt
loca = ''

def on_message(client, userdata, message):
    ##print("received message: ", str(message.payload.decode("utf-8")))
    loca = str(message.payload.decode("utf-8"))
    ##print("Topic"+ str(message.topic))
cross = cv2.imread('pngwing.com.png')
size = 100
final = cv2.resize(cross,(size,size))
img2gray = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
cap = cv2.VideoCapture(0)

mqttBroker = "test.mosquitto.org"
port = 1883
client = mqtt.Client("esp32_pthon")
if client.connect(mqttBroker, port) != 0:
    print("Not connected")
    sys.exit(-1)
else:
    print("connected")

while cap.isOpened():
    client.loop_start()
    client.subscribe("test/spedo")
    client.on_message = on_message
    print(loca)
    client.loop_stop()
    ret, frame = cap.read()
    roi = frame[-size-200:-200, -size-300:-300]
    roi[np.where(final)] = 0
    roi += final
    image = cv2.flip(frame, 0)
    cv2.imshow('webcam', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()