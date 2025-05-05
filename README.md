# Obstacle Avoidance and Go-To-Goal for TurtleBot3 in Webots

This project implements obstacle avoidance and goal-directed motion using a LIDAR-equipped TurtleBot3 robot in the Webots simulator. Developed using ROS 2 (Humble).

ros2_ws/
└── src/
    └── obstacle_avoidance_go2goal/
        ├── launch/
        │   └── simulation_launch.py
        ├── world/
        │   └── turtlebot3_burger.wb
        ├── obstacle_avoidance_go2goal/
        │   ├── __init__.py
        │   ├── lidar_reader.py
        │   ├── goal_publisher.py
        │   ├── obstacle_avoidance.py
        │   ├── go_to_goal.py
        │   ├── motion_controller.py
        │   └── robot_interface.py
        ├── package.xml
        └── CMakeLists.txt
