# # import rclpy
# # from rclpy.node import Node
# # from tf2_ros import Buffer, TransformListener
# # from geometry_msgs.msg import Twist
# # import math
# # import csv
# # import time
# # from datetime import datetime
# # import os

# # class DistanceCalculatorTF(Node):
# #     def __init__(self):
# #         super().__init__('distance_calculator_tf')

# #         self.tf_buffer = Buffer()
# #         self.tf_listener = TransformListener(self.tf_buffer, self)

# #         self.min_movement_threshold = 0.01  # m
# #         self.max_idle_time = 3.0  # seconds

# #         self.prev_x = None
# #         self.prev_y = None
# #         self.prev_time = None

# #         self.total_distance = 0.0
# #         self.measuring = False
# #         self.last_movement_time = None
# #         self.start_real_time = None

# #         # Vận tốc từ cmd_vel
# #         self.current_linear_vel = 0.0

# #         # Lắng nghe /cmd_vel
# #         self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

# #         # Tạo đường dẫn log
# #         log_dir = '/home/chienle/nav2_ws_250606/src/scripts/robot_distance'
# #         os.makedirs(log_dir, exist_ok=True)
# #         timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
# #         filename = f'robot_distance_{timestamp}.csv'
# #         self.csv_path = os.path.join(log_dir, filename)

# #         self.csv_file = open(self.csv_path, mode='w', newline='')
# #         self.csv_writer = csv.writer(self.csv_file)
# #         self.csv_writer.writerow([
# #             'ROS Time (s)', 'Real Time', 'X (m)', 'Y (m)',
# #             'Distance (m)', 'Linear Velocity (m/s)', 'Total Distance (m)'
# #         ])

# #         self.get_logger().info(f'📁 Đang ghi log vào: {self.csv_path}')
# #         self.timer = self.create_timer(0.1, self.timer_callback)

# #     def cmd_vel_callback(self, msg: Twist):
# #         self.current_linear_vel = msg.linear.x  # Cập nhật vận tốc hiện tại

# #     def timer_callback(self):
# #         try:
# #             now = rclpy.time.Time()
# #             trans = self.tf_buffer.lookup_transform('map', 'base_link', now)

# #             x = trans.transform.translation.x
# #             y = trans.transform.translation.y
# #             ros_time = trans.header.stamp.sec + trans.header.stamp.nanosec * 1e-9
# #             real_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# #             distance = 0.0

# #             if self.prev_x is not None and self.prev_y is not None:
# #                 dx = x - self.prev_x
# #                 dy = y - self.prev_y
# #                 distance = math.sqrt(dx*dx + dy*dy)

# #                 if distance > self.min_movement_threshold:
# #                     if not self.measuring:
# #                         self.get_logger().info('📍 Robot bắt đầu di chuyển.')
# #                         self.measuring = True
# #                         self.total_distance = 0.0
# #                         self.start_real_time = time.time()
# #                         self.csv_writer.writerow(['--- Start Moving ---'])

# #                     self.total_distance += distance
# #                     self.last_movement_time = time.time()

# #                 elif self.measuring:
# #                     if (time.time() - self.last_movement_time) > self.max_idle_time:
# #                         total_time = self.last_movement_time - self.start_real_time
# #                         self.get_logger().info('✅ Robot đã dừng.')
# #                         self.get_logger().info(f'📏 Tổng quãng đường: {self.total_distance:.3f} m')
# #                         self.get_logger().info(f'⏱️ Tổng thời gian di chuyển: {total_time:.2f} giây')

# #                         self.csv_writer.writerow(['--- Robot Stopped ---'])
# #                         self.csv_writer.writerow(['Total Distance', '', '', '', '', '', f'{self.total_distance:.4f}'])
# #                         self.csv_writer.writerow(['Total Time (s)', '', '', '', '', '', f'{total_time:.2f}'])
# #                         self.measuring = False

# #             self.prev_x = x
# #             self.prev_y = y

# #             if self.measuring:
# #                 self.csv_writer.writerow([
# #                     f'{ros_time:.2f}', real_time_str, f'{x:.3f}', f'{y:.3f}',
# #                     f'{distance:.4f}', f'{self.current_linear_vel:.4f}', f'{self.total_distance:.4f}'
# #                 ])

# #         except Exception as e:
# #             self.get_logger().warn(f'Không thể lấy transform: {e}')

# #     def destroy_node(self):
# #         self.csv_file.close()
# #         self.get_logger().info(f'📝 Đã lưu file log tại: {self.csv_path}')
# #         super().destroy_node()

# # def main(args=None):
# #     rclpy.init(args=args)
# #     node = DistanceCalculatorTF()
# #     try:
# #         rclpy.spin(node)
# #     except KeyboardInterrupt:
# #         node.get_logger().info('⛔ Đã dừng bằng tay.')
# #     finally:
# #         node.destroy_node()
# #         rclpy.shutdown()

