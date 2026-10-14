ros2 launch bringup bringup_2.py
~/nav2_ws$ ros2 launch nav2_bringup bringup_launch.py use_sim_time:=false  map:=/home/chienle/Desktop/skid_robot_v2/src/mapping/map/A10_t2/A10_t2.yaml 
ros2 launch nav2_bringup rviz_launch.py 
# sau khi định vị robot
python3 initial_pose_publisher.py             // Đặt vị trí ban đầu cho AMCL
# Run code thu thập data trước khi gửi goal pose
python3 save_data.py				// node thu thap du lieu chinh  trước khi gửi goal
# Gửi goal			
python3 waypoit_fl.py (Nếu dùng waypoint được viết sẵn)  or python3 csv_path_publisher.py (dùng waypoint từ CSV) or python3 Nav_through_poses.py
python3 distance_calculator_tf.py		//tính tổng quãng đường robot chạy
# Sau khi chạy xong thì Ctrl C để stop lưu data
--- --- --- ---

#Sau khi thu thap xong
python3 caculator_rmse.py			// tinh rmse
python3 Bam_quy_dao.py		 or 	python3 bieu_do_path.py		// ve quy dao
python3 bieu_do_v.py				// ve van toc
python3 sai_so_x.py			
python3 sai_so_y.py
python3 tinh_path.py				// tinh do dai path



#Quy dao dua vao robot
python3 waypoit_fl.py or python3 csv_path_publisher.py

# cách Xác định vị trí Goal trên map
ros2 topic echo /goal_pose
ros2 topic list | grep goal   // để tìm topic liên quan đến goal pose

# Các file csv có được sau khi run
nav2_ws/
└── src/
    └── scripts/
        ├── save_data.py
        │
        ├── amcl/
        │   └── amcl_data_YYYYMMDD_HHMMSS.csv
        │
        ├── path/
        │   └── local_plan_data_YYYYMMDD_HHMMSS.csv
        │
        ├── odom/
        │   └── odom_data_YYYYMMDD_HHMMSS.csv
        │
        ├── cmd_vel/
        │   └── cmd_vel_data_YYYYMMDD_HHMMSS.csv
        │
        └── first_path/
            └── first_path_data_YYYYMMDD_HHMMSS.csv

