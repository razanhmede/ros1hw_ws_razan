#subscibes to temperature topic to take the float temperature values 
#checks if the temperature value being published is greater than the threshold 37
#publishes the alert trigger message in case of exceeding the threshold
import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32,String 


class ThresholdSubscriber(Node):
    def __init__(self):
        super().__init__('threshold_subscriber')
        #create subscriber to temperature topic
        self.subscription=self.create_subscription(Float32,'temperature',self.temperature_callback,10)
        #create publisher 
        self.publisher_=self.create_publisher(String,'alert_trigger',10)
        #specify the threshold
        self.threshold=36
    def temperature_callback(self, msg):
        temperature=msg.data
        self.get_logger().info('Temperature received : "%f"' % temperature)
        #check the threshold
        if msg.data>self.threshold:
            self.get_logger().info('Threshold exceeded! Temperature: {: .2f}'.format(msg.data))
            alert_msg= String()
            alert_msg.data='Tempearture exceeds threshold: "%f"' % temperature
            self.publisher_.publish(alert_msg)
            self.get_logger().info('Publishing trigger message: "%s"' % alert_msg.data)
def main(args=None):      
    rclpy.init(args=args)
    node = ThresholdSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()