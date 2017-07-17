from study7_12 import gif
import struct

width, height = struct.unpack('<HH',gif[6:10])
print(width,height)
