"""The `device` module enables you to write code to get information about
devices plugged into the hub.

To use the Device module add the following import statement to your
project:

`import device`

All functions in the module should be called inside the `device` module as
a prefix like so:

`device.device_id(port.A)`

"""

def data(port: int) -> tuple[int]:
    """Retrieve the raw LPF-2 data from a device.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: tuple
    """

def id(port: int) -> int:
    """Retrieve the device id of a device. Each device has an id based on
    its type.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def get_duty_cycle(port: int) -> int:
    """Retrieve the duty cycle for a device. Returned values is in range 0
    to 10000

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def ready(port: int) -> bool:
    """When a device is attached to the hub it might take a short amount of
    time before it's ready to accept requests.<br />
    Use `ready` to test for the readiness of the attached devices.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: bool
    """

def set_duty_cycle(port: int, duty_cycle: int) -> None:
    """Set the duty cycle on a device. Range 0 to 10000

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param duty_cycle: The PWM value (0-10000)
    :type duty_cycle: int
    :rtype: None
    """

