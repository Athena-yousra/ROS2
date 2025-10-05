from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='yolo',
            executable='yolo_node',
            name='yolo_node',
            output='screen'
        )
    ])
