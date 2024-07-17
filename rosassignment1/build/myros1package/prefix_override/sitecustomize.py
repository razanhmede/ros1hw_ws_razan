import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/razanhmede/ros1hw_ws_razan/rosassignment1/install/myros1package'
