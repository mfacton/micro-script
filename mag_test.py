import time

from tools.plotter import Plot
from tools.serial_manager import DataType, SerialManager, pack_data, unpack_data

manager = SerialManager("mag-test", baud=115200)
plotter = Plot(3, -32768, 32767)

msg_type = [DataType.Int16, DataType.Int16, DataType.Int16]

while True:
    data = unpack_data(msg_type, manager.read_bytes(6))
    plotter.push(data)

    time.sleep(0.001)