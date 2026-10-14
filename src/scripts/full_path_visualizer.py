import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
import matplotlib.pyplot as plt

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
        self.last_end_x = None
        self.last_end_y = None
        self.fig, self.ax = plt.subplots()  # Tạo figure cho real-time update

    def listener_callback(self, msg):
        self.get_logger().info(f"Nhận dữ liệu quỹ đạo mới với {len(msg.poses)} điểm")

        # Trích xuất tọa độ từ quỹ đạo
        x_points = [pose.pose.position.x for pose in msg.poses]
        y_points = [-pose.pose.position.y for pose in msg.poses]  # Đảo ngược trục Y

        # Kiểm tra nếu có sự ngắt quãng, nối điểm cuối của đoạn trước vào
        if self.last_end_x is not None and self.last_end_y is not None:
            self.full_x_path.append(self.last_end_x)
            self.full_y_path.append(self.last_end_y)

        # Lưu toàn bộ quỹ đạo
        self.full_x_path.extend(x_points)
        self.full_y_path.extend(y_points)

        # Cập nhật điểm cuối của quỹ đạo hiện tại
        if x_points and y_points:
            self.last_end_x = x_points[-1]
            self.last_end_y = y_points[-1]

        # Hiển thị biểu đồ real-time
        self.plot_trajectory()

    def plot_trajectory(self):
        """ Cập nhật biểu đồ mỗi khi nhận được dữ liệu mới """
        self.ax.clear()  # Xóa dữ liệu cũ để cập nhật mới
        self.ax.scatter(self.full_y_path, self.full_x_path, color='blue', s=5, label="Real-Time Path")  # Điểm nhỏ hơn

        # Vẽ điểm đầu và điểm cuối
        if self.full_x_path and self.full_y_path:
            self.ax.scatter(self.full_y_path[0], self.full_x_path[0], color='green', s=50, label="Start")
            self.ax.scatter(self.full_y_path[-1], self.full_x_path[-1], color='red', s=50, label="End")

        self.ax.set_xlabel("Y (m) - Nằm ngang")
        self.ax.set_ylabel("X (m) - Dọc")
        self.ax.set_title("Quỹ đạo cập nhật Real-Time từ /plan")
        self.ax.legend()
        self.ax.grid(True)

        # Tự động điều chỉnh phạm vi hiển thị
        self.ax.set_xlim(min(self.full_y_path, default=-10)-1, max(self.full_y_path, default=10)+1)
        self.ax.set_ylim(min(self.full_x_path, default=-10)-1, max(self.full_x_path, default=10)+1)

        plt.pause(0.1)  # Cập nhật biểu đồ mà không bị treo chương trình

def main(args=None):
    rclpy.init(args=args)
    plan_subscriber = PlanSubscriber()
    rclpy.spin(plan_subscriber)
    plan_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
