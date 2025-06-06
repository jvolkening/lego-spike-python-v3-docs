"""
The ``light`` module includes functions to change the color of the light
on the SPIKE Prime hub.

To use the Light module add the following import statement to your
project:

::

   from hub import light

All functions in the module should be called inside the ``light`` module
as a prefix like so:

::

   light.color(color.RED)

The following constants are defined:

* POWER = 1
"""

POWER = 1

def color(light: int, color: int) -> None:
    """
    Change the color of a light on the hub.
    
    ::
    
       from hub import light
       import color
    
       # Change the light to red
       light.color(light.POWER, color.RED)

    :param light: The light on the hub 
    :param color: A color from the ``color`` module 
    :rtype: None
    """

