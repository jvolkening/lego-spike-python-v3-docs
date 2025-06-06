"""
The `bargraph` module is used make bar graphs in the SPIKE App

To use the `bargraph` module simply import the module like so:

::

	from app import bargraph

`bargraph` details
"""

from typing import Awaitable

def change(color: int, value: float) -> None:
    """
    
    :param color: A color from the `color` module
    :param value: The value
    :rtype: None
    """

def clear_all() -> None:
    """
    
    :rtype: None
    """

def get_value(color: int) -> Awaitable:
    """
    
    :param color: A color from the `color` module
    :rtype: Awaitable
    """

def hide() -> None:
    """
    
    :rtype: None
    """

def set_value(color: int, value: float) -> None:
    """
    
    :param color: A color from the `color` module
    :param value: The value
    :rtype: None
    """

def show(fullscreen: bool) -> None:
    """
    
    :param fullscreen: Show in full screen
    :rtype: None
    """

