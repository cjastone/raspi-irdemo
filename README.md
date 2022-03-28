# Raspberry Pi Infrared Reception Demonstration
A simple demonstration of infrared reception on the Raspberry Pi using Python and [evdev](https://python-evdev.readthedocs.io/en/latest/).
### Basic Functionality
Reception of infrared scancodes is implemented through four basic functions, exposing most common features that are intended to cover most use cases:

    get_ir_device()
Returns the input device index of the IR sensor.  This must be supplied to all subsequent functions.

    get_all_events(dev)
Returns a generator object that yields [InputEvent](https://python-evdev.readthedocs.io/en/latest/apidoc.html#evdev.events.InputEvent) instances.  This function raises a BlockingIOError exception if no events are available, which much be handled by the code from which it's called.

    get_last_event(dev):	
Returns the most recent [InputEvent](https://python-evdev.readthedocs.io/en/latest/apidoc.html#evdev.events.InputEvent) instance only.  Returns NoneType if no events available and does not raise any exceptions.

    get_next_event(dev):	
Returns the next [InputEvent](https://python-evdev.readthedocs.io/en/latest/apidoc.html#evdev.events.InputEvent) instance.  This is a blocking function and execution will not proceed until an InputEvent becomes available.

### Further Reading
For detailed implementation instructions, please refer to the accompanying blog post at ignorantofthings.com.
