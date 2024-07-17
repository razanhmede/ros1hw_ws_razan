#the temperature node subscribes to the tempearture topic of the tempearture publisher node 
#logs the temperature values to a text file 
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import time
import os

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(Float32,'temperature',self.listener_callback,10)
        log_dir = os.path.expanduser('~/home/ros2hw_ws_razan')
        os.makedirs(log_dir, exist_ok=True)
        self.log_file_path = os.path.join(log_dir, 'temperature_log.txt')

    def listener_callback(self, msg):
        temp_value = msg.data
        timestamp = time.time()  
        log_entry = f'{timestamp}, {temp_value} Celsius\n'

        with open(self.log_file_path, 'a') as file:
            file.write(log_entry)
            self.get_logger().info(f'Logged temperature: {temp_value} Celsius')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
