import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseWithCovarianceStamped
import matplotlib.pyplot as plt
import csv
import signal
import sys
import datetime
from threading import Lock

class FirstPathPlanner(Node):
    def __init__(self):
        super().__init__('first_path_planner')

        self.subscription = self.create_subscription(Path, '/plan', self.listener_callback, 10)
        self.pose_subscription = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)

        self.total_x_path = []
        self.total_y_path = []
        self.timestamps = []

        self.real_x_path = []
        self.real_y_path = []

        self.goal_waypoints = []  # Lưu các goal

        self.current_segment_x = []
        self.current_segment_y = []

        self.current_segment_id = 0
        self.segment_first_plan_received = False
        self.lock = Lock()

        self.fig, self.ax = plt.subplots()
        self.setup_plot()

        # Ghi log ra file CSV
        timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.csv_filename = f'first_path_plan_{timestamp_str}.csv'
        self.csv_file = open(self.csv_filename, 'w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['X (m)', 'Y (m)', 'Timestamp', 'Actual X (m)', 'Actual Y (m)'])

        signal.signal(signal.SIGINT, self.handle_shutdown)

    def setup_plot(self):
        self.ax.set_xlabel("Y (m)")
        self.ax.set_ylabel("X (m)")
        self.ax.set_title("First Path Plan & Actual Path")
        self.ax.grid(True)

    def listener_callback(self, msg):
        with self.lock:
            if self.segment_first_plan_received:
                return

            self.get_logger().info(f"Nhận first path mới với {len(msg.poses)} điểm (Segment {self.current_segment_id})")

            self.current_segment_x.clear()
            self.current_segment_y.clear()
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for pose in msg.poses:
                self.current_segment_x.append(pose.pose.position.x)
                self.current_segment_y.append(-pose.pose.position.y)  # Flip Y để giống RViz
                self.timestamps.append(current_time)

            self.total_x_path.extend(self.current_segment_x)
            self.total_y_path.extend(self.current_segment_y)

            # Ghi log path mới vào CSV
            for x, y in zip(self.current_segment_x, self.current_segment_y):
                self.csv_writer.writerow([x, y, current_time, "", ""])

            if len(self.current_segment_x) > 0:
                goal_x = self.current_segment_x[-1]
                goal_y = self.current_segment_y[-1]
                self.goal_waypoints.append((goal_x, goal_y))

            self.segment_first_plan_received = True
            self.plot_total_path()

    def pose_callback(self, msg):
        self.record_real_pose(msg.pose.pose)

    def record_real_pose(self, pose):
        with self.lock:
            x = pose.position.x
            y = -pose.position.y  # Flip Y để khớp với plan

            self.real_x_path.append(x)
            self.real_y_path.append(y)

            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Ghi log vị trí thực tế vào CSV
            self.csv_writer.writerow(["", "", current_time, x, y])

            self.plot_total_path()

    def plot_total_path(self):
        self.ax.clear()
        self.setup_plot()

        if self.total_x_path and self.total_y_path:
            self.ax.plot(self.total_y_path, self.total_x_path, color='blue', linewidth=2, label='First Path Plan')

        if self.real_x_path and self.real_y_path:
            self.ax.plot(self.real_y_path, self.real_x_path, color='red', linewidth=2, label='Actual Path (AMCL)')

        if self.total_x_path and self.total_y_path:
            self.ax.scatter(self.total_y_path[0], self.total_x_path[0], color='green', s=80, label='Start')
            self.ax.scatter(self.total_y_path[-1], self.total_x_path[-1], color='red', s=80, label='Current Goal')

        for idx, (gx, gy) in enumerate(self.goal_waypoints):
            self.ax.scatter(gy, gx, color='purple', s=100, label=f'Goal {idx+1}' if idx == 0 else None)

        self.ax.legend()
        self.ax.grid(True)

        all_y = self.total_y_path + self.real_y_path
        all_x = self.total_x_path + self.real_x_path

        self.ax.set_xlim(min(all_y) - 1, max(all_y) + 1)
        self.ax.set_ylim(min(all_x) - 1, max(all_x) + 1)

        plt.pause(0.1)

    def move_to_next_point(self):
        self.get_logger().info(f"Đã tới Goal {len(self.goal_waypoints)}, chuẩn bị nhận kế hoạch mới (segment {self.current_segment_id + 1})")

        with self.lock:
            self.current_segment_x.clear()
            self.current_segment_y.clear()
            self.current_segment_id += 1
            self.segment_first_plan_received = False

    def save_results(self):
        png_filename = self.csv_filename.replace('.csv', '.png')
        plt.savefig(png_filename)
        self.get_logger().info(f"Đã lưu {self.csv_filename} và {png_filename}")

        self.csv_file.close()

    def handle_shutdown(self, signum, frame):
        self.get_logger().info("Nhận Ctrl+C, lưu kết quả và thoát...")
        self.save_results()
        rclpy.shutdown()
        sys.exit(0)

def main(args=None):
    rclpy.init(args=args)
    node = FirstPathPlanner()

    def simulate_robot_waypoints():
        import time
        for _ in range(4):
            time.sleep(10)
            node.move_to_next_point()

    import threading
    threading.Thread(target=simulate_robot_waypoints, daemon=True).start()

    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.1)
    except KeyboardInterrupt:
        node.handle_shutdown(signal.SIGINT, None)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
