import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleDrawer(Node):
    def __init__(self):
        super().__init__('circle_drawer')
        # 创建发布者
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # 设定定时器
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    circle_drawer = CircleDrawer()
    rclpy.spin(circle_drawer)
    circle_drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
