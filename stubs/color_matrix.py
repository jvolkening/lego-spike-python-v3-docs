"""The ``color_matrix`` module contains functions to interact with an attached
3x3 Color Light Matrix (e.g. LEGO part 45608). It enables you to write code
that sets or retrieves the color and intensity of the nine LEDs as a whole or
individually.

To use the ``color_matrix`` module, add the following import statement to
your project:

::

    import color_matrix

All functions in the module should be called inside the ``color_matrix``
module as a prefix like so:

::

    color_matrix.set_pixel(port.A, 1, 1, (color.BLUE, 10))
"""


def clear(port: int) -> None:
    """Turn off all pixels on a Color Matrix

    ::

        from hub import port
        import color_matrix

        color_matrix.clear(port.A)

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :rtype: None
    """


def get_pixel(port: int, x: int, y: int) -> tuple[int, int]:
    """Get the current value of a specific pixel at column X and row Y,
    represented as a tuple containing the color and intensity.

    ::

        from hub import port
        import color_matrix

        # Print the color and intensity of the 0,0 pixel on the Color
        # Matrix connected to port A
        print(color_matrix.get_pixel(port.A, 0, 0))

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :param x: The pixel column, range 0–2
    :param y: The pixel row, range 0–2
    :rtype: tuple
    """


def set_pixel(port: int, x: int, y: int, pixel: tuple[int, int]) -> None:
    """Set the color and intensity of a single pixel at column X and row Y.

    ::

        from hub import port
        import color
        import color_matrix

        # Change the color of the 0,0 pixel on the Color Matrix
        # connected to port A
        color_matrix.set_pixel(port.A, 0, 0, (color.RED, 10))

        # Print the color of the 0,0 pixel on the Color Matrix connected
        # to port A
        print(color_matrix.get_pixel(port.A, 0, 0)[0])

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :param x: The pixel column, range 0–2
    :param y: The pixel row, range 0–2
    :param pixel: A tuple containing color constant and intensity (0–100)
    :rtype: None
    """


def show(port: int, pixels: list[tuple[int, int]]) -> None:
    """Set the color and intensity of all pixels at once on a Color Matrix

    ::

        from hub import port
        import color
        import color_matrix

        # Update all pixels on Color Matrix using the show function

        # Create a list with 18 items (color and intensity pairs)
        pixels = [(color.BLUE, 10)] * 9

        # Update all pixels to show same color and intensity
        color_matrix.show(port.A, pixels)

    :param port: A port from the ``port`` submodule in the ``hub`` module
    :param pixels: A list of tuples specifying color and intensity values for
        all 9 pixels (see `set_pixel()` for a description of the individual
        pixel format)
    :rtype: None
    """
