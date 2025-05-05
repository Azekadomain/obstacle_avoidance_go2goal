import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')
        self.subscription = self.create_subscription(
            LaserScan,
            'lidar_scan',
            self.lidar_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.twist = Twist()

    def lidar_callback(self, msg):
        
        if min(msg.ranges) < 1.0:  
            self.twist.linear.x = 0.0  
            self.twist.angular.z = 1.0  
        else:
            self.twist.linear.x = 0.5  
            self.twist.angular.z = 0.0
        self.publisher_.publish(self.twist)

def main(args=None):
    rclpy.init(args=args)
    obstacle_avoidance = ObstacleAvoidance()
    rclpy.spin(obstacle_avoidance)
    obstacle_avoidance.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
