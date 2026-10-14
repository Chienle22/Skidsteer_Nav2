#!/usr/bin/env python3
"""
Trajectory Tracking Visualizer for Nav2 on Isaac ROS Dev
- Global path : /plan      -> đường xanh nét đứt (frame map)
- Robot path  : /amcl_pose -> đường đỏ            (frame map)
- Tự động lưu ảnh khi đến đích hoặc khi ấn Ctrl+C
"""

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseWithCovarianceStamped

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import signal
import sys
import os
from datetime import datetime

# ─────────────────────────────────────────────────────────────────────────────
SAVE_DIR          = "/home/chienle/Desktop/nav2_ws/src"
GLOBAL_PATH_TOPIC = "/plan"
ROBOT_POSE_TOPIC  = "/amcl_pose"   # frame map — khớp với /plan

# THÔNG SỐ MỚI: Bán kính sai số để xác nhận đã đến đích (đơn vị: mét)
GOAL_TOLERANCE    = 0.2 
# ─────────────────────────────────────────────────────────────────────────────


class TrajectoryPlotter(Node):
    def __init__(self):
        super().__init__('trajectory_plotter')

        self.global_path_x: list[float] = []
        self.global_path_y: list[float] = []
        self.robot_x: list[float] = []
        self.robot_y: list[float] = []

        self.tracking_started = False
        self.got_global_path  = False
        self.is_finished      = False  # Cờ kiểm tra trạng thái hoàn thành

        # ── subscribers ──────────────────────────────────────────────────────
        self.path_sub = self.create_subscription(
            Path, GLOBAL_PATH_TOPIC, self._path_cb, 10)

        self.pose_sub = self.create_subscription(
            PoseWithCovarianceStamped, ROBOT_POSE_TOPIC, self._pose_cb, 10)

        # ── matplotlib ───────────────────────────────────────────────────────
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self._setup_axes()

        self.line_global, = self.ax.plot([], [], 'b--', linewidth=2)
        self.line_robot,  = self.ax.plot([], [], 'r-',  linewidth=2)
        self.robot_dot,   = self.ax.plot([], [], 'ro',  markersize=8)
        self.start_dot,   = self.ax.plot([], [], 'go',  markersize=10, zorder=5)

        self.ax.legend(handles=[
            mpatches.Patch(color='blue',  label='Global Path (kế hoạch)'),
            mpatches.Patch(color='red',   label='Robot Trajectory (thực tế)'),
            mpatches.Patch(color='green', label='Start'),
        ], loc='upper left')

        self.draw_timer = self.create_timer(0.1, self._draw)

        self.get_logger().info(
            f'\n[TrajectoryPlotter] Sẵn sàng — cả 2 topic đều ở frame map\n'
            f'  {GLOBAL_PATH_TOPIC:<25} → global path\n'
            f'  {ROBOT_POSE_TOPIC:<25} → robot pose\n'
            f'  Hệ thống sẽ TỰ ĐỘNG LƯU ẢNH khi đến đích (cách goal < {GOAL_TOLERANCE}m)\n'
            f'  Hoặc ấn Ctrl+C để lưu sớm.')

    # ── callbacks ─────────────────────────────────────────────────────────────

    def _path_cb(self, msg: Path):
        xs = [p.pose.position.x for p in msg.poses]
        ys = [p.pose.position.y for p in msg.poses]
        if not xs:
            return
        self.global_path_x = xs
        self.global_path_y = ys
        self.got_global_path = True
        self.get_logger().info(
            f'[path] {len(xs)} điểm | '
            f'start=({xs[0]:.2f},{ys[0]:.2f}) '
            f'goal=({xs[-1]:.2f},{ys[-1]:.2f})')

    def _pose_cb(self, msg: PoseWithCovarianceStamped):
        # Nếu đã hoàn thành thì bỏ qua không update pose nữa
        if self.is_finished:
            return

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        if not self.tracking_started:
            if len(self.robot_x) == 0:
                self.robot_x.append(x)
                self.robot_y.append(y)
                self.get_logger().info(
                    f'[pose] Vị trí đầu robot: ({x:.3f}, {y:.3f})')
            else:
                dx = x - self.robot_x[0]
                dy = y - self.robot_y[0]
                if (dx**2 + dy**2) > 0.01**2:
                    self.tracking_started = True
                    self.get_logger().info(
                        '[pose] Robot bắt đầu di chuyển — đang vẽ!')
        else:
            self.robot_x.append(x)
            self.robot_y.append(y)

            # KIỂM TRA ĐIỀU KIỆN ĐẾN ĐÍCH
            if self.got_global_path:
                goal_x = self.global_path_x[-1]
                goal_y = self.global_path_y[-1]
                
                # Tính khoảng cách từ vị trí hiện tại đến goal
                distance_to_goal = np.hypot(x - goal_x, y - goal_y)
                
                if distance_to_goal < GOAL_TOLERANCE:
                    self.is_finished = True
                    self.get_logger().info(
                        f'✅ ĐÃ ĐẾN ĐÍCH (Cách goal {distance_to_goal:.3f}m). Đang tự động lưu ảnh...')
                    
                    # Gửi tín hiệu giả lập Ctrl+C để kích hoạt hàm _shutdown
                    os.kill(os.getpid(), signal.SIGINT)

    # ── vẽ ───────────────────────────────────────────────────────────────────

    def _setup_axes(self):
        self.ax.set_xlabel('X (m)', fontsize=12)
        self.ax.set_ylabel('Y (m)', fontsize=12)
        self.ax.set_title('Trajectory Tracking — Nav2 / Isaac ROS ',
                          fontsize=14)
        self.ax.set_aspect('equal', adjustable='datalim')
        self.ax.grid(True, linestyle='--', alpha=0.4)

    def _draw(self):
        if not self.got_global_path and not self.tracking_started:
            return
        if self.global_path_x:
            self.line_global.set_data(self.global_path_x, self.global_path_y)
        if len(self.robot_x) >= 1:
            self.start_dot.set_data([self.robot_x[0]], [self.robot_y[0]])
        if len(self.robot_x) > 1:
            self.line_robot.set_data(self.robot_x, self.robot_y)
            self.robot_dot.set_data([self.robot_x[-1]], [self.robot_y[-1]])
        self.ax.relim()
        self.ax.autoscale_view()
        try:
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
        except Exception:
            pass

    # ── lưu ảnh ──────────────────────────────────────────────────────────────

    def save_figure(self):
        os.makedirs(SAVE_DIR, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filepath = os.path.join(SAVE_DIR, f'tracking_{timestamp}.png')

        fig_save, ax_save = plt.subplots(figsize=(12, 9))
        ax_save.set_xlabel('X (m)', fontsize=13)
        ax_save.set_ylabel('Y (m)', fontsize=13)
        ax_save.set_title('Trajectory Tracking — Nav2 / Isaac ROS  [frame: map]',
                          fontsize=15)
        ax_save.set_aspect('equal', adjustable='datalim')
        ax_save.grid(True, linestyle='--', alpha=0.4)

        if self.global_path_x:
            ax_save.plot(self.global_path_x, self.global_path_y,
                         'b--', linewidth=2, label='Global Path (kế hoạch)')

        if len(self.robot_x) > 1:
            ax_save.plot(self.robot_x, self.robot_y,
                         'r-', linewidth=2, label='Robot Trajectory (thực tế)')
            ax_save.plot(self.robot_x[0], self.robot_y[0],
                         'go', markersize=12, label='Start', zorder=5)
            ax_save.plot(self.robot_x[-1], self.robot_y[-1],
                         'rs', markersize=12, label='End',   zorder=5)

        ax_save.legend(loc='upper left', fontsize=11)

        # Tracking error
        if self.global_path_x and len(self.robot_x) > 1:
            gx = np.array(self.global_path_x)
            gy = np.array(self.global_path_y)
            errors = [np.hypot(gx - rx, gy - ry).min()
                      for rx, ry in zip(self.robot_x, self.robot_y)]
            mean_e = np.mean(errors)
            max_e  = np.max(errors)
            rmse   = np.sqrt(np.mean(np.array(errors)**2))
            txt = (f'Mean error : {mean_e:.4f} m\n'
                   f'Max  error : {max_e:.4f} m\n'
                   f'RMSE       : {rmse:.4f} m\n'
                   f'Path pts   : {len(self.global_path_x)}\n'
                   f'Odom pts   : {len(self.robot_x)}')
            ax_save.text(0.02, 0.02, txt,
                         transform=ax_save.transAxes, fontsize=10,
                         verticalalignment='bottom',
                         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.85))

        fig_save.tight_layout()
        fig_save.savefig(filepath, dpi=150)
        plt.close(fig_save)
        print(f'\n✅ Ảnh đã lưu thành công tại: {filepath}')


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    rclpy.init()
    node = TrajectoryPlotter()

    def _shutdown(sig, frame):
        print('\n[Hệ thống] Nhận yêu cầu dừng. Đang tiến hành lưu ảnh...')
        node.save_figure()
        node.destroy_node()
        rclpy.shutdown()
        plt.close('all')
        sys.exit(0)

    signal.signal(signal.SIGINT, _shutdown)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        _shutdown(None, None)


if __name__ == '__main__':
    main()
