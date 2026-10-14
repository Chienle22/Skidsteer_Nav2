# #!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import PoseStamped
# from nav2_msgs.action import NavigateThroughPoses
# from rclpy.action import ActionClient
# from action_msgs.msg import GoalStatus

# class NavThroughPoses(Node):
#     def __init__(self):
#         super().__init__('nav_through_poses')
#         self.nav_to_poses_client = ActionClient(self, NavigateThroughPoses, 'navigate_through_poses')

#         # Định nghĩa các poses mà robot sẽ di chuyển qua
#         self.waypoints = [
#         # {'position': {'x': -4.0, 'y': -6.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
#         {'position': {'x': 22.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
#         {'position': {'x': 22.0, 'y': 12.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': 1.0}},
#         {'position': {'x': -4.0, 'y': 12.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 1.0, 'w': 1.0}},
#         {'position': {'x': -4.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
#         ]

#     def send_goals(self, goal_poses):
#         goal_msg = NavigateThroughPoses.Goal()
#         goal_msg.poses = goal_poses

#         # Đợi server sẵn sàng
#         self.nav_to_poses_client.wait_for_server()
        
#         # Gửi goal và đợi phản hồi
#         send_goal_future = self.nav_to_poses_client.send_goal_async(goal_msg)
#         rclpy.spin_until_future_complete(self, send_goal_future)
        
#         goal_handle = send_goal_future.result()
#         if not goal_handle.accepted:
#             self.get_logger().error('Goal bị từ chối!')
#             return False

#         # Đợi kết quả
#         get_result_future = goal_handle.get_result_async()
#         rclpy.spin_until_future_complete(self, get_result_future)
        
#         status = get_result_future.result().status
#         if status == GoalStatus.STATUS_SUCCEEDED:
#             self.get_logger().info('Goal đã hoàn thành thành công!')
#             return True
#         else:
#             self.get_logger().warning(f'Goal không thành công với status: {status}')
#             return False

#     def navigate_through_poses(self):
#         """Điều khiển robot di chuyển qua các poses liên tục"""
        
#         # Tạo danh sách các pose
#         goal_poses = []
#         for waypoint in self.waypoints:
#             pose = PoseStamped()
#             pose.header.frame_id = 'map'
#             pose.header.stamp = self.get_clock().now().to_msg()
#             pose.pose.position.x = waypoint['position']['x']
#             pose.pose.position.y = waypoint['position']['y']
#             pose.pose.position.z = waypoint['position']['z']
#             pose.pose.orientation.x = waypoint['orientation']['x']
#             pose.pose.orientation.y = waypoint['orientation']['y']
#             pose.pose.orientation.z = waypoint['orientation']['z']
#             pose.pose.orientation.w = waypoint['orientation']['w']
#             goal_poses.append(pose)

#         # Gửi tất cả các goal poses liên tiếp
#         self.get_logger().info('Bắt đầu di chuyển qua các poses.')
#         self.send_goals(goal_poses)  # Gửi tất cả các goal poses

#         # Chờ cho đến khi quá trình di chuyển hoàn tất
#         while not self.nav_to_poses_client.is_nav_complete():
#             rclpy.spin_once(self)

#         self.get_logger().info('Hoàn thành tất cả các poses.')

# def main():
#     rclpy.init()
    
#     nav_through_poses = NavThroughPoses()

#     # Chạy điều khiển robot qua các poses liên tục
#     nav_through_poses.navigate_through_poses()

#     nav_through_poses.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateThroughPoses
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus


class NavThroughPoses(Node):
    def __init__(self):
        super().__init__('nav_through_poses')
        self.nav_to_poses_client = ActionClient(self, NavigateThroughPoses, 'navigate_through_poses')

        # Định nghĩa các poses mà robot sẽ di chuyển qua
        self.waypoints = [
# Gia tri z & w:  goc 0 (0.0,1.0); 90 (0.7071,0.7071); 180 (1.0,0.0); 270 (0.7071,-0.7071)
            # # {'position': {'x': -4.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
            # {'position': {'x': 22.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
            # {'position': {'x': 22.0, 'y': 12.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': 1.0}},
            # {'position': {'x': -4.0, 'y': 12.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 1.0, 'w': 1.0}},
            # {'position': {'x': -4.0, 'y': -1.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},

            # {'position': {'x': -3.75, 'y': -6.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
            # {'position': {'x': 22.35, 'y': -5.4, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
            # {'position': {'x': 22.35, 'y': 6.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': 1.0}},
            # {'position': {'x': -4.0, 'y': 5.75, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 1.0, 'w': 1.0}},
            # {'position': {'x': -3.75, 'y': -5.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},


            # {'position': {'x': -35.5, 'y': 15.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 1.0, 'w': 0.0}},
            # {'position': {'x': -70.5, 'y': 15.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 1.0, 'w': 0.0}},
            # {'position': {'x': -70.5, 'y': 50.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7071, 'w': 0.7071}},
            

        # {'position': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7071, 'w': 0.7071}},
        # {'position': {'x': 0.0, 'y': 37.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7071, 'w': 0.7071}},
        {'position': {'x': -35.0, 'y': 37.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},


        ]

    def send_goals(self, goal_poses):
        goal_msg = NavigateThroughPoses.Goal()
        goal_msg.poses = goal_poses

        # Đợi server sẵn sàng
        self.nav_to_poses_client.wait_for_server()

        # Gửi goal và đợi phản hồi
        send_goal_future = self.nav_to_poses_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal bị từ chối!')
            return False

        # Đợi kết quả
        get_result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, get_result_future)

        status = get_result_future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Goal đã hoàn thành thành công!')
            return True
        else:
            self.get_logger().warning(f'Goal không thành công với status: {status}')
            return False

    def navigate_through_poses(self):
        """Điều khiển robot di chuyển qua các poses liên tục"""

        # Tạo danh sách các pose
        goal_poses = []
        for waypoint in self.waypoints:
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.pose.position.x = waypoint['position']['x']
            pose.pose.position.y = waypoint['position']['y']
            pose.pose.position.z = waypoint['position']['z']
            pose.pose.orientation.x = waypoint['orientation']['x']
            pose.pose.orientation.y = waypoint['orientation']['y']
            pose.pose.orientation.z = waypoint['orientation']['z']
            pose.pose.orientation.w = waypoint['orientation']['w']
            goal_poses.append(pose)

        # Gửi tất cả các goal poses một lần
        self.get_logger().info('Bắt đầu di chuyển qua các poses.')
        success = self.send_goals(goal_poses)

        if success:
            self.get_logger().info('Hoàn thành tất cả các poses.')
        else:
            self.get_logger().warn('Không hoàn thành được tất cả các poses.')


def main():
    rclpy.init()
    nav_through_poses = NavThroughPoses()

    nav_through_poses.navigate_through_poses()

    nav_through_poses.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
