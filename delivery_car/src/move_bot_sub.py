#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def r_rear_speed_cb(data):
    rospy.loginfo("Subscribed right-rear wheel speed (m/s):  %f\n", data.data)

def l_rear_speed_cb(data):
    rospy.loginfo("Subscribed left-rear wheel speed (m/s):  %f\n", data.data)

def r_front_pos_cb(data):
    rospy.loginfo("Subscribed right-front wheel angle (rad):  %f\n", data.data)

def l_front_pos_cb(data):
    rospy.loginfo("Subscribed leftt-front wheel angle (rad):  %f\n", data.data)
    

if __name__ == '__main__':
    try:
        rospy.init_node('delivery_car_move_sub', anonymous=False)

        rospy.Subscriber("/delivery_car/right_rear_wheel_speed_control/command", Float64, r_rear_speed_cb)
        rospy.Subscriber("/delivery_car/left_rear_wheel_speed_control/command", Float64, l_rear_speed_cb)
        rospy.Subscriber("/delivery_car/right_front_wheel_pos_control/command", Float64, r_front_pos_cb)
        rospy.Subscriber("/delivery_car/left_front_wheel_pos_control/command", Float64, l_front_pos_cb)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

    except rospy.ROSInterruptException: 
        pass