

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
import math

class MotionController(Node):
    def __init__(self):
        super().__init__('motion_controller')

        self.goal = Point()
        self.goal.x = 1.0
        self.goal.y = 1.0

        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10)

        self.goal_sub = self.create_subscription(
            Point,
            '/goal',
            self.goal_callback,
            10)

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.k_linear = 0.5
        self.k_angular = 1.5
        self.distance_tolerance = 0.05

    def goal_callback(self, msg):
        self.goal = msg
        self.get_logger().info(f"New goal: ({msg.x}, {msg.y})")

    def odom_callback(self, msg):
        pos = msg.pose.pose.position
        orientation = msg.pose.pose.orientation

        # Convert quaternion to yaw
        siny_cosp = 2.0 * (orientation.w * orientation.z + orientation.x * orientation.y)
        cosy_cosp = 1.0 - 2.0 * (orientation.y * orientation.y + orientation.z * orientation.z)
        yaw = math.atan2(siny_cosp, cosy_cosp)

        dx = self.goal.x - pos.x
        dy = self.goal.y - pos.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < self.distance_tolerance:
            twist = Twist()
            self.cmd_pub.publish(twist)
            return

        angle_to_goal = math.atan2(dy, dx)
        angle_diff = self.normalize_angle(angle_to_goal - yaw)

        twist = Twist()
        twist.linear.x = self.k_linear * distance
        twist.angular.z = self.k_angular * angle_diff
        self.cmd_pub.publish(twist)

    @staticmethod
    def normalize_angle(angle):
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle

def main(args=None):
    rclpy.init(args=args)
    node = MotionController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
