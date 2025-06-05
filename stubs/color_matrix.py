"""To use the Color Matrix module add the following import statement to
your project:

`import color_matrix`

All functions in the module should be called inside the `color_matrix`
module as a prefix like so:

`color_matrix.set_pixel(port.A, 1, 1, (color.BLUE, 10))`

"""

def clear(port: int) -> None:
    """Turn off all pixels on a Color Matrix

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: None
    """

def get_pixel(port: int, x: int, y: int) -> tuple[int, int]:
    """Retrieve a specific pixel represented as a tuple containing the
    color and intensity

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param x: The X value (0 - 2)
    :type x: int
    :param y: The Y value, range (0 - 2)
    :type y: int
    :rtype: tuple
    """

def set_pixel(port: int, x: int, y: int, pixel: tuple[color: int, intensity: int]) -> None:
    """Change a single pixel on a Color Matrix

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param x: The X value (0 - 2)
    :type x: int
    :param y: The Y value, range (0 - 2)
    :type y: int
    :param pixel: Tuple containing color and intensity, meaning how bright
    to light up the pixel
    :type pixel: tuple[color: int, intensity: int]
    :rtype: None
    """

def show(port: int, pixels: list[tuple[int, int]]) -> None:
    """Change all pixels at once on a Color Matrix

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param pixels: A list containing color and intensity value tuples for
    all 9 pixels.
    :type pixels: list[tuple[int, int]]
    :rtype: None
    """

