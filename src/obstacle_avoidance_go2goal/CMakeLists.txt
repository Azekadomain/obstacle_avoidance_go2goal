cmake_minimum_required(VERSION 3.5)
project(obstacle_avoidance_go2goal)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(webots_ros2_core REQUIRED)

install(PROGRAMS
  obstacle_avoidance_go2goal/obstacle_avoidance.py
  obstacle_avoidance_go2goal/go_to_goal.py
  obstacle_avoidance_go2goal/lidar_reader.py
  obstacle_avoidance_go2goal/goal_publisher.py
  obstacle_avoidance_go2goal/motion_controller.py
  obstacle_avoidance_go2goal/robot_interface.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
