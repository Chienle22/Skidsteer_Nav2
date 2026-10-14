import pandas as pd
import matplotlib.pyplot as plt

file_rpp = "/home/chienle/nav2_ws/src/scripts/robot_distance/robot_distance_20250821_184449.csv"
# file_mppi = "/home/chienle/nav2_ws/src/scripts/robot_distance/V_Mppi_05ms.csv"
file_mppi = ('/home/chienle/nav2_ws/src/scripts/robot_distance/robot_distance_20250821_194407.csv')
# Đọc file RPP
df_rpp = pd.read_csv(file_rpp, skiprows=lambda x: x==1 or "---" in open(file_rpp).readlines()[x])
print("==== RPP columns ====")
print(df_rpp.columns)

# Chuyển cột numeric
for col in ["Elapsed Time (s)", "Linear Velocity (m/s)"]:
    if col in df_rpp.columns:
        df_rpp[col] = pd.to_numeric(df_rpp[col], errors='coerce')

df_rpp_clean = df_rpp.dropna(subset=["Elapsed Time (s)", "Linear Velocity (m/s)"])

# Đọc file MPPI
df_mppi = pd.read_csv(file_mppi, skiprows=lambda x: x==1 or "---" in open(file_mppi).readlines()[x])
print("==== MPPI columns ====")
print(df_mppi.columns)

for col in ["Elapsed Time (s)", "Linear Velocity (m/s)"]:
    if col in df_mppi.columns:
        df_mppi[col] = pd.to_numeric(df_mppi[col], errors='coerce')

df_mppi_clean = df_mppi.dropna(subset=["Elapsed Time (s)", "Linear Velocity (m/s)"])

# In số hàng dữ liệu xem còn không
print(f"Rows in RPP data: {len(df_rpp_clean)}")
print(f"Rows in MPPI data: {len(df_mppi_clean)}")

# Tìm max Elapsed Time để vẽ đường ngang đủ dài
max_time = 0
if len(df_rpp_clean) > 0:
    max_time = max(max_time, df_rpp_clean["Elapsed Time (s)"].max())
if len(df_mppi_clean) > 0:
    max_time = max(max_time, df_mppi_clean["Elapsed Time (s)"].max())

plt.figure(figsize=(10,5))

# ✅ Vẽ đường đỏ trước (zorder thấp) để nó nằm dưới
plt.hlines(
    y=0.5,
    xmin=0,
    xmax=max_time,
    colors='red',
    linestyles='solid',
    linewidth=3,
    label='Max Velocity 0.5m/s',
    zorder=1
)

# Vẽ RPP
if len(df_rpp_clean) > 0:
    plt.plot(
        df_rpp_clean["Elapsed Time (s)"],
        df_rpp_clean["Linear Velocity (m/s)"],
        label="MPPI 1 Obstacle",
        linewidth=3,
        color='green',
        linestyle='--',
        zorder=2
    )

# Vẽ MPPI
if len(df_mppi_clean) > 0:
    plt.plot(
        df_mppi_clean["Elapsed Time (s)"],
        df_mppi_clean["Linear Velocity (m/s)"],
        label="MPPI 2 Obstacle",
        linewidth=3,
        color='blue',
        linestyle='--',
        zorder=2
    )

plt.xlabel("Time (s)")
plt.ylabel("Linear Velocity (m/s)")
plt.title("Velocity Response:MPPI 0.5m/s")
plt.legend()
plt.grid(True)
plt.show()
