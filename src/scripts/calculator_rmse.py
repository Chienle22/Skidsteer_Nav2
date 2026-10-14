import pandas as pd
import numpy as np
from scipy.spatial import KDTree

# ---- ĐƯỜNG DẪN FILE (Cấu hình cho vận tốc 0.5m/s) ----
path_file = "/home/chienle/Desktop/nav2_ws/src/scripts/first_path/first_path_3_goals.csv"
mppi_file = "/home/chienle/Desktop/nav2_ws/src/scripts/amcl/amcl_data_mppi_1.0_3.csv"
rpp_file = "/home/chienle/Desktop/nav2_ws/src/scripts/amcl/amcl_data_rpp_1.0_3.csv"

# # (Nếu chuyển sang 1m/s, bạn chỉ cần thay đường dẫn ở đây)
#path_file = "/home/chienle/Desktop/nav2_ws/src/scripts/first_path/first_path_data_20261002_205832.csv"
#rpp_file = "/home/chienle/Desktop/nav2_ws/src/scripts/amcl/rpp_1ms/amcl_data_20261003_131423.csv"
#mppi_file = "/home/chienle/Desktop/nav2_ws/src/scripts/amcl/mppi_1ms/amcl_mppi_1ms_fix.csv"

# ========== 1. ĐỌC REFERENCE PATH ==========
df_path = pd.read_csv(path_file)
path_points = df_path[["x", "y"]].dropna().values
tree = KDTree(path_points)

# ========== 2. TÍNH RMSE CHO RPP ==========
df_rpp = pd.read_csv(rpp_file)
rpp_points = df_rpp[["x", "y"]].dropna().values
dists_rpp, _ = tree.query(rpp_points)
rmse_rpp = np.sqrt(np.mean(dists_rpp**2))

# ========== 3. TÍNH RMSE CHO MPPI ==========
df_mppi = pd.read_csv(mppi_file)
mppi_points = df_mppi[["x", "y"]].dropna().values
dists_mppi, _ = tree.query(mppi_points)
rmse_mppi = np.sqrt(np.mean(dists_mppi**2))

# ========== 4. IN KẾT QUẢ ==========
print("========================================")
print(f"✅ RMSE RPP  : {rmse_rpp:.4f} m")
print(f"✅ RMSE MPPI : {rmse_mppi:.4f} m")
print("========================================")
