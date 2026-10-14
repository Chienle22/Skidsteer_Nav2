import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ 2 file CSV (thay đổi đường dẫn tới file của bạn)

denta_5m = pd.read_csv('/home/chienle/Desktop/sai_so_truc_x.csv')  # Dữ liệu từ path 5m/s
denta_3m = pd.read_csv('/home/chienle/Desktop/sai_so_truc_x.csv')  # Dữ liệu từ path 5m/s
denta = pd.read_csv('/home/chienle/Desktop/sai_so_truc_x.csv')  # Dữ liệu từ path 5m/s

#odom_data = pd.read_csv('/home/chienle/nav2_ws/src/scripts/amcl/amcl_data_20250405_135915.csv')  # Dữ liệu từ path 3m/s
# Giả sử rằng trong cả 2 file CSV, bạn có cột 'x' và 'y'
# Nếu tên cột khác, bạn cần điều chỉnh cho đúng với tên cột trong file của bạn

# Lấy dữ liệu x, y từ AMCL và path
denta_x = denta['x']
denta_y = denta['denta']

denta_5m_x = denta['x']
denta_5m_y = denta['denta y_5m']

denta_3m_x = denta['x']
denta_3m_y = denta['denta_y3m']

# odom_data_x = odom_data['x']
# odom_data_y = odom_data['y']

# Tạo một biểu đồ để so sánh
plt.figure(figsize=(8, 4))

# Vẽ Path (quỹ đạo được tính toán) trước
#plt.plot(path_x, path_y, label='Optimal Path', color='red', linestyle='--', marker='x')
plt.plot(denta_x, denta_y, label='Reference path', color='green',linewidth=2) #(marker='o')

# Vẽ AMCL (vị trí thực tế của robot) sau, đường màu xanh sẽ hiển thị trên cùng
plt.plot(denta_5m_x, denta_5m_y, label='AMCL Path 0.5m/s', color='blue',linewidth=2,linestyle='--') #(marker='o')

# Vẽ first path (vị trí thực tế của robot) sau, đường màu green sẽ hiển thị trên cùng
plt.plot(denta_3m_x, denta_3m_y, label='AMCL Path 0.3m/s', color='red',linewidth=2,linestyle='--') #(marker='o')

# Vẽ odom (vị trí thực tế của robot) sau, đường màu xanh sẽ hiển thị trên cùng
#plt.plot(odom_data_x, odom_data_y, label='Reference Path 3m/s', color='grey',linewidth=3) #(marker='o')

# Thêm nhãn cho các trục và tiêu đề
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Sai số trục x')

plt.yticks([-0.05, 0.0, 0.05, 0.1])
# Thêm chú thích để phân biệt hai quỹ đạo
plt.legend()

# Hiển thị biểu đồ
plt.grid(True)
plt.show()
