"""
The ``force_sensor`` module enables you to interact with an attached Force
Sensor (e.g. LEGO part 45606) and write code that reacts to touch events or 
force magnitude.

To use the ``force_sensor`` module, add the following import statement to
your project:

::

   import force_sensor

All functions in the module should be called inside the ``force_sensor``
module as a prefix like so:

::

   force_sensor.force(port.A)

"""

def force(port: int) -> int:
    """
    Retrieves the measured force as decinewton. Values range from 0 to 100
    
    ::
    
       from hub import port
       import force_sensor
    
       print(force_sensor.force(port.A))

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: int
    """

def pressed(port: int) -> bool:
    """
    Tests whether the button on the sensor is pressed. Returns true if the
    force sensor connected to port is pressed.
    
    ::
    
       from hub import port
       import force_sensor
    
       print(force_sensor.pressed(port.A))

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: bool
    """

def raw(port: int) -> int:
    """
    Returns the raw, uncalibrated force value of the force sensor connected
    on port ``port``
    
    ::
    
       from hub import port
       import force_sensor
    
       print(force_sensor.raw(port.A))

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: int
    """

