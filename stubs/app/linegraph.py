"""The `linegraph` module is used make line graphs in the SPIKE App

To use the `linegraph` module simply import the module like so:

`from app import linegraph`

`linegraph` details

"""

from typing import Awaitable

def clear(color: int) -> None:
    """

    :param color: A color from the `color` module
    :type color: int
    :rtype: None
    """

def clear_all() -> None:
    """

    :rtype: None
    """

async def get_average(color: int) -> Awaitable:
    """

    :param color: A color from the `color` module
    :type color: int
    :rtype: Awaitable
    """

async def get_last(color: int) -> Awaitable:
    """

    :param color: A color from the `color` module
    :type color: int
    :rtype: Awaitable
    """

async def get_max(color: int) -> Awaitable:
    """

    :param color: A color from the `color` module
    :type color: int
    :rtype: Awaitable
    """

async def get_min(color: int) -> Awaitable:
    """

    :param color: A color from the `color` module
    :type color: int
    :rtype: Awaitable
    """

def hide() -> None:
    """

    :rtype: None
    """

def plot(color: int, x: float, y: float) -> None:
    """

    :param color: A color from the `color` module
    :type color: int
    :param x: The X value
    :type x: float
    :param y: The Y value
    :type y: float
    :rtype: None
    """

def show(fullscreen: bool) -> None:
    """

    :param fullscreen: Show in full screen
    :type fullscreen: bool
    :rtype: None
    """

