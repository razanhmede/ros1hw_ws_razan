from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'myros1package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py'))
    ],
    install_requires=['setuptools', 'rclpy', 'std_msgs','myros1package_msgs'],
    zip_safe=True,
    maintainer='razanhmede',
    maintainer_email='razan.hmede@lau.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_publisher = myros1package.temperature_publisher :main',
            'threshold_subscriber=myros1package.threshold_subscriber:main',
            'alert_publisher=myros1package.alert_publisher:main',
            'temperature_logger=myros1package.temperature_logger:main'
        ],
    },
)
