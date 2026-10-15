## 1. Overview
ROS 2 navigation packages featuring custom trajectory tracking controllers and localization configurations for skid-steer mobile robots.

## 2. Installation & Build

Clone the Repository

```bash
cd ~/Desktop
git clone https://github.com/Chienle22/Skidsteer_Nav2
cd Skidsteer_Nav2
```
Build the Workspace

```bash
source /opt/ros/humble/setup.bash
colcon build --symlink-install --parallel-workers 1
```
Affter the workspace is builded successfully:
```bash
source install/setup.bash
```

## 3. Quick Start

### Terminal 1
Launch the entire robot system within the workspace for the skid-steer robot named `skid_robot_v2`

```bash
cd ~/Desktop/skid_steer_v2/
source install/setup.bash
ros2 launch bringup bringup_2.py
```
***Ensure that the robot startup process proceeds without any errors and that the robot’s wheels are locked 

### Terminal 2
Launch the navigation2 navigation stack
```bash
cd ~/Desktop/Skidsteer_Nav2/
source install/setup.bash
ros2 launch nav2_bringup bringup_launch.py

### Terminal 3

### Terminal 4

