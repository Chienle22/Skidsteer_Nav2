import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ 2 file CSV (thay đổi đường dẫn tới file của bạn)
path_data = pd.read_csv('/home/chienle/nav2_ws/src/scripts/first_path/first_path_data_20250812_185947.csv')  
# path_data_1 = pd.read_csv('/home/chienle/nav2_ws_250606/src/scripts/first_path/first_path_data_20250711_210756.csv') 
# amcl_data_mppi = pd.read_csv('/home/chienle/nav2_ws_250606/src/scripts/amcl/Data_simulation_2706/Mppi_1ms.csv')  
# amcl_data_rpp = pd.read_csv('/home/chienle/nav2_ws_250606/src/scripts/amcl/Data_simulation_2706/Rpp_1ms_.csv') 

amcl_data_mppi_05 = pd.read_csv('/home/chienle/Desktop/Data_outdoor/Tránh vật cản/250822_Tránh vật cản/1 vật cản/0.5ms_robot_distance_20250821_184449.csv')  #171145
amcl_data_rpp_05 = pd.read_csv('/home/chienle/Desktop/Data_outdoor/Tránh vật cản/250822_Tránh vật cản/1 vật cản/1ms_robot_distance_20250812_185419.csv')
# first_path_data = pd.read_csv('/home/chienle/nav2_ws/src/scripts/first_path/first_path_data_20250407_003128.csv')  # Dữ liệu từ path 5m/s
#odom_data = pd.read_csv('/home/chienle/nav2_ws/src/scripts/amcl/amcl_data_20250405_135915.csv')  # Dữ liệu từ path 3m/s
# Giả sử rằng trong cả 2 file CSV, bạn có cột 'x' và 'y'
# Nếu tên cột khác, bạn cần điều chỉnh cho đúng với tên cột trong file của bạn

# Lấy dữ liệu x, y từ AMCL và path

path_x = path_data['x']
path_y = path_data['y']

# path_x_1 = path_data_1['x']
# path_y_1 = path_data_1['y']

amcl_x_mppi_05 = amcl_data_mppi_05['x']
amcl_y_mppi_05 = amcl_data_mppi_05['y']

amcl_x_rpp_05 = amcl_data_rpp_05['x']
amcl_y_rpp_05 = amcl_data_rpp_05['y']

# amcl_x_rpp_10 = amcl_data_rpp_10['x']
# amcl_y_rpp_10 = amcl_data_rpp_10['y']

# first_path_x = first_path_data['y']
# first_path_y = first_path_data['x']

# odom_data_x = odom_data['x']
# odom_data_y = odom_data['y']

# Tạo một biểu đồ để so sánh
plt.figure(figsize=(6, 8))

# Vẽ Path (quỹ đạo được tính toán) trước
#plt.plot(path_x, path_y, label='Optimal Path', color='red', linestyle='--', marker='x')
plt.plot(path_x, path_y, label='Reference Path', color='red',linewidth=4, ) #(marker='o')
# plt.plot(path_x_1, path_y_1, label='Path 2', color='brown',linewidth=4, ) #(marker='o')




# # Vẽ AMCL (vị trí thực tế của robot) sau, đường màu xanh sẽ hiển thị trên cùng
plt.plot(amcl_x_mppi_05, amcl_y_mppi_05, label='Position Trajectory 0.5m/s', color='blue',linewidth=3, linestyle='--') #(marker='o')

# # Vẽ AMCL (vị trí thực tế của robot) sau, đường màu xanh sẽ hiển thị trên cùng
plt.plot(amcl_x_rpp_05, amcl_y_rpp_05, label='Position Trajectory 1m/s', color='lime',linewidth=3, linestyle='--') #(marker='o')

# Vẽ AMCL (vị trí thực tế của robot) sau, đường màu xanh sẽ hiển thị trên cùng
# plt.plot(amcl_x_rpp_10, amcl_y_rpp_10, label='RPP 1m/s', color='blue',linewidth=3) #(marker='o')



# Thêm nhãn cho các trục và tiêu đề
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
# plt.title('Comparison of Path Tracking using MPPI and RPP Controllers for Mobile Robot')
plt.title('Position Trajectory of a Robot Avoiding An Obstacle Using an MPPI Controller at Speeds of 0.5 m/s and 1 m/s')
# plt.title('Robot Trajectory Avoiding Obstacles Using MPPI')
# plt.gca().invert_xaxis() # Lật trục X
# plt.yticks([0.0, 0.25, 0.5 , 0.75, 1.0])
# Thêm chú thích để phân biệt hai quỹ đạo
plt.legend()

# Hiển thị biểu đồ
plt.grid(True)
plt.show()
