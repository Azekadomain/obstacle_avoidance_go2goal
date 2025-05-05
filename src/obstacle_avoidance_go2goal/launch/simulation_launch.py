from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='obstacle_avoidance_go2goal',
            executable='lidar_reader',
            name='lidar_reader',
            output='screen',
        ),
        Node(
            package='obstacle_avoidance_go2goal',
            executable='goal_publisher',
            name='goal_publisher',
            output='screen',
        ),
        Node(
            package='obstacle_avoidance_go2goal',
            executable='obstacle_avoidance',
            name='obstacle_avoidance',
            output='screen',
        ),
        Node(
            package='obstacle_avoidance_go2goal',
            executable='go_to_goal',
            name='go_to_goal',
            output='screen',
        ),
        Node(
            package='obstacle_avoidance_go2goal',
            executable='motion_controller',
            name='motion_controller',
            output='screen',
        ),
        Node(
            package='obstacle_avoidance_go2goal',
            executable='robot_interface',
            name='robot_interface',
            output='screen',
        ),
    ])

