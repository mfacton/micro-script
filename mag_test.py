import time

from tools.plotter import Plot
from tools.serial_manager import DataType, SerialManager, pack_data, unpack_data

manager = SerialManager("slc-control-lib", baud=115200)
# plotter = Plot(3, -32768, 32767)

msg_type = [DataType.Int16, DataType.Int16, DataType.Int16, DataType.UInt16]

while True:
    data = manager.read_bytes(8)
    values = unpack_data(msg_type, data)
    print(values)
    # plotter.push(data)

    # data = manager.read_bytes(6)
    # print(f"{data[0]} {data[1]}")

    time.sleep(0.001)