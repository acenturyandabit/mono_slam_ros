cmake_minimum_required(VERSION 2.8.3)
project(cambridge)

find_package(catkin REQUIRED COMPONENTS
   rospy
   std_msgs
   message_generation
  cv_bridge
  image_transport
  sensor_msgs
  std_msgs
)

find_package(OpenCV REQUIRED)

 generate_messages(
   DEPENDENCIES
   std_msgs  # Or other packages containing msgs
 )
catkin_package(
CATKIN_DEPENDS message_runtime
)
include_directories(

 ${catkin_INCLUDE_DIRS}
)
