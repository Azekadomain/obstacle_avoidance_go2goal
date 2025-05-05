

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Point

class RobotInterface(Node):
    def __init__(self):
        super().__init__('robot_interface')

        # Subscribe to LIDAR
        self.lidar_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            10)

        # Subscribe to motion commands
        self.cmd_vel_sub = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10)

        # Subscribe to goal (optional)
        self.goal_sub = self.create_subscription(
            Point,
            '/goal',
            self.goal_callback,
            10)

        # Publisher to drive the robot
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel_out', 10)

        self.latest_scan = None
        self.goal_point = None

    def lidar_callback(self, msg):
        self.latest_scan = msg

    def goal_callback(self, msg):
        self.goal_point = msg
        self.get_logger().info(f'Goal received: ({msg.x}, {msg.y})')

    def cmd_vel_callback(self, msg):
        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotInterface()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
