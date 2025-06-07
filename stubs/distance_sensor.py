"""
The ``distance_sensor`` module enables you to interact with an attached
Distance Sensor (e.g. LEGO part 45604) and write code that reacts to
specific distances or lights up the sensor LEDs in different ways.

To use the ``distance_sensor`` module, add the following import statement to
your project:

::

   import distance_sensor

All functions in the module should be called inside the ``distance_sensor``
module as a prefix like so:

::

   distance_sensor.distance(port.A)
"""

def clear(port: int) -> None:
    """
    Turns off all the lights in the Distance Sensor connected to ``port``.
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: None
    """

def distance(port: int) -> int:
    """
    Retrieve the distance in millimeters captured by the Distance Sensor
    connected to ``port``. If the Distance Sensor cannot read a valid
    distance it will return -1.
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: int
    """

def get_pixel(port: int, x: int, y: int) -> int:
    """
    Retrieve the intensity of a specific light on the Distance Sensor
    connected to ``port``.
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param x: The X value (0 - 1) 
    :param y: The Y value, range (0 - 1) 
    :rtype: int
    """

def set_pixel(port: int, x: int, y: int, intensity: int) -> None:
    """
    Changes the intensity of a specific light on the Distance Sensor
    connected to ``port``.
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param x: The X value (0 - 1) 
    :param y: The Y value, range (0 - 1) 
    :param intensity: How bright to light up the pixel 
    :rtype: None
    """

def show(port: int, pixels: list[int]) -> None:
    """
    Change all the lights at the same time.
    
    ::
    
       from hub import port
       import distance_sensor
    
       # Update all pixels on Distance Sensor using the show function
    
       # Create a list with 4 identical intensity values
       pixels = [100] * 4
    
       # Update all pixels to show same intensity
       distance_sensor.show(port.A, pixels)

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param pixels: A list containing intensity values for all 4 pixels. 
    :rtype: None
    """

