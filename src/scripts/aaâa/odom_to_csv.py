#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class OdomToCSVWithPlot(Node):
    def __init__(self):
        super().__init__('odom_to_csv_with_plot_node')

        # Subscribe đến topic /odom
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        # Tạo file CSV để ghi dữ liệu
        self.csv_file_path = 'odom_data.csv'
        self.create_csv_file()

        # Danh sách lưu dữ liệu để vẽ
        self.x_data = []
        self.y_data = []

        # Cài đặt biểu đồ
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'bo-', label='Path')
        self.ax.set_title('Real-time Odometry Plot')
        self.ax.set_xlabel('X Position')
        self.ax.set_ylabel('Y Position')
        self.ax.legend()
        self.ax.grid(True)

        # Biến toàn cục để giữ FuncAnimation
        global anim
        anim = FuncAnimation(
            self.fig,
            self.update_plot,
            interval=200,
            cache_frame_data=False  # Tắt bộ đệm khung hình
        )
        plt.show()  # Sử dụng block=True để giữ cửa sổ biểu đồ mở

    def create_csv_file(self):
        """Tạo file CSV và ghi header"""
        try:
            with open(self.csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['x', 'y', 'timestamp'])  # Header của CSV
            self.get_logger().info(f'File CSV đã được tạo: {self.csv_file_path}')
        except Exception as e:
            self.get_logger().error(f'Lỗi khi tạo file CSV: {e}')

    def odom_callback(self, msg):
        """Xử lý dữ liệu từ topic /odom và ghi vào file CSV"""
        try:
            # Lấy thông tin tọa độ từ message Odometry
            x = msg.pose.pose.position.x
            y = msg.pose.pose.position.y
            timestamp = self.get_clock().now().to_msg().sec

            # Lưu dữ liệu vào danh sách và CSV
            with open(self.csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([x, y, timestamp])
            self.x_data.append(x)
            self.y_data.append(y)

            # Log thông tin
            self.get_logger().info(f'Ghi dữ liệu vào CSV: x={x}, y={y}, timestamp={timestamp}')
        except Exception as e:
            self.get_logger().error(f'Lỗi khi ghi dữ liệu vào file CSV: {e}')

    def update_plot(self, frame):
        """Cập nhật biểu đồ với dữ liệu mới"""
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        return self.line,

def main(args=None):
    rclpy.init(args=args)
    node = OdomToCSVWithPlot()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node đã dừng bằng Ctrl+C')

    # Dừng node và hủy rclpy
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
