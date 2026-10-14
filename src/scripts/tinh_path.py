import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
import math
import csv
import os
from datetime import datetime

class PathLengthSaver(Node):
    def __init__(self):
        super().__init__('path_length_saver')
        self.subscription = self.create_subscription(
            Path,
            '/plan',  # Hoặc '/global_plan' nếu dùng topic khác
            self.path_callback,
            10)
        self.first_path_received = False

    def path_callback(self, msg):
        if self.first_path_received:
            return

        self.first_path_received = True
        poses = msg.poses
        total_length = 0.0

        # ✅ Tạo tên file có timestamp
        timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f'global_path_{timestamp_str}.csv'
        output_path = os.path.join(os.getcwd(), file_name)

        with open(output_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['index', 'x', 'y', 'distance_from_last_point'])

            for i in range(len(poses)):
                x = poses[i].pose.position.x
                y = poses[i].pose.position.y

                if i == 0:
                    dist = 0.0
                else:
                    x_prev = poses[i-1].pose.position.x
                    y_prev = poses[i-1].pose.position.y
                    dist = math.sqrt((x - x_prev)**2 + (y - y_prev)**2)
                    total_length += dist

                writer.writerow([i, x, y, round(dist, 5)])

        self.get_logger().info(f'✅ Đã lưu path vào: {output_path}')
        self.get_logger().info(f'📏 Chiều dài path: {total_length:.3f} mét')

def main(args=None):
    rclpy.init(args=args)
    node = PathLengthSaver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