# # if __name__ == '__main__':
# #     main()

# import rclpy
# from rclpy.node import Node
# from tf2_ros import Buffer, TransformListener
# from geometry_msgs.msg import Twist
# import math
# import csv
# import time
# from datetime import datetime
# import os
# from tf_transformations import euler_from_quaternion  # ✅ Thêm dòng này để chuyển quaternion → yaw

# class DistanceCalculatorTF(Node):
#     def __init__(self):
#         super().__init__('distance_calculator_tf')

#         self.tf_buffer = Buffer()
#         self.tf_listener = TransformListener(self.tf_buffer, self)

#         self.min_movement_threshold = 0.01  # m
#         self.max_idle_time = 3.0  # seconds

#         self.prev_x = None
#         self.prev_y = None
#         self.prev_time = None

#         self.total_distance = 0.0
#         self.measuring = False
#         self.last_movement_time = None
#         self.start_real_time = None

#         # Vận tốc từ cmd_vel
#         self.current_linear_vel = 0.0

#         # Lắng nghe /cmd_vel
#         self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

#         # Tạo đường dẫn log
#         log_dir = '/home/chienle/nav2_ws_250606/src/scripts/robot_distance'
#         os.makedirs(log_dir, exist_ok=True)
#         timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#         filename = f'robot_distance_{timestamp}.csv'
#         self.csv_path = os.path.join(log_dir, filename)

#         self.csv_file = open(self.csv_path, mode='w', newline='')
#         self.csv_writer = csv.writer(self.csv_file)
#         self.csv_writer.writerow([
#             'ROS Time (s)', 'Real Time', 'X (m)', 'Y (m)', 'Yaw (deg)',
#             'Distance (m)', 'Linear Velocity (m/s)', 'Total Distance (m)'
#         ])

#         self.get_logger().info(f'📁 Đang ghi log vào: {self.csv_path}')
#         self.timer = self.create_timer(0.1, self.timer_callback)

#     def cmd_vel_callback(self, msg: Twist):
#         self.current_linear_vel = msg.linear.x  # Cập nhật vận tốc hiện tại

#     def timer_callback(self):
#         try:
#             now = rclpy.time.Time()
#             trans = self.tf_buffer.lookup_transform('map', 'base_link', now)

#             x = trans.transform.translation.x
#             y = trans.transform.translation.y
#             ros_time = trans.header.stamp.sec + trans.header.stamp.nanosec * 1e-9
#             real_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#             # ✅ Tính yaw từ quaternion
#             q = trans.transform.rotation
#             quaternion = (q.x, q.y, q.z, q.w)
#             _, _, yaw = euler_from_quaternion(quaternion)
#             yaw_deg = math.degrees(yaw)

#             distance = 0.0

#             if self.prev_x is not None and self.prev_y is not None:
#                 dx = x - self.prev_x
#                 dy = y - self.prev_y
#                 distance = math.sqrt(dx * dx + dy * dy)

#                 if distance > self.min_movement_threshold:
#                     if not self.measuring:
#                         self.get_logger().info('📍 Robot bắt đầu di chuyển.')
#                         self.measuring = True
#                         self.total_distance = 0.0
#                         self.start_real_time = time.time()
#                         self.csv_writer.writerow(['--- Start Moving ---'])

#                     self.total_distance += distance
#                     self.last_movement_time = time.time()

#                 elif self.measuring:
#                     if (time.time() - self.last_movement_time) > self.max_idle_time:
#                         total_time = self.last_movement_time - self.start_real_time
#                         self.get_logger().info('✅ Robot đã dừng.')
#                         self.get_logger().info(f'📏 Tổng quãng đường: {self.total_distance:.3f} m')
#                         self.get_logger().info(f'⏱️ Tổng thời gian di chuyển: {total_time:.2f} giây')

#                         self.csv_writer.writerow(['--- Robot Stopped ---'])
#                         self.csv_writer.writerow(['Total Distance', '', '', '', '', '', '', f'{self.total_distance:.4f}'])
#                         self.csv_writer.writerow(['Total Time (s)', '', '', '', '', '', '', f'{total_time:.2f}'])
#                         self.measuring = False

#             self.prev_x = x
#             self.prev_y = y

#             if self.measuring:
#                 self.csv_writer.writerow([
#                     f'{ros_time:.2f}', real_time_str, f'{x:.3f}', f'{y:.3f}', f'{yaw_deg:.2f}',
#                     f'{distance:.4f}', f'{self.current_linear_vel:.4f}', f'{self.total_distance:.4f}'
#                 ])

#         except Exception as e:
#             self.get_logger().warn(f'Không thể lấy transform: {e}')

