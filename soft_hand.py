import time

from tools.plotter import Plot
from tools.serial_manager import DataType, SerialManager, pack_data, unpack_data

manager = SerialManager("soft-hand", baud=115200)
plotter = Plot(3, 0, 65535)

msg_type = [DataType.UInt16, DataType.UInt16, DataType.UInt16]


while True:
    data = manager.read_bytes(6)
    values = unpack_data(msg_type, data)
    plotter.push(values)
    # print(values)