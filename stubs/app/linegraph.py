"""
The ``linegraph`` module is used make line graphs in the SPIKE App

To use the ``linegraph`` module simply import the module like so:

::

   from app import linegraph

``linegraph`` details

"""

from typing import Awaitable

def clear(color: int) -> None:
    """
    
    :param color: A color from the ``color`` module 
    :rtype: None
    """

def clear_all() -> None:
    """
    
    :rtype: None
    """

def get_average(color: int) -> Awaitable:
    """
    
    :param color: A color from the ``color`` module 
    :rtype: Awaitable
    """

def get_last(color: int) -> Awaitable:
    """
    
    :param color: A color from the ``color`` module 
    :rtype: Awaitable
    """

def get_max(color: int) -> Awaitable:
    """
    
    :param color: A color from the ``color`` module 
    :rtype: Awaitable
    """

def get_min(color: int) -> Awaitable:
    """
    
    :param color: A color from the ``color`` module 
    :rtype: Awaitable
    """

def hide() -> None:
    """
    
    :rtype: None
    """

def plot(color: int, x: float, y: float) -> None:
    """
    
    :param color: A color from the ``color`` module 
    :param x: The X value 
    :param y: The Y value 
    :rtype: None
    """

def show(fullscreen: bool) -> None:
    """
    
    :param fullscreen: Show in full screen 
    :rtype: None
    """

