#!/usr/bin/env python3
import rospy
import math
import angles
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float64, String, Float32
from first_coursework.msg import Intention

rospy.init_node('key_finder', anonymous = True)
cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
rate = rospy.Rate(10)

pose = None
beacon_position = None

def getDistance(dist: Float32):
    global distance_to_beacon
    distance_to_beacon = dist.data

def getPose(pose_msg: Pose):
    global pose
    pose = pose_msg


def moveTurtle():
    global pose, beacon_position

    if pose is not None and beacon_position is not None:
        msg = Twist()

    diff = (beacon_position[0] - pose.x, beacon_position[1] - pose.y)
    beacon_position = math.atan2(diff[1], diff[0])

    angle_diff = angles.shortest_angular_distance(pose.theta, beacon_position)

    if angle_diff < -0.087 or angle_diff > 0.087:
        msg.angular.z = -1
    elif math.hypot(*diff) > 0.3:
        msg.linear.x = 1

    cmd_pub.publish(msg)

beacon_sub = rospy.Subscriber('/beacon', Float32, getDistance)
pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, getPose)

while not rospy.is_shutdown():
    moveTurtle()
    rate.sleep()







