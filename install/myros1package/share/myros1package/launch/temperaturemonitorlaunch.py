import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='myros1package',
            executable='temperature_publisher',
            name='temperature_publisher',
            output='screen'
        ),
        Node(
            package='myros1package',
            executable='threshold_subscriber',
            name='threshold_subscriber',
            output='screen'
        ),
        Node(
            package='myros1package',
            executable='alert_publisher',
            name='alert_publisher',
            output='screen'
        ),
    ])

if __name__ == '__main__':
    generate_launch_description()
