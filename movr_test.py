import can
from tinymovr.bus_router import get_router, init_router
from tinymovr.channel import CANChannel
from tinymovr.config import configure_logging, get_bus_config

params = get_bus_config(["canine", "slcan_disco"], bitrate=1000000)
init_router(can.Bus, params, configure_logging())

def filter(frame):
    return True

def print_smth(frame):
    print(frame)

get_router().add_client(filter, print_smth)

chan = CANChannel(node_id=0)

frame = can.Message(
            arbitration_id=69,
            is_extended_id=False,
            is_remote_frame=False,
            data=bytearray([1, 0, 0, 0, 0]),
        )
get_router().send(frame)

while True:
    pass
