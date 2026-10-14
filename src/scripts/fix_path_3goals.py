#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped, Twist
from nav_msgs.msg import Odometry, Path
import csv
import time
import os

class DataSaver(Node):
    def __init__(self):
        super().__init__('data_saver')

        # === GIỮ NGUYÊN ĐƯỜNG DẪN GỐC CỦA BẠN ===
        script_path = '/home/chienle/Desktop/nav2_ws/src/scripts'
        amcl_dir = os.path.join(script_path, 'amcl')              # Thư mục lưu AMCL
        path_dir = os.path.join(script_path, 'path')              # Thư mục lưu Local Plan
        odom_dir = os.path.join(script_path, 'odom')              # Thư mục lưu Odom
        cmd_vel_dir = os.path.join(script_path, 'cmd_vel')        # Thư mục lưu Cmd Vel
        first_path_dir = os.path.join(script_path, 'first_path')  # Thư mục lưu Reference Path (đã bật lại)

        # Tạo thư mục nếu chưa tồn tại
        os.makedirs(amcl_dir, exist_ok=True)
        os.makedirs(path_dir, exist_ok=True)
        os.makedirs(odom_dir, exist_ok=True)
        os.makedirs(cmd_vel_dir, exist_ok=True)
        os.makedirs(first_path_dir, exist_ok=True)

        # Lấy thời gian hiện tại để tạo tên file
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        # Đặt tên file chuẩn
        self.amcl_filename = os.path.join(amcl_dir, f'amcl_data_{timestamp}.csv')
        self.path_filename = os.path.join(path_dir, f'local_plan_data_{timestamp}.csv')
        self.odom_filename = os.path.join(odom_dir, f'odom_data_{timestamp}.csv')
        self.cmd_vel_filename = os.path.join(cmd_vel_dir, f'cmd_vel_data_{timestamp}.csv')
        self.first_path_filename = os.path.join(first_path_dir, f'first_path_data_{timestamp}.csv')

        # Mở file CSV với buffering=1 để ghi trực tiếp xuống ổ cứng tránh kẹt dữ liệu
        self.amcl_file = open(self.amcl_filename, mode='w', newline='', buffering=1)
        self.path_file = open(self.path_filename, mode='w', newline='', buffering=1)
        self.odom_file = open(self.odom_filename, mode='w', newline='', buffering=1)
        self.cmd_vel_file = open(self.cmd_vel_filename, mode='w', newline='', buffering=1)
        self.first_path_file = open(self.first_path_filename, mode='w', newline='', buffering=1)

        self.amcl_writer = csv.writer(self.amcl_file)
        self.path_writer = csv.writer(self.path_file)
        self.odom_writer = csv.writer(self.odom_file)
        self.cmd_vel_writer = csv.writer(self.cmd_vel_file)
        self.first_path_writer = csv.writer(self.first_path_file)

        # Ghi tiêu đề cho các file CSV
        self.amcl_writer.writerow(['timestamp', 'x', 'y', 'z', 'orientation_x', 'orientation_y', 'orientation_z', 'orientation_w'])
        self.path_writer.writerow(['timestamp', 'x', 'y', 'z'])
        self.odom_writer.writerow(['timestamp', 'x', 'y', 'z', 'orientation_x', 'orientation_y', 'orientation_z', 'orientation_w'])
        self.cmd_vel_writer.writerow(['timestamp', 'linear_x', 'linear_y', 'angular_z'])
        self.first_path_writer.writerow(['timestamp', 'x', 'y', 'z'])

        # Tập hợp dùng để lọc trùng lặp các điểm quỹ đạo toàn cục qua các lần replanning/chuyển goal
        self.recorded_path_points = set()

        # Subcribe vào các topic
        self.amcl_subscription = self.create_subscription(
            PoseWithCovarianceStamped, '/amcl_pose', self.amcl_listener_callback, 10)

        self.path_subscription = self.create_subscription(
            Path, '/plan', self.path_listener_callback, 10)

        self.odom_subscription = self.create_subscription(
            Odometry, '/odom', self.odom_listener_callback, 10)

        self.cmd_vel_subscription = self.create_subscription(
            Twist, '/cmd_vel', self.cmd_vel_listener_callback, 10)

        # Subscribe vào topic /plan để gom trọn vẹn đa chặng quỹ đạo (hình chữ L)
        self.first_path_subscription = self.create_subscription(
            Path, '/plan', self.first_path_listener_callback, 10)

        self.get_logger().info("DataSaver node đã khởi động với đầy đủ đường dẫn gốc và gom đủ quỹ đạo chữ L!")

    def amcl_listener_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec
        p = msg.pose.pose.position
        o = msg.pose.pose.orientation
        self.amcl_writer.writerow([timestamp, p.x, p.y, p.z, o.x, o.y, o.z, o.w])

    def path_listener_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec
        for pose in msg.poses:
            p = pose.pose.position
            self.path_writer.writerow([timestamp, p.x, p.y, p.z])

    def first_path_listener_callback(self, msg):
        """Thu thập liên tục các điểm từ /plan, tự động lọc trùng để gom đủ cả đoạn ngang và dọc chữ L"""
        timestamp = self.get_clock().now().to_msg().sec
        for pose in msg.poses:
            p = pose.pose.position
            point_key = (round(p.x, 4), round(p.y, 4))
            if point_key not in self.recorded_path_points:
                self.recorded_path_points.add(point_key)
                self.first_path_writer.writerow([timestamp, p.x, p.y, p.z])

    def odom_listener_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec
        p = msg.pose.pose.position
        o = msg.pose.pose.orientation
        self.odom_writer.writerow([timestamp, p.x, p.y, p.z, o.x, o.y, o.z, o.w])

    def cmd_vel_listener_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec
        self.cmd_vel_writer.writerow([timestamp, msg.linear.x, msg.linear.y, msg.angular.z])

    def destroy_node(self):
        # Đóng các file CSV khi node bị hủy
        self.amcl_file.close()
        self.path_file.close()
        self.odom_file.close()
        self.cmd_vel_file.close()
        self.first_path_file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    data_saver = DataSaver()

    try:
        rclpy.spin(data_saver)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            data_saver.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
