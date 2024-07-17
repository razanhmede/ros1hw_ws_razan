#the temperature node subscribes to the tempearture topic of the tempearture publisher node 
#logs the temperature values to a text file 
import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32
import os

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription=self.create_subscription(Float32,'temperature', self.listener_callback,10)
        #open a log file in append mode to write the temperature values to it 
        log_dir = os.path.join(os.path.expanduser('~'), 'temperature_logs')
        os.makedirs(log_dir, exist_ok=True)
        self.log_file = open(os.path.join(log_dir, 'temperature_log.txt'), 'a')
    def listener_callback(self, msg):
        temp_value = msg.data
        self.get_logger().info(f'Logging temperature: {temp_value}')
        #include time stamp and temperature value 
        self.log_file.write(f'{self.get_clock().now().to_msg().sec}, {temp_value}\n')
    def destroy_node(self):
        self.log_file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()




