from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_detection',
            executable='yolov8_ros2_pt',  # Adjusted this line
            name='yolov8_ros2_pt_node',
            output='screen',
        ),
    ])