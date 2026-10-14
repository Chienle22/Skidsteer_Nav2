import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseWithCovarianceStamped
import matplotlib.pyplot as plt
import csv
import threading
import time
import signal
import sys

class PlanTracker(Node):
    def __init__(self):
        super().__init__('plan_tracker')

        self.plan_sub = self.create_subscription(Path, '/plan', self.plan_callback, 10)
        self.pose_sub = self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)

        self.full_x_path = []
        self.full_y_path = []
        self.actual_x = []
        self.actual_y = []
        self.goal_waypoints = []

        self.csv_file = open('path_vs_actual.csv', 'w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(["timestamp", "path_x", "path_y", "actual_x", "actual_y"])

        self.fig, self.ax = plt.subplots(figsize=(8, 6))

        self.last_actual_x = None
        self.last_actual_y = None

        self.lock = threading.Lock()

    def plan_callback(self, msg):
        x_points = [pose.pose.position.x for pose in msg.poses]
        y_points = [-pose.pose.position.y for pose in msg.poses]

        with self.lock:
            self.full_x_path.extend(x_points)
            self.full_y_path.extend(y_points)

            if x_points and y_points:
                self.goal_waypoints.append((x_points[-1], y_points[-1]))

        timestamp = self.get_clock().now().seconds_nanoseconds()[0] + \
                    self.get_clock().now().seconds_nanoseconds()[1] * 1e-9

        for x, y in zip(x_points, y_points):
            actual_x = self.last_actual_x if self.last_actual_x is not None else ""
            actual_y = self.last_actual_y if self.last_actual_y is not None else ""
            self.csv_writer.writerow([timestamp, x, y, actual_x, actual_y])

    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = -msg.pose.pose.position.y

        with self.lock:
            self.actual_x.append(x)
            self.actual_y.append(y)

        self.last_actual_x = x
        self.last_actual_y = y

        timestamp = self.get_clock().now().seconds_nanoseconds()[0] + \
                    self.get_clock().now().seconds_nanoseconds()[1] * 1e-9

        self.csv_writer.writerow([timestamp, "", "", x, y])

    def update_plot(self):
        with self.lock:
            self.ax.clear()

            # Vẽ đường path tối ưu (first path)
            if self.full_x_path and self.full_y_path:
                self.ax.plot(self.full_y_path, self.full_x_path, color='blue', linewidth=2, label=" Path Plan")

            # Vẽ đường thực tế AMCL
            if self.actual_x and self.actual_y:
                self.ax.plot(self.actual_y, self.actual_x, color='red', linewidth=2, label="Actual Path (AMCL)")

            # Điểm bắt đầu
            if self.full_x_path and self.full_y_path:
                self.ax.scatter(self.full_y_path[0], self.full_x_path[0], color='green', s=100, label="Start")

            # Điểm goal cuối
            if self.goal_waypoints:
                gx, gy = self.goal_waypoints[-1]
                self.ax.scatter(gy, gx, color='red', s=100, label="Current Goal")

            # Vẽ tất cả goal trước đó (chấm tím)
            for i, (gx, gy) in enumerate(self.goal_waypoints[:-1]):
                self.ax.scatter(gy, gx, color='purple', s=80, label="Goal" if i == 0 else None)

            self.ax.set_xlabel("Y (m)")
            self.ax.set_ylabel("X (m)")
            self.ax.set_title("Full Path Plan & Actual Path")
            self.ax.legend()
            self.ax.grid(True)

            all_x = self.full_x_path + self.actual_x
            all_y = self.full_y_path + self.actual_y

            if all_x and all_y:
                self.ax.set_xlim(min(all_y) - 1, max(all_y) + 1)
                self.ax.set_ylim(min(all_x) - 1, max(all_x) + 1)

            plt.draw()

    def save_plot(self):
        self.ax.figure.savefig("trajectory_plot.png")
        print("Saved final trajectory plot to 'trajectory_plot.png'")

    def destroy_node(self):
        self.save_plot()
        self.csv_file.close()
        super().destroy_node()

def run_ros2_node(node):
    rclpy.spin(node)

def handle_sigint(signum, frame, node):
    print("Ctrl+C detected. Saving and shutting down...")
    node.destroy_node()
    rclpy.shutdown()
    sys.exit(0)

def main(args=None):
    rclpy.init(args=args)
    node = PlanTracker()

    ros2_thread = threading.Thread(target=run_ros2_node, args=(node,), daemon=True)
    ros2_thread.start()

    signal.signal(signal.SIGINT, lambda signum, frame: handle_sigint(signum, frame, node))

    plt.ion()
    while rclpy.ok():
        node.update_plot()
        plt.pause(0.1)

    plt.close()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
