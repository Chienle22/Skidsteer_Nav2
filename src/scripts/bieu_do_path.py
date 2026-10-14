import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Đọc dữ liệu
# =========================

path_data = pd.read_csv(
    '/home/chienle/Desktop/nav2_ws/src/scripts/first_path/first_path_data_20250711_210756.csv'
)

amcl_data_mppi_05 = pd.read_csv(
    '/home/chienle/Desktop/nav2_ws/src/scripts/amcl/Data_simulation_2706/Mppi_1ms.csv'
)

amcl_data_rpp_05 = pd.read_csv(
    '/home/chienle/Desktop/nav2_ws/src/scripts/amcl/Data_simulation_2706/Rpp_1ms.csv'
)

# =========================
# Lấy dữ liệu x, y
# Chuyển Pandas Series -> NumPy array
# =========================

path_x = path_data['x'].to_numpy()
path_y = path_data['y'].to_numpy()

amcl_x_mppi_05 = amcl_data_mppi_05['x'].to_numpy()
amcl_y_mppi_05 = amcl_data_mppi_05['y'].to_numpy()

amcl_x_rpp_05 = amcl_data_rpp_05['x'].to_numpy()
amcl_y_rpp_05 = amcl_data_rpp_05['y'].to_numpy()

# =========================
# Tạo biểu đồ
# =========================

plt.figure(figsize=(6, 8))

# Reference Path
plt.plot(
    path_x,
    path_y,
    label='Reference Path',
    color='red',
    linewidth=4
)

# MPPI
plt.plot(
    amcl_x_mppi_05,
    amcl_y_mppi_05,
    label='Position Trajectory 0.5m/s',
    color='blue',
    linewidth=3,
    linestyle='--'
)

# RPP
plt.plot(
    amcl_x_rpp_05,
    amcl_y_rpp_05,
    label='Position Trajectory 1m/s',
    color='lime',
    linewidth=3,
    linestyle='--'
)

# =========================
# Nhãn
# =========================

plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')

plt.title(
    'Position Trajectory of a Robot Avoiding An Obstacle '
    'Using an MPPI Controller at Speeds of 0.5 m/s and 1 m/s'
)

plt.legend()
plt.grid(True)

plt.show()
