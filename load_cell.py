import time

from tools.can_manager import CanManager
from tools.plotter import Plot
from tools.serial_manager import SerialManager

ser_manager = SerialManager("usb-can", baud=460800)
can_manager = CanManager(ser_manager)

plot = Plot(7, 98000, 103000)

while True:
    id, data, dlc_idx = can_manager.receive_frame()

    pressures = []
    temperatures = []
    for i in range(7):
        start_index = i * 5
        pressures.append(
            (data[start_index + 2] << 16 | data[start_index + 1] << 8 | data[start_index])/40.96
        )
        temperatures.append((data[start_index + 4] << 8 | data[start_index + 3])/100)

    plot.push(pressures)

    # print([int(p) for p in pressures])
    # print([int(t) for t in temperatures])
    # print()
