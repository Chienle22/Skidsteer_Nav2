import pandas as pd
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

# ---- ĐƯỜNG DẪN FILE ----

##RMSE sai so bam quy dao van toc 0.5m/s
path_file = "/home/chienle/Desktop/nav2_ws/src/scripts/amcl/mppi_0.5ms/amcl_mppi_0.5_fix.csv"
# rpp_file = "/home/chienle/nav2_ws_250606/src/scripts/robot_distance/simulation_A10/rpp_0.5ms_robot_distance_20250701_162037.csv"
mppi_file = "/home/chienle/Desktop/nav2_ws/src/scripts/amcl/rpp_0.5ms/amcl_data_20261003_125937.csv"

# # RMSE sai so bam quy dao van toc 1m/s
# path_file = "/home/chienle/nav2_ws_250606/src/scripts/first_path/first_path_data_20250704_113031.csv"
# rpp_file = "/home/chienle/nav2_ws_250606/src/scripts/robot_distance/rpp_1ms_robot_distance_20250704_142621.csv"
# mppi_file = "/home/chienle/nav2_ws_250606/src/scripts/robot_distance/mppi_1ms_robot_distance_20250704_113032.csv"

# ========== ĐỌC FILE FIRST PATH ==========

df_path = pd.read_csv(path_file)
print("=== PATH FILE ===")
print(df_path.head())
print("Columns:", df_path.columns.tolist())

# Lấy đúng 2 cột x,y
path_points = df_path[["x", "y"]].dropna().values
print(f"Path points shape: {path_points.shape}")

# KDTree cho path
tree = KDTree(path_points)

# # ========== ĐỌC FILE RPP ==========

# df_rpp = pd.read_csv(rpp_file)
# print("\n=== RPP FILE ===")
# print(df_rpp.head())
# print("Columns:", df_rpp.columns.tolist())

# # Lấy đúng 2 cột x,y
# rpp_points = df_rpp[["x", "y"]].dropna().values
# print(f"RPP points shape: {rpp_points.shape}")

# Tính RMSE RPP
# dists_rpp, _ = tree.query(rpp_points)
# rmse_rpp = np.sqrt(np.mean(dists_rpp**2))
# print(f"\n✅ RMSE RPP: {rmse_rpp:.4f} m")

# ========== ĐỌC FILE MPPI ==========

df_mppi = pd.read_csv(mppi_file)
print("\n=== MPPI FILE ===")
print(df_mppi.head())
print("Columns:", df_mppi.columns.tolist())

# Lấy đúng 2 cột x,y
mppi_points = df_mppi[["x", "y"]].dropna().values
print(f"MPPI points shape: {mppi_points.shape}")

# Tính RMSE MPPI
dists_mppi, _ = tree.query(mppi_points)
rmse_mppi = np.sqrt(np.mean(dists_mppi**2))
print(f"\n✅ RMSE MPPI: {rmse_mppi:.4f} m")

# ========== VẼ HÌNH ==========

# plt.figure(figsize=(10,5))
# plt.plot(path_points[:,0], path_points[:,1], 'r-', label='Reference Path')
# plt.plot(rpp_points[:,0], rpp_points[:,1], 'b--', label=f'RPP Trajectory (RMSE={rmse_rpp:.4f} m)')
# plt.plot(mppi_points[:,0], mppi_points[:,1], 'g--', label=f'MPPI Trajectory (RMSE={rmse_mppi:.4f} m)')

# plt.legend()
# plt.xlabel("x (m)")
# plt.ylabel("y (m)")
# plt.title("Trajectory Tracking Comparison")
# plt.grid()
# plt.tight_layout()
# plt.show()
