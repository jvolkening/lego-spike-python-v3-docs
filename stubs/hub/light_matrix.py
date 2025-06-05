"""To use the Light Matrix module add the following import statement to
your project:

`from hub import light_matrix`

All functions in the module should be called inside the `light_matrix`
module as a prefix like so:

`light_matrix.write("Hello World")`

"""

def clear() -> None:
    """Switches off all of the pixels on the Light Matrix.

    :rtype: None
    """

def get_orientation() -> int:
    """Retrieve the current orientation of the Light Matrix.<br />
     Can be used with the following constants: `orientation.UP`,
    `orientation.LEFT`, `orientation.RIGHT`, `orientation.DOWN`

    :rtype: int
    """

def get_pixel(x: int, y: int) -> int:
    """Retrieve the intensity of a specific pixel on the Light Matrix.

    :param x: The X value, range (0 - 4)
    :type x: int
    :param y: The Y value, range (0 - 4)
    :type y: int
    :rtype: int
    """

def set_orientation(top: int) -> int:
    """Change the orientation of the Light Matrix. All subsequent calls
    will use the new orientation.<br />
     Can be used with the following constants: `orientation.UP`,
    `orientation.LEFT`, `orientation.RIGHT`, `orientation.DOWN`

    :param top: The side of the hub to be the top
    :type top: int
    :rtype: int
    """

def set_pixel(x: int, y: int, intensity: int) -> None:
    """Sets the brightness of one pixel (one of the 25 LEDs) on the Light
    Matrix.

    :param x: The X value, range (0 - 4)
    :type x: int
    :param y: The Y value, range (0 - 4)
    :type y: int
    :param intensity: How bright to light up the pixel
    :type intensity: int
    :rtype: None
    """

def show(pixels: list[int]) -> None:
    """Change all the lights at the same time.

    :param pixels: A list containing light intensity values for all 25
    pixels.
    :type pixels: iterable
    :rtype: None
    """

def show_image(image: int) -> None:
    """Display one of the built in images on the display.

    :param image: The id of the image to show. The range of available
    images is 1 to 67. There are consts on the `light_matrix` module for
    these.
    :type image: int
    :rtype: None
    """

def write(text: str, intensity: int = 100, time_per_character: int = 500) -> Awaitable:
    """Displays text on the Light Matrix, one letter at a time, scrolling
    from right to left except if there is a single character to show which
    will not scroll

    :param text: The text to display
    :type text: str
    :param intensity: How bright to light up the pixel
    :type intensity: int
    :param time_per_character: How long to show each character on the
    display
    :type time_per_character: int
    :rtype: Awaitable
    """

