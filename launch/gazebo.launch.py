from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess
import os

def generate_launch_description():

    pkg_description = get_package_share_directory('kuka_kr210_arm')
    urdf_file = os.path.join(pkg_description, "urdf","kr210.urdf")


    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["gazebo","-s","libgazebo_ros_factory.so"],      # running gazebo and communicate with ros
                output="screen",
            ),
            Node(
                package="gazebo_ros",                                  # Spawn the robot
                node_executable="spawn_entity.py",
                arguments=["-entity","kuka_kr210_arm","-b","-file",urdf_file,],
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                arguments=[urdf_file],
            ),
        
        ]
    )