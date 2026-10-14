#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import pandas as pd
import os

class FixedPathPublisher(Node):
    def __init__(self):
        super().__init__('fixed_path_publisher')
        
        # Publisher phát quỹ đạo lên topic /plan của Nav2
        self.publisher_ = self.create_publisher(Path, '/plan', 10)
        
        # Tần suất phát lại (ví dụ 5 Hz)
        self.timer = self.create_timer(0.2, self.publish_path)
        
        # Đường dẫn tới file CSV First Path chuẩn của bạn
        self.csv_file_path = '/home/chienle/Desktop/nav2_ws/src/scripts/rpp_0.5ms/first_path_data_20261002_204616.csv'
        
        # Load dữ liệu từ CSV
        self.path_msg = self.load_path_from_csv()
        self.get_logger().info(f"Đã tải thành công quỹ đạo cố định từ CSV với {len(self.path_msg.poses)} điểm.")

    def load_path_from_csv(self):
        path_msg = Path()
        path_msg.header.frame_id = 'map'
        
        if not os.path.exists(self.csv_file_path):
            self.get_logger().error(f"Không tìm thấy file CSV tại: {self.csv_file_path}")
            return path_msg

        df = pd.read_csv(self.csv_file_path)
        
        for _, row in df.iterrows():
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.pose.position.x = float(row['x'])
            pose.pose.position.y = float(row['y'])
            pose.pose.position.z = float(row['z']) if 'z' in df.columns else 0.0
            
            # Nếu file CSV có thông tin orientation, có thể gán thêm ở đây
            pose.pose.orientation.w = 1.0  # Mặc định hướng chuẩn
            
            path_msg.poses.append(pose)
            
        return path_msg

    def publish_path(self):
        if len(self.path_msg.poses) > 0:
            self.path_msg.header.stamp = self.get_clock().now().to_msg()
            self.publisher_.publish(self.path_msg)

def main(args=None):
    rclpy.init(args=args)
    node = FixedPathPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
