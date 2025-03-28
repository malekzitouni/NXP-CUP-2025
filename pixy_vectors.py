from __future__ import print_function
import pixy
from ctypes import *
from pixy import *
import csv
import os
from datetime import datetime

print("Pixy2 Python SWIG Example -- Saving Vectors to CSV")

# Initialize Pixy
pixy.init()
pixy.change_prog("line")

# CSV file setup
output_dir = os.path.expanduser("~/Desktop")  # Save to Desktop (change if needed)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_filename = os.path.join(output_dir, f"pixy_vectors_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

# Write CSV headers
with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['frame', 'index', 'x0', 'y0', 'x1', 'y1', 'flags'])

print(f"CSV file will be saved to: {csv_filename}")

frame = 0
try:
    while True:
        line_get_all_features()
        vectors = VectorArray(100)  # Reset vectors each frame
        v_count = line_get_vectors(100, vectors)

        if v_count > 0:
            with open(csv_filename, mode='a', newline='') as csv_file:  # Append mode
                writer = csv.writer(csv_file)
                for index in range(v_count):
                    writer.writerow([
                        frame,
                        vectors[index].m_index,
                        vectors[index].m_x0,
                        vectors[index].m_y0,
                        vectors[index].m_x1,
                        vectors[index].m_y1,
                        vectors[index].m_flags
                    ])
            print(f"Frame {frame}: Saved {v_count} vectors")
            frame += 1

except KeyboardInterrupt:
    print(f"\nScript stopped. Vectors saved to: {csv_filename}")