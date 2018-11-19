#include <ros/ros.h>
#include <docker_ros_test/AddTwoInts.h>

bool add( docker_ros_test::AddTwoInts::Request & req, docker_ros_test::AddTwoInts::Response & res )
{
    ROS_INFO( "se");
    return true;
}

int main( int argc, char ** argv )
{
    ros::init( argc, argv, "add_two_ints_server_cpp" );
    ros::NodeHandle n;

    ros::ServiceServer service = n.advertiseService( "add_two_ints", add );
    ROS_INFO( "service is up");
    ros::spin();

    return 0;
}
