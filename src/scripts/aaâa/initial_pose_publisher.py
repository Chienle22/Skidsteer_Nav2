#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
import time

class InitialPosePublisher(Node):
    def __init__(self):
        super().__init__('initial_pose_publisher')
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)
        timer_period = 2.0  # delay để đợi amcl và rviz load
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = PoseWithCovarianceStamped()
        msg.header.frame_id = 'map'
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.pose.pose.position.x = 2.5
        msg.pose.pose.position.y = 17.0
        msg.pose.pose.position.z = 0.0
        import math
        from tf_transformations import quaternion_from_euler
        q = quaternion_from_euler(0, 0, 0.0)  # góc quay z = 0.0 rad
        msg.pose.pose.orientation.x = q[0]
        msg.pose.pose.orientation.y = q[1]
        msg.pose.pose.orientation.z = q[2]
        msg.pose.pose.orientation.w = q[3]

        # Optional: set covariance (identity matrix or custom)
        msg.pose.covariance[0] = 0.25  # x
        msg.pose.covariance[7] = 0.25  # y
        msg.pose.covariance[35] = 0.06853892326654787  # yaw

        self.publisher_.publish(msg)
        self.get_logger().info('Published initial pose.')
        self.destroy_node()  # chỉ publish 1 lần

def main(args=None):
    rclpy.init(args=args)
    node = InitialPosePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
