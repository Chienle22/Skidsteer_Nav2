# 
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus

class WaypointFollower(Node):
    def __init__(self):
        super().__init__('waypoint_follower')
        self.nav_to_pose_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def send_goal(self, pose):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose

        # Đợi server sẵn sàng
        self.nav_to_pose_client.wait_for_server()
        
        # Gửi goal và đợi phản hồi
        send_goal_future = self.nav_to_pose_client.send_goal_async(goal_msg)
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

def main():
    rclpy.init()
    
    follower = WaypointFollower()
    
    # Định nghĩa các waypoint
    waypoints = [
        # Ví dụ waypoint - điều chỉnh tọa độ theo map của bạn

        # {'position': {'x': 22.0, 'y': 0.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.5, 'w': 1.0}},

        # {'position': {'x': 22.0, 'y': 12.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.5, 'w': 1.0}},

        # {'position': {'x': -4.0, 'y': 12.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.5, 'w': 1.0}},

        # {'position': {'x': -4.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
        # {'position': {'x': 22.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
        # {'position': {'x': 22.0, 'y': 12.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7, 'w': 1.0}},
        # {'position': {'x': -4.0, 'y': 12.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 1.0, 'w': 1.0}},
        # {'position': {'x': -4.0, 'y': 0.0, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},

        # {'position': {'x': -35.25, 'y': -20.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7071, 'w': 0.7071}},
        {'position': {'x': -35.25, 'y': 15.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
        {'position': {'x': -70.0, 'y': 15.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},

        # {'position': {'x': -35.5, 'y': 15.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 1.0, 'w': 0.0}},

        # {'position': {'x': -70.5, 'y': 15.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 1.0, 'w': 0.0}},
        
        # {'position': {'x': -70.5, 'y': 50.5, 'z': 0.0}, 'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.7071, 'w': 0.7071}},

#2025 06 13
#start
        # {'position': {'x': -1.0, 'y': -6.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
#end1
        # {'position': {'x': 11.5, 'y': -16.0, 'z': 0.0},
        # 'orientation': {'x': 0.0, 'y': 0.0, 'z': -0.7, 'w': 1.0}},
# real start
        # {'position': {'x': 24.0, 'y': 30.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
# # end start
#         {'position': {'x': 1.0, 'y': 70.0, 'z': 0.0},
#          'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},



# point A(34.0;11.0)
        # {'position': {'x': -20.0, 'y': 38.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
# # point B(34.0;11.0)
        # {'position': {'x': 2.0, 'y': 70.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
# #point C(30.0;83.0)
        # {'position': {'x': 19.0, 'y': 32.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},
# point D(8.0;87.0)
        # {'position': {'x': 8.0, 'y': 87.0, 'z': 0.0},
        #  'orientation': {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}},

        ]
    
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
        
        # Gửi goal và đợi hoàn thành
        success = follower.send_goal(pose)
        
        if not success:
            follower.get_logger().error(f'Không thể đến waypoint {i+1}')
            break
    
    follower.get_logger().info('Hoàn thành tất cả các waypoint')
    follower.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()