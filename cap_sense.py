import time

from tools.plotter import Plot
from tools.serial_manager import DataType, SerialManager, unpack_data

manager = SerialManager("flex-control", baud=38400)
plot = Plot(1, 20000, 40000, pixel_shift=2)

while True:
    data = manager.read_bytes(4)
    values = unpack_data([DataType.UInt16, DataType.UInt16], data)
    
    # print(f"{values[0]:05d} : 0x{values[0]:04x} : 0b{(values[0]>>8):08b} {(values[0]&0xff):08b}")
    # print(values[0]//16)

    plot.push(values)

    time.sleep(0.001)