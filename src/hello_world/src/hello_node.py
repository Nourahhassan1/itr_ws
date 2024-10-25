#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker(): 
    pub = rospy.Publisher('hello', String, queue_size=10)
    rospy.init_node('hello_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world" 
        pub.publish(String(data=hello_str))  # Corrected line
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
