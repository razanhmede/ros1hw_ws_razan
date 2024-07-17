import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class AlertPublisher(Node):
    def __init__(self):
        super().__init__('alert_publisher')
        self.publisher_=self.create_publisher(String,'alert',10)
        self.subscription=self.create_subscription(String,'alert_publisher',self.alert_callback,10)
    def alert_callback(self, msg):
        self.get_logger().info('Received alert trigger: "%s"' %msg.data)
        alert_msg= String()
        alert_msg.data='Alert: Temperature exceeded threshold'
        self.publisher_.publish(alert_msg)
        self.get_logger().info('Publishing alert : "%s"' %alert_msg.data)
def main(args=None):
    rclpy.init(args=args)
    node = AlertPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()