"""The `color_sensor` module enables you to write code that reacts to
specific colors or the intensity of the reflected light.

To use the Color Sensor module add the following import statement to your
project:

`import color_sensor`

All functions in the module should be called inside the `color_sensor`
module as a prefix like so:

`color_sensor.reflection(port.A)`

The Color Sensor can recognize the following colors:

Red<br />
Green<br />
Blue<br />
Magenta<br />
Yellow<br />
Orange<br />
Azure<br />
Black<br />
White

"""

def color(port: int) -> int:
    """Returns the color value of the detected color. Use the `color`
    module to map the color value to a specific color.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def reflection(port: int) -> int:
    """Retrieves the intensity of the reflected light (0-100%).

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def rgbi(port: int) -> tuple[int, int, int, int]:
    """Retrieves the overall color intensity and intensity of red, green
    and blue.
    
    Returns tuple[red: int, green: int, blue: int, intensity: int]

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: tuple
    """

