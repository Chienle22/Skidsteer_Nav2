#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateThroughPoses
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
import csv
import math

class SmoothPathFollower(Node):
    def __init__(self):
        super().__init__('smooth_path_follower')
        self.nav_client = ActionClient(self, NavigateThroughPoses, 'navigate_through_poses')

    def send_entire_path(self, poses_list):
        goal_msg = NavigateThroughPoses.Goal()
        goal_msg.poses = poses_list

        self.get_logger().info('Đang chờ Action Server (NavigateThroughPoses) sẵn sàng...')
        self.nav_client.wait_for_server()
        
        self.get_logger().info(f'Đang gửi quỹ đạo đã lọc thưa gồm {len(poses_list)} điểm cho robot...')
        send_goal_future = self.nav_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)
        
        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Quỹ đạo bị từ chối bởi Nav2!')
            return False

        self.get_logger().info('Quỹ đạo đã được chấp nhận, robot đang tracking liên tục...')
        get_result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, get_result_future)
        
        status = get_result_future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('🎉 Robot đã hoàn thành toàn bộ quỹ đạo mượt mà!')
            return True
        else:
            self.get_logger().warning(f'Hành trình dừng lại, mã trạng thái: {status}')
            return False

def read_and_downsample_poses(file_path, min_distance=0.2):
    """
    Đọc file CSV và lọc thưa các waypoint. 
    min_distance: Khoảng cách tối thiểu giữa 2 waypoint liên tiếp (tính bằng mét).
    Giúp tránh việc Nav2 bị ngập lụt quá nhiều điểm sát nhau gây mất bám sau vài giây.
    """
    raw_poses = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                raw_poses.append((float(row['x']), float(row['y'])))
    except Exception as e:
        print(f'Lỗi đọc file CSV: {e}')
        return []

    if not raw_poses:
        return []

    # Thuật toán lọc thưa (Downsampling)
    filtered_poses = [raw_poses[0]]
    for p in raw_poses[1:]:
        dist = math.hypot(p[0] - filtered_poses[-1][0], p[1] - filtered_poses[-1][1])
        if dist >= min_distance:
            filtered_poses.append(p)
            
    # Luôn đảm bảo điểm cuối cùng được đưa vào
    if raw_poses[-1] not in filtered_poses:
        filtered_poses.append(raw_poses[-1])

    # Chuyển đổi thành PoseStamped kèm góc hướng theta mượt mà
    poses_stamped = []
    for i in range(len(filtered_poses)):
        x, y = filtered_poses[i]
        
        if i < len(filtered_poses) - 1:
            next_x, next_y = filtered_poses[i+1]
            theta = math.atan2(next_y - y, next_x - x)
        else:
            theta = poses_stamped[-1].pose.orientation.z if poses_stamped else 0.0

        qx, qy, qz, qw = euler_to_quaternion(0.0, 0.0, theta)

        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0
        pose.pose.orientation.x = qx
        pose.pose.orientation.y = qy
        pose.pose.orientation.z = qz
        pose.pose.orientation.w = qw
        
        poses_stamped.append(pose)

    return poses_stamped

def euler_to_quaternion(roll, pitch, yaw):
    qx = math.sin(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) - math.cos(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
    qy = math.cos(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2)
    qz = math.cos(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2) - math.sin(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2)
    qw = math.cos(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
    return qx, qy, qz, qw

def main():
    rclpy.init()
    follower = SmoothPathFollower()
    
    # Thay đường dẫn tới file CSV First Path của bạn
    csv_file_path = '/home/chienle/Desktop/nav2_ws/src/scripts/first_path/first_path_3_goals.csv'
    
    # Lọc thưa với khoảng cách tối thiểu giữa các điểm là 0.2 mét (có thể tăng lên 0.3 nếu đường dài)
    poses_list = read_and_downsample_poses(csv_file_path, min_distance=0.2)
    
    if not poses_list:
        follower.get_logger().error('Không có điểm hợp lệ nào được tải!')
        return

    follower.send_entire_path(poses_list)
    
    follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
