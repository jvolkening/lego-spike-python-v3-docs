"""The `force_sensor` module contains all functions and constants to use
the Force Sensor.

To use the Force Sensor module add the following import statement to your
project:

`import force_sensor`

All functions in the module should be called inside the `force_sensor`
module as a prefix like so:

`force_sensor.force(port.A)`

"""

def force(port: int) -> int:
    """Retrieves the measured force as decinewton. Values range from 0 to
    100

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def pressed(port: int) -> bool:
    """Tests whether the button on the sensor is pressed. Returns true if
    the force sensor connected to port is pressed.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: bool
    """

def raw(port: int) -> int:
    """Returns the raw, uncalibrated force value of the force sensor
    connected on port `port`

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

