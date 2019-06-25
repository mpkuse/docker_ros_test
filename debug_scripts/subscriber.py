#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu


prev_t = rospy.Time()

def callback(data):
    global prev_t
    curr_t = data.header.stamp
    # print( 'IMU with t=', data.header.stamp )

    print( 'IMU with t=', curr_t.secs, curr_t.nsecs )

    if data.header.stamp <= prev_t:
        print( 'imu message in disorder!, curr_t=', curr_t, ' prev_t=', prev_t )

    prev_t = data.header.stamp

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    print( 'init node')
    rospy.init_node('listener', anonymous=True)

    sub_topic = "/camera/imu"
    print( 'Subscribe to topic: ', sub_topic )
    rospy.Subscriber(sub_topic, Imu, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
