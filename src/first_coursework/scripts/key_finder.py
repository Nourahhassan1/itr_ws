#!/usr/bin/env/ python3
import rospy
from math import *
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float64, String

rospy.init_node('beacon_node', Anonymous = True)

cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 100)
current_pose = Pose()
pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, dist_pub)

