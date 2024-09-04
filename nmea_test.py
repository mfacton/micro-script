import time

from tools.plotter import Plot
from tools.serial_manager import DataType, SerialManager, pack_data, unpack_data

manager = SerialManager("slc-control-lib", baud=115200)

msg_type = [DataType.Float]

while True:
    data = unpack_data(msg_type, manager.read_bytes(4))
    print(data)

    time.sleep(0.001)