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

        # Đường dẫn thư mục để lưu file CSV
        script_path = '/home/chienle/nav2_ws/src/scripts'
        amcl_dir = os.path.join(script_path, 'amcl')  # Thư mục lưu AMCL
        path_dir = os.path.join(script_path, 'path')  # Thư mục lưu Local Plan
        odom_dir = os.path.join(script_path, 'odom')  # Thư mục lưu Odom
        cmd_vel_dir = os.path.join(script_path, 'cmd_vel')  # Thư mục lưu Cmd Vel
        first_path_dir = os.path.join(script_path, 'first_path')  # Thư mục lưu First Path
        transformed_plan_dir = os.path.join(script_path, 'transformed_global_plan')  # Thư mục lưu Transformed Global Plan

        # Tạo thư mục nếu chưa tồn tại
        os.makedirs(amcl_dir, exist_ok=True)
        os.makedirs(path_dir, exist_ok=True)
        os.makedirs(odom_dir, exist_ok=True)
        os.makedirs(cmd_vel_dir, exist_ok=True)
        os.makedirs(first_path_dir, exist_ok=True)
        os.makedirs(transformed_plan_dir, exist_ok=True)

        # Lấy thời gian hiện tại để tạo tên file
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        # Đặt tên file cho AMCL, Local Plan, Odom, Cmd Vel, First Path và Transformed Global Plan
        self.amcl_filename = os.path.join(amcl_dir, f'amcl_data_{timestamp}.csv')
        self.path_filename = os.path.join(path_dir, f'local_plan_data_{timestamp}.csv')
        self.odom_filename = os.path.join(odom_dir, f'odom_data_{timestamp}.csv')
        self.cmd_vel_filename = os.path.join(cmd_vel_dir, f'cmd_vel_data_{timestamp}.csv')
        self.first_path_filename = os.path.join(first_path_dir, f'first_path_data_{timestamp}.csv')
        self.transformed_plan_filename = os.path.join(transformed_plan_dir, f'transformed_plan_data_{timestamp}.csv')

        # Mở file CSV để lưu dữ liệu AMCL, path, odom, cmd_vel, first path và transformed global plan
        self.amcl_file = open(self.amcl_filename, mode='w', newline='')
        self.path_file = open(self.path_filename, mode='w', newline='')
        self.odom_file = open(self.odom_filename, mode='w', newline='')
        self.cmd_vel_file = open(self.cmd_vel_filename, mode='w', newline='')
        self.first_path_file = open(self.first_path_filename, mode='w', newline='')
        self.transformed_plan_file = open(self.transformed_plan_filename, mode='w', newline='')

        self.amcl_writer = csv.writer(self.amcl_file)
        self.path_writer = csv.writer(self.path_file)
        self.odom_writer = csv.writer(self.odom_file)
        self.cmd_vel_writer = csv.writer(self.cmd_vel_file)
        self.first_path_writer = csv.writer(self.first_path_file)
        self.transformed_plan_writer = csv.writer(self.transformed_plan_file)

        # Ghi tiêu đề cho các file CSV
        self.amcl_writer.writerow(['timestamp', 'x', 'y', 'z', 'orientation_x', 'orientation_y', 'orientation_z', 'orientation_w'])
        self.path_writer.writerow(['timestamp', 'x', 'y', 'z'])
        self.odom_writer.writerow(['timestamp', 'x', 'y', 'z', 'orientation_x', 'orientation_y', 'orientation_z', 'orientation_w'])
        self.cmd_vel_writer.writerow(['timestamp', 'linear_x', 'linear_y', 'angular_z'])
        self.first_path_writer.writerow(['timestamp', 'x', 'y', 'z'])
        self.transformed_plan_writer.writerow(['timestamp', 'x', 'y', 'z'])

        # Subcribe vào các topic /amcl_pose, /path, /odom, /cmd_vel, /plan, /transformed_global_plan
        self.amcl_subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            '/amcl_pose',
            self.amcl_listener_callback,
            10)

        self.path_subscription = self.create_subscription(
            Path,
            '/plan',
            self.path_listener_callback,
            10)

        self.odom_subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_listener_callback,
            10)

        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_listener_callback,
            10)

        self.first_path_subscription = self.create_subscription(
            Path,
            '/plan',  # Quỹ đạo đầu tiên
            self.first_path_listener_callback,
            10)

        self.transformed_plan_subscription = self.create_subscription(
            Path,
            '/transformed_global_plan',  # Quỹ đạo đã chuyển đổi
            self.transformed_plan_listener_callback,
            10)

        # Flag để chỉ lấy dữ liệu quỹ đạo đầu tiên
        self.received_first_path = False
        self.received_transformed_plan = False

    def amcl_listener_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec  # Thời gian hiện tại
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        orientation_x = msg.pose.pose.orientation.x
        orientation_y = msg.pose.pose.orientation.y
        orientation_z = msg.pose.pose.orientation.z
        orientation_w = msg.pose.pose.orientation.w

        # Ghi dữ liệu vào file CSV AMCL
        self.amcl_writer.writerow([timestamp, x, y, z, orientation_x, orientation_y, orientation_z, orientation_w])
        self.get_logger().info(f"AMCL Data saved: {timestamp}, {x}, {y}, {z}, {orientation_x}, {orientation_y}, {orientation_z}, {orientation_w}")

    def path_listener_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec  # Thời gian hiện tại
        for pose in msg.poses:
            # Lấy dữ liệu từ thông điệp Path
            trajectory_x = pose.pose.position.x
            trajectory_y = pose.pose.position.y
            trajectory_z = pose.pose.position.z

            # Ghi dữ liệu vào file CSV Path
            self.path_writer.writerow([timestamp, trajectory_x, trajectory_y, trajectory_z])
            self.get_logger().info(f"Path Data saved: {timestamp}, {trajectory_x}, {trajectory_y}, {trajectory_z}")

    def odom_listener_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec  # Thời gian hiện tại
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        orientation_x = msg.pose.pose.orientation.x
        orientation_y = msg.pose.pose.orientation.y
        orientation_z = msg.pose.pose.orientation.z
        orientation_w = msg.pose.pose.orientation.w

        # Ghi dữ liệu vào file CSV Odom
        self.odom_writer.writerow([timestamp, x, y, z, orientation_x, orientation_y, orientation_z, orientation_w])
        self.get_logger().info(f"Odom Data saved: {timestamp}, {x}, {y}, {z}, {orientation_x}, {orientation_y}, {orientation_z}, {orientation_w}")

    def cmd_vel_listener_callback(self, msg):
        timestamp = self.get_clock().now().to_msg().sec  # Thời gian hiện tại
        linear_x = msg.linear.x
        linear_y = msg.linear.y
        angular_z = msg.angular.z

        # Ghi dữ liệu vào file CSV Cmd Vel
        self.cmd_vel_writer.writerow([timestamp, linear_x, linear_y, angular_z])
        self.get_logger().info(f"Cmd Vel Data saved: {timestamp}, {linear_x}, {linear_y}, {angular_z}")

    def first_path_listener_callback(self, msg):
        if not self.received_first_path:
            timestamp = self.get_clock().now().to_msg().sec  # Thời gian hiện tại
            for pose in msg.poses:
                # Lấy dữ liệu từ thông điệp First Path
                trajectory_x = pose.pose.position.x
                trajectory_y = pose.pose.position.y
                trajectory_z = pose.pose.position.z

                # Ghi dữ liệu vào file CSV First Path
                self.first_path_writer.writerow([timestamp, trajectory_x, trajectory_y, trajectory_z])
                self.get_logger().info(f"First Path Data saved: {timestamp}, {trajectory_x}, {trajectory_y}, {trajectory_z}")

            # Set flag to True to avoid saving the path again
            self.received_first_path = True

    def transformed_plan_listener_callback(self, msg):
        if not self.received_transformed_plan:
            timestamp = self.get_clock().now().to_msg().sec  # Thời gian hiện tại
            for pose in msg.poses:
                # Lấy dữ liệu từ thông điệp Transformed Global Plan
                trajectory_x = pose.pose.position.x
                trajectory_y = pose.pose.position.y
                trajectory_z = pose.pose.position.z

                # Ghi dữ liệu vào file CSV Transformed Global Plan
                self.transformed_plan_writer.writerow([timestamp, trajectory_x, trajectory_y, trajectory_z])
                self.get_logger().info(f"Transformed Global Plan Data saved: {timestamp}, {trajectory_x}, {trajectory_y}, {trajectory_z}")

            # Set flag to True to avoid saving the path again
            self.received_transformed_plan = True

    def destroy_node(self):
        # Đóng các file CSV khi node bị hủy
        self.amcl_file.close()
        self.path_file.close()
        self.odom_file.close()
        self.cmd_vel_file.close()
        self.first_path_file.close()
        self.transformed_plan_file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    data_saver = DataSaver()

    try:
        rclpy.spin(data_saver)
    except KeyboardInterrupt:
        pass

    data_saver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
