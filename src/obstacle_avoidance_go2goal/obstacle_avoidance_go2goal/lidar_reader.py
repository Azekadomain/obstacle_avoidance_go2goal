import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from webots_ros2_core.device import Lidar

class LidarReader(Node):
    def __init__(self):
        super().__init__('lidar_reader')
        self.publisher_ = self.create_publisher(LaserScan, 'lidar_scan', 10)
        self.lidar = Lidar("LDS-01")
        self.lidar.enable(64)
        self.create_timer(0.1, self.timer_callback)  

    def timer_callback(self):
        lidar_values = self.lidar.get_range_image()
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.angle_min = -1.57
        msg.angle_max = 1.57
        msg.angle_increment = 0.01
        msg.ranges = lidar_values
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    lidar_reader = LidarReader()
    rclpy.spin(lidar_reader)
    lidar_reader.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
