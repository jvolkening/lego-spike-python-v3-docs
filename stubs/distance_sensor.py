"""The `distance_sensor` module enables you to write code that reacts to
specific distances or light up the Distance Sensor in different ways.

To use the Distance Sensor module add the following import statement to
your project:

`import distance_sensor`

All functions in the module should be called inside the `distance_sensor`
module as a prefix like so:

`distance_sensor.distance(port.A)`

"""

def clear(port: int) -> None:
    """Turns off all the lights in the Distance Sensor connected to `port`.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: None
    """

def distance(port: int) -> int:
    """Retrieve the distance in millimeters captured by the Distance Sensor
    connected to `port`. If the Distance Sensor cannot read a valid
    distance it will return -1.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def get_pixel(port: int, x: int, y: int) -> int:
    """Retrieve the intensity of a specific light on the Distance Sensor
    connected to `port`.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param x: The X value (0 - 3)
    :type x: int
    :param y: The Y value, range (0 - 3)
    :type y: int
    :rtype: int
    """

def set_pixel(port: int, x: int, y: int, intensity: int) -> None:
    """Changes the intensity of a specific light on the Distance Sensor
    connected to `port`.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param x: The X value (0 - 3)
    :type x: int
    :param y: The Y value, range (0 - 3)
    :type y: int
    :param intensity: How bright to light up the pixel
    :type intensity: int
    :rtype: None
    """

def show(port: int, pixels: list[int]) -> None:
    """Change all the lights at the same time.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param pixels: A list containing intensity values for all 4 pixels.
    :type pixels: bytes
    :rtype: None
    """

