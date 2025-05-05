import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped

class GoToGoal(Node):
    def __init__(self):
        super().__init__('go_to_goal')
        self.subscription = self.create_subscription(
            PoseStamped,
            'goal',
            self.goal_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.twist = Twist()

    def goal_callback(self, msg):
        
        target_x = msg.pose.position.x
        target_y = msg.pose.position.y
        self.twist.linear.x = 0.5  
        self.twist.angular.z = 0.0  
        self.publisher_.publish(self.twist)

def main(args=None):
    rclpy.init(args=args)
    go_to_goal = GoToGoal()
    rclpy.spin(go_to_goal)
    go_to_goal.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
