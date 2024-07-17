import rclpy
from rclpy.node import Node 
from myros1package_msgs.msg import Alert

class AlertPublisher(Node):
    def __init__(self):
        super().__init__('alert_publisher')
        self.subscription=self.create_subscription(Alert,'alert_publisher',self.alert_callback,10)
    def alert_callback(self, msg):
        self.get_logger().info('Alert Triggered! Temperature: {: .2f}'.format(msg.temperature))
def main(args=None):
    rclpy.init(args=args)
    node = AlertPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()