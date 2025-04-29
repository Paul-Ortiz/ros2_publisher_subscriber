import sys
if sys.prefix == 'E:\\Python310':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = 'E:\\ros2_ws\\install\\py_pubsub'
