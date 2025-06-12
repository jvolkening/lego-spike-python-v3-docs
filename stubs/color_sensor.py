"""The ``color_sensor`` module contains functions to interact with an attached Color
Sensor (e.g. LEGO part 45605) and write code that reacts to specific colors or
the intensity of the reflected light.

To use the ``color_sensor`` module, add the following import statement to
your project:

::

    import color_sensor

All functions in the module should be called inside the ``color_sensor``
module as a prefix like so:

::

    color_sensor.reflection(port.A)

The Color Sensor can recognize the following named colors:

* Red
* Green
* Blue
* Magenta
* Yellow
* Orange
* Azure
* Black
* White

It can also return intensity values for the red, green, and blue channels
individually for more control over color recognition.
"""


def color(port: int) -> int:
    """Get the enumerated color value of the detected color. Use the
    ``color`` module to map the color value to a specific color.

    ::

        import color_sensor
        from hub import port
        import color

        if color_sensor.color(port.A) is color.RED:
            print("Red detected")

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: int
    """


def reflection(port: int) -> int:
    """Get the intensity of the reflected light as a percent (0-100).

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: int
    """


def rgbi(port: int) -> tuple[int, int, int, int]:
    """Get the individual intensities of red, green and blue as well as
    the overall intensity, each on a scale of 0-1024.

    Returns tuple[red: int, green: int, blue: int, intensity: int]


    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: tuple
    """
