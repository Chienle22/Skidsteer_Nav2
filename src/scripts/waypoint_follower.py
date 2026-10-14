#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
import csv
import math
import numpy as np

class WaypointFollower(Node):
    def __init__(self):
        super().__init__('waypoint_follower')
        self.nav_to_pose_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def send_goal(self, pose):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose

        self.nav_to_pose_client.wait_for_server()
        
        send_goal_future = self.nav_to_pose_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)
        
        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal bị từ chối!')
            return False

        get_result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, get_result_future)
        
        status = get_result_future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Goal đã hoàn thành thành công!')
            return True
        else:
            self.get_logger().warning(f'Goal không thành công với status: {status}')
            return False

def read_waypoints_from_csv(file_path):
    """Đọc tọa độ x, y từ file CSV và tự động tính góc theta hướng di chuyển."""
    waypoints = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            
            for i in range(len(rows)):
                x = float(rows[i]['x'])
                y = float(rows[i]['y'])
                
                # Tự động tính góc hướng theta dựa vào điểm kế tiếp
                if i < len(rows) - 1:
                    next_x = float(rows[i+1]['x'])
                    next_y = float(rows[i+1]['y'])
                    theta = math.atan2(next_y - y, next_x - x)
                else:
                    # Giữ nguyên theta của điểm gần cuối cho điểm cuối cùng
                    theta = waypoints[-1]['theta'] if waypoints else 0.0
                
                qx, qy, qz, qw = euler_to_quaternion(0.0, 0.0, theta)
                
                waypoint = {
                    'position': {'x': x, 'y': y, 'z': 0.0},
                    'orientation': {'x': qx, 'y': qy, 'z': qz, 'w': qw},
                    'theta': theta
                }
                waypoints.append(waypoint)
    except Exception as e:
        print(f'Lỗi khi đọc file CSV: {e}')
    return waypoints

def euler_to_quaternion(roll, pitch, yaw):
    qx = math.sin(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) - math.cos(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
    qy = math.cos(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2)
    qz = math.cos(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2) - math.sin(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2)
    qw = math.cos(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
    return qx, qy, qz, qw

def main():
    rclpy.init()
    follower = WaypointFollower()
    
    # === HÃY THAY ĐƯỜNG DẪN ĐÚNG ĐẾN FILE CSV FIRST PATH CỦA BẠN TẠI ĐÂY ===
    csv_file_path = '/home/chienle/Desktop/nav2_ws/src/scripts/rpp_0.5ms/first_path_data_20261002_204616.csv'
    
    waypoints = read_waypoints_from_csv(csv_file_path)
    
    if not waypoints:
        follower.get_logger().error('Không có waypoint nào được đọc từ file CSV!')
        return

    for i, waypoint in enumerate(waypoints):
        follower.get_logger().info(f'Di chuyển đến waypoint {i+1}/{len(waypoints)}')
        
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = follower.get_clock().now().to_msg()
        pose.pose.position.x = waypoint['position']['x']
        pose.pose.position.y = waypoint['position']['y']
        pose.pose.position.z = waypoint['position']['z']
        pose.pose.orientation.x = waypoint['orientation']['x']
        pose.pose.orientation.y = waypoint['orientation']['y']
        pose.pose.orientation.z = waypoint['orientation']['z']
        pose.pose.orientation.w = waypoint['orientation']['w']
        
        success = follower.send_goal(pose)
        
        if not success:
            follower.get_logger().error(f'Không thể đến waypoint {i+1}')
            break
    
    follower.get_logger().info('Hoàn thành tất cả các waypoint')
    follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
