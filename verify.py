import pixy

from pixy import *
pixy.init()
print("Pixy initialized successfully")
blocks = BlockArray(10)
count = pixy.ccc_get_blocks(10, blocks)
print(f"Found {count} blocks")