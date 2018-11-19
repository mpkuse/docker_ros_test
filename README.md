# Sample ROS Publisher

Contains two sample publishers to check/verify connection between separate ros terminals.

- [scripts/pub_text.py](scripts/pub_text.py) : Publish a std_msgs::String
- [scripts/pub_marker.py](scripts/pub_marker.py) : Publish a visualization_msgs::Marker


## How to use ROS with docker
If you are a computer vision/robotics researcher or an engineerer checkout my blog post on
what docker can do for you. [HERE](https://kusemanohar.wordpress.com/2018/10/03/docker-for-computer-vision-researchers/).
Following is a checklist to get this sample nodes running on ros on docker. 

- Run the container image. You may use my images which has ros.  [hub.docker/mpkuse](https://hub.docker.com/r/mpkuse/kusevisionkit/).
```
$(host) docker run -ti mpkuse/kusevisionkit:ros-kinetic-vins
```
- Setup a catkin_ws. See [ros-tutorials](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
on how to setup a catkin_ws.
```
$(container) mkdir -p ~/catkin_ws/src
$(container) cd ~/catkin_ws/
$(container) catkin_make
$(container) source devel/setup.bash
```
- Using `docker inspect <container name>` ​get the IP address of the container. Assuming the ip address of container is 172.17.0.2 and the hosts's ip-address is 172.17.0.1. 
- Edit the `/etc/hosts` file on the host and also on docker so that both docker-container and hosts knows each other. This is needed for roscore to work correctly. It looks something like below. Assuming deephorse is hostname of the host PC and ​
0ef6065d7b27 is the container id. 
```
172.17.0.2 0ef6065d7b27
172.17.0.1 deephorse
```
- Make sure container can ping to host with hostname and host can pind container with container id. 
```
$(host) ping 0ef6065d7b27
$(container) ping deephorse. 
```
- ```
$(container) roscore
$(host) export ROS_MASTER_URI=http://0ef6065d7b27:11311/
```
- Run a dummy node and see if you can receive messages on the host PC. You may like to use my dummy node. https://github.com/mpkuse/docker_ros_test
```
$(container) cd ~/catkin_ws/src
$(container) git clone https://github.com/mpkuse/docker_ros_test
$(container) cd ~/catkin_ws
$(container) catkin_make
$(container) rosrun docker_ros_test pub_text.py
```
- Verify the host can receive the messages.
```
$(host) rostopic list
/chatter
/rosout
/rosout_agg
$(host) rostopic echo /chatter
$(host) rostopic echo /chatter
data: hello world 1542596296.97
---
data: hello world 1542596297.07
---
.
.
```

Congratulations..!!!
You have successfully setup ros on docker.
