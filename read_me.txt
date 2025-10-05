first install 

sudo apt install ros-humble-ros-ign-bridge
pip install ultralytics
pip install "numpy<2" --upgrade


in first terminal launch 
 
cd CRTI/src/sdf
export IGN_GAZEBO_RESOURCE_PATH=/home/souhib/CRTI/models:$IGN_GAZEBO_RESOURCE_PATH
ign gazebo word_demo.sdf 


in another terminal launch
ros2 run ros_ign_bridge parameter_bridge   /camera@sensor_msgs/msg/Image[ignition.msgs.Image


in last 

python3 yolo_node.py

