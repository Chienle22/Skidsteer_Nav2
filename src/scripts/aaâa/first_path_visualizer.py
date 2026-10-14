import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
import matplotlib.pyplot as plt
import time
import threading

class PlanSubscriber(Node):
    def __init__(self):
        super().__init__('plan_subscriber')
        self.subscription = self.create_subscription(
            Path,
            '/plan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.full_x_path = []
        self.full_y_path = []
        self.last_waypoint_x = None
        self.last_waypoint_y = None
        self.last_update_time = time.time()  # Thời gian nhận dữ liệu gần nhất
        self.timeout_seconds = 5  # Nếu không có dữ liệu mới sau 5s, dừng chương trình

        self.fig, self.ax = plt.subplots()
        self.running = True  # Kiểm soát vòng lặp chính

        # Chạy luồng kiểm tra timeout
        self.timeout_thread = threading.Thread(target=self.check_timeout)
        self.timeout_thread.start()

    def listener_callback(self, msg):
        """ Nhận dữ liệu quỹ đạo và chỉ lưu nếu là waypoint mới """
        self.get_logger().info(f"Nhận quỹ đạo mới với {len(msg.poses)} điểm")

        # Trích xuất tọa độ từ quỹ đạo
        x_points = [pose.pose.position.x for pose in msg.poses]
        y_points = [-pose.pose.position.y for pose in msg.poses]  # Đảo ngược trục Y

        # Nếu waypoint chưa được ghi nhận, lưu lại
        if not self.full_x_path or (x_points and y_points and
                                    (self.last_waypoint_x != x_points[-1] or self.last_waypoint_y != y_points[-1])):
            self.full_x_path.extend(x_points)
            self.full_y_path.extend(y_points)
            self.last_waypoint_x = x_points[-1]
            self.last_waypoint_y = y_points[-1]
            self.last_update_time = time.time()  # Cập nhật thời gian nhận dữ liệu
            self.plot_trajectory()

    def plot_trajectory(self):
        """ Hiển thị biểu đồ real-time """
        self.ax.clear()
        self.ax.scatter(self.full_y_path, self.full_x_path, color='blue', s=5, label="Planned Path")

        # Vẽ điểm đầu và điểm cuối
        if self.full_x_path and self.full_y_path:
            self.ax.scatter(self.full_y_path[0], self.full_x_path[0], color='green', s=50, label="Start")
            self.ax.scatter(self.full_y_path[-1], self.full_x_path[-1], color='red', s=50, label="End")

        self.ax.set_xlabel("Y (m) - Nằm ngang")
        self.ax.set_ylabel("X (m) - Dọc")
        self.ax.set_title("Quỹ đạo ban đầu từ /plan")
        self.ax.legend()
        self.ax.grid(True)

        # Tự động điều chỉnh phạm vi hiển thị
        self.ax.set_xlim(min(self.full_y_path, default=-10) - 1, max(self.full_y_path, default=10) + 1)
        self.ax.set_ylim(min(self.full_x_path, default=-10) - 1, max(self.full_x_path, default=10) + 1)

        plt.pause(0.1)

    def check_timeout(self):
        """ Kiểm tra nếu không có dữ liệu mới trong 5 giây, tự động kết thúc """
        while self.running:
            if time.time() - self.last_update_time > self.timeout_seconds:
                self.get_logger().info("Không có dữ liệu mới trong 5 giây, lưu kết quả và kết thúc.")
                plt.savefig("plan_result.png")  # Lưu kết quả
                plt.show()
                self.running = False
                rclpy.shutdown()
                break
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    plan_subscriber = PlanSubscriber()
    rclpy.spin(plan_subscriber)
    plan_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
