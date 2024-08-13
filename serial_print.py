import time

from tools.serial_manager import SerialManager

manager = SerialManager("slc-control-lib", baud=38400)

while True:
    data = manager.read_all()
    if data:
        print(data.decode())
    time.sleep(0.001)