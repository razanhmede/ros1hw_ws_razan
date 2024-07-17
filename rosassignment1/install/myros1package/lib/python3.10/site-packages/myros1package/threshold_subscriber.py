#subscibes to temperature topic to take the float temperature values 
#checks if the temperature value being published is greater than the threshold 37
#publishes the alert trigger message in case of exceeding the threshold
import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32 
from myros1package_msgs.msg import Alert

class ThresholdSubscriber(Node):
    def __init__(self):
        super().__init__('threshold_subscriber')
        self.subscription=self.create_subscription(Float32,'temperature',self.temperature_callback,10)
        self.publisher_=self.create_publisher(Alert,'alert_trigger',10)
        self.threshold=36
    def temperature_callback(self, msg):
        if msg.data>self.threshold:
            alert_msg=Alert()
            alert_msg.tempearture=msg.data
            self.publisher_.publish(alert_msg)
            self.get_logger().info('Threshold exceeded! Temperature: {: .2f}'.format(msg.data))
def main(args=None):
    rclpy.init(args=args)
    node = ThresholdSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()