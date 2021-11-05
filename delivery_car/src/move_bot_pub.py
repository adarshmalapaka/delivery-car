#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


def go_straight():

    rospy.loginfo("Publishing command to accelerate Robot straight until 8.0 m/s")

    # Setting the front wheels angle at 0 rad.
    pub_right_turn.publish(0.0)
    pub_left_turn.publish(0.0)
    rospy.loginfo("Published angle to robot (rad): " + str(0.0))

    forward_speed = 0.0

    while (forward_speed < 8.0):

        rospy.loginfo("Published speed to robot (m/s): " + str(forward_speed))
        # Moving the delivery robot straight with forward_speed
        pub_right_wheel.publish(forward_speed)
        pub_left_wheel.publish(forward_speed)
        forward_speed += 0.1
        rospy.sleep(rospy.Duration(0.1)) 

    # Stopping the robot
    pub_right_wheel.publish(0.0)
    pub_left_wheel.publish(0.0)

    # Calling the go_loop() function to make the Robot move in a loop
    go_loop()


def go_loop():

    rospy.loginfo("Publishing command to move Robot in a loop")

    while (not rospy.is_shutdown()):
        # Setting the front wheels angle at 0.5 rads to turn
        pub_right_turn.publish(0.5)
        pub_left_turn.publish(0.5)
        # Setting the rear wheels speed at 8.0 m/s to move
        pub_right_wheel.publish(8.0)
        pub_left_wheel.publish(8.0)
        rospy.loginfo("Published speed to robot (m/s): " + str(8.0))
        rospy.loginfo("Published angle to robot (rad): " + str(0.5))

    # Stopping the robot
    pub_right_wheel.publish(0.0)
    pub_left_wheel.publish(0.0)

if __name__ == '__main__':
    try:

        # inititalizing node
        rospy.init_node('delivery_car_move_pub', anonymous=False)

        # rear wheel velocity publishers
        pub_right_wheel = rospy.Publisher('/delivery_car/right_rear_wheel_speed_control/command', Float64, queue_size=10) 
        pub_left_wheel = rospy.Publisher('/delivery_car/left_rear_wheel_speed_control/command', Float64, queue_size=10)

        # front wheel angle publishers
        pub_right_turn = rospy.Publisher('/delivery_car/right_front_wheel_pos_control/command', Float64, queue_size=10)
        pub_left_turn = rospy.Publisher('/delivery_car/left_front_wheel_pos_control/command', Float64, queue_size=10)

        go_straight()

    except rospy.ROSInterruptException: 
        pass