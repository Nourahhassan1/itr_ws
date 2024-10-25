#!/usr/bin/env python3
from symbol import and_expr

import rospy
import random
import math
from turtlesim.msg import Pose
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

RANGE_DISTANCE = 4
ARRIVAL_THRESHOLD = 0.2
MAX_TIME=30

MAX_LINEAR_VELOCITY = 3
MAX_ANGULAR_VELOCITY = math.pi

first_pose = None
had_moved = False
was_in_range = False

phase_1_start = None
phase_2_start = None
phase_2_end = None

files_written = False

velocity_valid = True

def save_crash():
    with open("phase1.txt", "a") as file:
        file.write(f"{MAX_TIME}\n")
        file.close()

    with open("phase2.txt", "a") as file:
        file.write(f"{MAX_TIME}\n")
        file.close()

    with open("crashes.txt", "a") as file:
        file.write(f"crash at {target_x} {target_y}\n")
        file.close()

def save_results():

    if not velocity_valid:
        rospy.logerr("detected velocity violation, ignoring this run")
        return

    if phase_1_start is not None:
        duration_phase_1 = phase_2_start - phase_1_start

        with open("phase1.txt", "a") as file:
            file.write(f"{duration_phase_1.to_sec()} \n")
            file.close()

    duration_phase_2 = phase_2_end - phase_2_start
    with open("phase2.txt", "a") as file:
        file.write(f"{duration_phase_2.to_sec()} \n")
        file.close()

    global files_written
    files_written = True

def handle_timing(distance: float, msg: Pose):

    global had_moved
    global was_in_range

    global phase_1_start
    global phase_2_start
    global phase_2_end

    in_range = distance < RANGE_DISTANCE
    moved = first_pose.x != msg.x or first_pose.y != msg.y or first_pose.theta != msg.theta

    if not had_moved and moved and not in_range:  # starting phase 1

        phase_1_start = rospy.get_rostime()
        rospy.loginfo("starting phase 1")

    if moved and not was_in_range and in_range:  # starting phase 2

        phase_2_start = rospy.get_rostime()
        rospy.loginfo("starting phase 2")
        was_in_range = in_range

    if distance <= ARRIVAL_THRESHOLD and phase_2_end is None:
        if phase_2_start is None:                   #if the goal is near the starting state, distance can be in threshold before the turtle has moved
            phase_2_start = rospy.get_rostime()
        phase_2_end = rospy.get_rostime()
        rospy.loginfo("ending phase 2")
        save_results()      #this is a slow operation that shouldn't be done in a message handler, but the task is done
                            #so even if we miss a few messages it doesn't matter.

    had_moved = moved

def check_distance(msg: Pose):

    global first_pose

    if first_pose is None:
        first_pose = msg

    # Calculate the distance between the turtle and the random point
    distance = math.sqrt((target_x - msg.x) ** 2 + (target_y - msg.y) ** 2)

    handle_timing(distance,msg)

    # If the turtle is within RANGE_DISTANCE meters of the point, publish the distance
    if distance < RANGE_DISTANCE:
        #rospy.loginfo(f"Turtle is {distance:.2f} meters from the target point")
        beacon_publisher.publish(distance)

def check_velocity(vel: Twist):
    global velocity_valid

    if velocity_valid:
        velocity_valid = MAX_LINEAR_VELOCITY >= vel.linear.x  >= 0 == vel.linear.y and -MAX_ANGULAR_VELOCITY <= vel.angular.z <= MAX_ANGULAR_VELOCITY


rospy.init_node('beacon_node', anonymous=True)

in_centre = True

while in_centre:
    # Define a random point with x and y coordinates between 0 and 11
    target_x = random.uniform(0, 11)
    target_y = random.uniform(0, 11)

    in_centre = 5 < target_x < 6 and 5 < target_y < 6 #avoid points near the initial state



rospy.loginfo(f"Random target point set at: ({target_x}, {target_y})")

# Subscribers
pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, check_distance)
vel_subscriber = rospy.Subscriber('/turtle1/cmd_vel', Twist, check_velocity)

# Publisher to the "beacon" topic
beacon_publisher = rospy.Publisher('/beacon', Float32, queue_size=10)

rospy.spin()


if not files_written:   #in case the key_finder node stoppedIT defcakked  before reaching the end of phase two
    save_crash()