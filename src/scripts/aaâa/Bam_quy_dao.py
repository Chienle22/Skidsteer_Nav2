#!/usr/bin/env python3
import rclpy
import csv
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import FollowWaypoints
from rclpy.action import ActionClient
import math
import time

class ContinuousPathFollower(Node):
    def __init__(self, csv_file):
        super().__init__('continuous_path_follower')
        self.follow_waypoints_client = ActionClient(self, FollowWaypoints, 'follow_waypoints')
        self.csv_file = csv_file
        self.trajectory = self.load_trajectory()

    def load_trajectory(self):
        """
        Đọc file CSV và lưu danh sách waypoint.
        """
        trajectory = []
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    x, y, yaw = float(row['x']), float(row['y']), float(row['yaw'])
                    trajectory.append((x, y, yaw))
            self.get_logger().info(f"✅ Đã tải {len(trajectory)} điểm từ file CSV.")
        except Exception as e:
            self.get_logger().error(f"❌ Lỗi khi đọc file CSV: {e}")
        return trajectory

    def yaw_to_quaternion(self, yaw):
        """
        Chuyển đổi yaw (độ) thành quaternion (z, w) để sử dụng trong ROS.
        """
        z = math.sin(yaw / 2.0)
        w = math.cos(yaw / 2.0)
        return z, w

    def send_full_trajectory(self):
        """
        Gửi toàn bộ quỹ đạo đến FollowWaypoints để robot di chuyển liên tục.
        """
        if not self.trajectory:
            self.get_logger().error("❌ Không có quỹ đạo để bám theo!")
            return
        
        self.get_logger().info(f"🚀 Gửi {len(self.trajectory)} waypoint đến FollowWaypoints.")

        # Tạo danh sách PoseStamped
        waypoints = []
        for i, (x, y, yaw) in enumerate(self.trajectory):
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.position.z = 0.0

            z, w = self.yaw_to_quaternion(yaw)
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = z
            pose.pose.orientation.w = w

            waypoints.append(pose)

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints

        # Đợi server FollowWaypoints sẵn sàng
        self.follow_waypoints_client.wait_for_server()

        # Gửi toàn bộ waypoint
        send_goal_future = self.follow_waypoints_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('❌ Goal bị từ chối!')
            return

        self.get_logger().info("✅ FollowWaypoints đang chạy, robot sẽ di chuyển LIÊN TỤC!")

        # Chờ hoàn thành
        get_result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, get_result_future)

        self.get_logger().info("✅ Quỹ đạo hoàn thành!")

def main():
    rclpy.init()
    csv_path = "trajectory.csv"  # Đường dẫn file CSV
    follower = ContinuousPathFollower(csv_path)
    follower.send_full_trajectory()
    follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
