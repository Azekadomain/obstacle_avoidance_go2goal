import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class GoalPublisher(Node):
    def __init__(self):
        super().__init__('goal_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, 'goal', 10)
        self.goal_position = PoseStamped()
        self.goal_position.pose.position.x = 1.0
        self.goal_position.pose.position.y = 1.0
        self.goal_position.pose.orientation.w = 1.0
        self.create_timer(1.0, self.publish_goal)

    def publish_goal(self):
        self.publisher_.publish(self.goal_position)

def main(args=None):
    rclpy.init(args=args)
    goal_publisher = GoalPublisher()
    rclpy.spin(goal_publisher)
    goal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
