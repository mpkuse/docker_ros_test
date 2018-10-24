#!/usr/bin/python

import rospy
from visualization_msgs.msg import Marker

def talker():
    pub = rospy.Publisher('chatter_marker', Marker, queue_size=10)
    rospy.init_node('talker_marker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    i=0
    while not rospy.is_shutdown():
        hello_str = "marker hello %d %s" %(i, rospy.get_time() )
        rospy.loginfo(hello_str)

        marker = Marker()
        marker.header.frame_id = "/world"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = i
        marker.scale.y = i
        marker.scale.z = i
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 1.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = 1.
        marker.pose.position.y = 0.
        marker.pose.position.z = 0.

        pub.publish(marker)
        rate.sleep()
        i+=1
        i = i%100

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
