import time

from tools.plotter import Plot
from tools.serial_manager import DataType, SerialManager, pack_data, unpack_data

manager = SerialManager("slc-control-lib", baud=115200)
# plotter = Plot(3, -32768, 32767)

msg_type = [DataType.UInt8, DataType.Int16, DataType.Int16, DataType.Int16, DataType.Int16, DataType.Int16, DataType.Int16, DataType.Int16, DataType.UInt16, DataType.UInt8, DataType.UInt8, DataType.UInt8]

while True:
    data = unpack_data(msg_type, manager.read_bytes(20))
    print(data)

    time.sleep(0.001)