# mono_slam_ros
A stepped through guide of how to get monoslam working in ROS.

## Usage
1. Install ROS: http://www.ros.org/ (I used Kinetic Kame.)
2. Download this and put it in your workspace.
3. catkin_make
3.1. Get a webcam.
4. roslaunch mono-slam monoslam.launch
5. In the rviz window, make sure to set the fixed-frame to be world, rather than map!
6. Add mono-slam/camera_poses/path.
7. Enjoy!

# Credits
Full credits for the algorithm go to https://github.com/rrg-polito/mono-slam.
I do however take the credit for spending 3+ hours actually getting all the rest of the stuff to work :/
