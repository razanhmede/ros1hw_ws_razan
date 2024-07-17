import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32
import random 
import time 

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_=self.create_publisher(Float32, 'temperature',10)
        self.timer =self.create_timer(1.0,self.publish_temperature)
    def publish_temperature(self):
        temperature =random.uniform(17.0,37.0) #generate regular random temperature values between 17 and 37
        msg =Float32()
        msg.data=temperature
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing temperature: {:.2f}'.format(temperature))

def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

    
    

