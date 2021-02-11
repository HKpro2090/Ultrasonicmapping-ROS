import rospy
from std_msgs.msg import Int16
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
class Server:
    def __init__(self):
        self.angle = None
        self.distance = None
        self.xdistance = None
        self.ydistance = None
        self.count = 0

    def angle_callback(self, msg):
        self.angle = msg.data
        self.compute_stuff()

    def distance_callback(self, msg):
        self.distance = msg.data
        self.compute_stuff()

    def compute_stuff(self):
        if self.angle is not None and self.distance is not None:
            temp = str(self.angle) + ' '+ str(self.distance)
            print(temp)
            log.write((temp+'\n'))
            self.count +=1
            #print(self.count)
            if self.count >= 800:
                log.close()
                rospy.signal_shutdown('Hello')
            #self.xdistance = round((self.distance * math.sin(self.angle)),2)
            #self.ydistance = round((self.distance * math.cos(self.angle)),2)
            #print(self.xdistance,' ',self.ydistance)
            #plt.polar(math.radians(self.angle), self.distance,'o')
            #plt.pause(0.000001)
            



if __name__ == '__main__':
    rospy.init_node('listener')
    server = Server()
    log = open('log1.txt','w')
    #plt.axes(projection='polar')
    #plt.xlim(-100,100)
    #plt.ylim(0,100)
    rospy.Subscriber('angle',Int16,server.angle_callback)
    rospy.Subscriber('sensorvalues',Int16,server.distance_callback)
    rospy.spin()
    #plt.show(block=True)