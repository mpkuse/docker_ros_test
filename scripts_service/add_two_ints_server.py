#!/usr/bin/env python
import rospy
from docker_ros_test.srv import *


def handle_req( req ):
    print 'Got requested with inputs : ', req.a, '\t', req.b
    return AddTwoIntsResponse( req.a + req.b )


rospy.init_node( 'add_two_ints_server' )
s = rospy.Service( 'add_two_ints', AddTwoInts, handle_req )
print 'service is up'
rospy.spin()
