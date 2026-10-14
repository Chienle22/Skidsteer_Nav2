import pandas as pd
import numpy as np
import os
import re
from scipy.spatial.distance import cdist

def extract_timestamp_from_filename(filename):
    m = re.search(r'(\d{8}_\d{6})', filename)
    if m:
        return m.group(1)
    else:
        return None

def find_closest_index(path, point, distance_thresh=0.5):
    """
    Tìm index trên path gần nhất với point
    """
    dists = np.linalg.norm(path - point, axis=1)
    idx = np.argmin(dists)
    if dists[idx] < distance_thresh:
        return idx
    else:
        # Không tìm thấy điểm gần
        return None

def filter_local_paths_diff_segments(input_csv, output_folder, distance_thresh=0.5):
    df = pd.read_csv(input_csv)

    # Group các path riêng theo timestamp
    paths = []
    timestamps = []

    for t, group in df.groupby("timestamp"):
        xy = group[["x", "y"]].values
        paths.append(xy)
        timestamps.append(t)

    print(f"Tổng số path: {len(paths)}")

    result_segments = []
    
    for i in range(len(paths)-1):
        path_curr = paths[i]
        path_next = paths[i+1]

        # Lấy điểm đầu tiên của path tiếp theo
        first_point_next = path_next[0]

        # Tìm vị trí điểm đó trong path hiện tại
        idx_in_curr = find_closest_index(path_curr, first_point_next, distance_thresh)

        if idx_in_curr is not None and idx_in_curr > 0:
            # Lấy đoạn từ đầu path_curr tới trước idx_in_curr
            segment = path_curr[:idx_in_curr]
            if len(segment) > 0:
                result_segments.append(segment)
        else:
            # Nếu không tìm thấy → lấy nguyên path_curr
            result_segments.append(path_curr)

    # Sau cùng, thêm path cuối cùng vì nó chưa bị path nào thay thế
    result_segments.append(paths[-1])

    # Gộp toàn bộ segments
    final_path = np.vstack(result_segments)
    print(f"Tổng số điểm trong fix_path: {len(final_path)}")

    # Xuất file CSV
    timestamp_str = extract_timestamp_from_filename(os.path.basename(input_csv))
    if timestamp_str is None:
        timestamp_str = "unknown"
    output_filename = f"path_fix_{timestamp_str}.csv"
    output_csv = os.path.join(output_folder, output_filename)

    filtered_df = pd.DataFrame(final_path, columns=["x", "y"])
    filtered_df.to_csv(output_csv, index=False)
    print(f"Đã ghi file CSV: {output_csv}")

if __name__ == "__main__":
    input_csv = "/home/chienle/nav2_ws/src/scripts/path/three_points.csv"
    output_folder = "/home/chienle/nav2_ws/src/scripts/path_fix/"
    filter_local_paths_diff_segments(input_csv, output_folder, distance_thresh=0.5)
