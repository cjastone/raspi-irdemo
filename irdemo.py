#!/usr/bin/python
import evdev
from time import sleep

# returns path of gpio ir receiver device
def get_ir_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if (device.name == "gpio_ir_recv"):
            print("Using device", device.path, "\n")
            return device

    print("No device found!")
    sys.exit()

# returns a generator object that yields InputEvent instances
# raises BlockingIOError if no events available, which much be caught
def get_all_events(dev):
    return dev.read()

# returns the most recent InputEvent instance
# returns NoneType if no events available
def get_last_event(dev):
    try:
        for event in dev.read():	# iterate through all queued events
            if (event.value > 0):
                last_event = event
    except BlockingIOError: # no events to be read
        last_event = None

    return last_event

# returns the next InputEvent instance
# blocks until event is available
def get_next_event(dev):
    while(True):
    	event = dev.read_one()
    	if (event):
    		return event

def main():
    device = get_ir_device()

    print("Waiting 5 seconds for IR signals.  A list of all received commands will be returned.")
    sleep(5)
    events = get_all_events(device)
    try:
        event_list = [event.value for event in events]
        print("Received commands:", event_list, "\n")
    except BlockingIOError:
        print("No commands received.\n")

    print("Waiting 5 seconds for IR signals.  The last received command will be returned.")
    sleep(5)
    last_event = get_last_event(device)
    if last_event is not None:
        print("Received command:", last_event.value, "\n")
    else:
        print("No commands received.\n")

    print("Waiting indefinitely for IR signals.  The first received command will be returned.")
    next_event = get_next_event(device)
    print("Received command:", next_event.value, "\n")

if __name__ == "__main__":
    main()