#     def destroy_node(self):
#         self.csv_file.close()
#         self.get_logger().info(f'📝 Đã lưu file log tại: {self.csv_path}')
#         super().destroy_node()

# def main(args=None):
#     rclpy.init(args=args)
#     node = DistanceCalculatorTF()
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         node.get_logger().info('⛔ Đã dừng bằng tay.')
#     finally:
#         node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()


import rclpy
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener
from geometry_msgs.msg import Twist
import math
import csv
import time
from datetime import datetime
import os
from tf_transformations import euler_from_quaternion  # ✅ Chuyển quaternion → yaw

class DistanceCalculatorTF(Node):
    def __init__(self):
        super().__init__('distance_calculator_tf')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.min_movement_threshold = 0.01  # m
        self.max_idle_time = 3.0  # seconds

        self.prev_x = None
        self.prev_y = None
        self.prev_time = None

        self.total_distance = 0.0
        self.measuring = False
        self.last_movement_time = None
        self.start_real_time = None

        # Vận tốc từ cmd_vel
        self.current_linear_vel = 0.0

        # Lắng nghe /cmd_vel
        self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

        # Tạo đường dẫn log
        log_dir = '/home/chienle/nav2_ws_250606/src/scripts/robot_distance'
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'robot_distance_{timestamp}.csv'
        self.csv_path = os.path.join(log_dir, filename)

        self.csv_file = open(self.csv_path, mode='w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow([
            'ROS Time (s)', 'Real Time', 'Elapsed Time (s)',
            'x', 'y', 'Yaw (deg)',
            'Distance (m)', 'Linear Velocity (m/s)', 'Total Distance (m)'
        ])

        self.get_logger().info(f'📁 Đang ghi log vào: {self.csv_path}')
        self.timer = self.create_timer(0.1, self.timer_callback)

    def cmd_vel_callback(self, msg: Twist):
        self.current_linear_vel = msg.linear.x  # Cập nhật vận tốc hiện tại

    def timer_callback(self):
        try:
            now = rclpy.time.Time()
            trans = self.tf_buffer.lookup_transform('map', 'base_link', now)

            x = trans.transform.translation.x
            y = trans.transform.translation.y
            ros_time = trans.header.stamp.sec + trans.header.stamp.nanosec * 1e-9
            real_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # ✅ Tính yaw từ quaternion
            q = trans.transform.rotation
            quaternion = (q.x, q.y, q.z, q.w)
            _, _, yaw = euler_from_quaternion(quaternion)
            yaw_deg = math.degrees(yaw)

            distance = 0.0

            if self.prev_x is not None and self.prev_y is not None:
                dx = x - self.prev_x
                dy = y - self.prev_y
                distance = math.sqrt(dx * dx + dy * dy)

                if distance > self.min_movement_threshold:
                    if not self.measuring:
                        self.get_logger().info('📍 Robot bắt đầu di chuyển.')
                        self.measuring = True
                        self.total_distance = 0.0
                        self.start_real_time = time.time()
                        self.csv_writer.writerow(['--- Start Moving ---'])

                    self.total_distance += distance
                    self.last_movement_time = time.time()

                elif self.measuring:
                    if (time.time() - self.last_movement_time) > self.max_idle_time:
                        total_time = self.last_movement_time - self.start_real_time
                        self.get_logger().info('✅ Robot đã dừng.')
                        self.get_logger().info(f'📏 Tổng quãng đường: {self.total_distance:.3f} m')
                        self.get_logger().info(f'⏱️ Tổng thời gian di chuyển: {total_time:.2f} giây')

                        self.csv_writer.writerow(['--- Robot Stopped ---'])
                        self.csv_writer.writerow(['Total Distance', '', '', '', '', '', '', '', f'{self.total_distance:.4f}'])
                        self.csv_writer.writerow(['Total Time (s)', '', '', '', '', '', '', '', f'{total_time:.2f}'])
                        self.measuring = False

            self.prev_x = x
            self.prev_y = y

            if self.measuring:
                elapsed_time = time.time() - self.start_real_time if self.start_real_time else 0.0
                self.csv_writer.writerow([
                    f'{ros_time:.2f}', real_time_str, f'{elapsed_time:.2f}',
                    f'{x:.3f}', f'{y:.3f}', f'{yaw_deg:.2f}',
                    f'{distance:.4f}', f'{self.current_linear_vel:.4f}', f'{self.total_distance:.4f}'
                ])

        except Exception as e:
            self.get_logger().warn(f'Không thể lấy transform: {e}')

    def destroy_node(self):
        self.csv_file.close()
        self.get_logger().info(f'📝 Đã lưu file log tại: {self.csv_path}')
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = DistanceCalculatorTF()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('⛔ Đã dừng bằng tay.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
