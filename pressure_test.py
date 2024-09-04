import time

from tools.plotter import Plot
from tools.serial_manager import DataType, SerialManager, pack_data, unpack_data

manager = SerialManager("slc-control-lib", baud=115200)

while True:
    data = manager.read_bytes(5)

    pressure = data[2] << 16 | data[1] << 8 | data[0]
    temperature = data[4] << 8 | data[3]

    temperature /= 100
    pressure /= 40.96

    print(f"P: {pressure:.2f}, T: {temperature:.2f}")

    time.sleep(0.001)