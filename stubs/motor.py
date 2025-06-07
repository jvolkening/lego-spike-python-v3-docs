"""
The ``motor`` module is used to control and query individual motors attached to the
Spike hub.

To use the `motor` module, add the following import statement to your project:

::

   import motor

All functions in the module should be called inside the ``motor`` module
as a prefix like so:

::

   motor.run(port.A, 1000)

The following constants are defined:

* ``READY`` = 0
* ``RUNNING`` = 1
* ``STALLED`` = 2
* ``CANCELLED`` = 3
* ``ERROR`` = 4
* ``DISCONNECTED`` = 5
* ``COAST`` = 0
* ``BRAKE`` = 1
* ``HOLD`` = 2
* ``CONTINUE`` = 3
* ``SMART_COAST`` = 4
* ``SMART_BRAKE`` = 5
* ``CLOCKWISE`` = 0
* ``COUNTERCLOCKWISE`` = 1
* ``SHORTEST_PATH`` = 2
* ``LONGEST_PATH`` = 3

**NOTE**: The ``motor`` module contains several functions that are not
documented in the official LEGO materials. These are marked as
**UNDOCUMENTED** in the function descriptions below. Their behavior has been
determined empirically and they should be used with caution.

"""



from typing import Awaitable

READY = 0
RUNNING = 1
STALLED = 2
CANCELLED = 3
ERROR = 4
DISCONNECTED = 5
COAST = 0
BRAKE = 1
HOLD = 2
CONTINUE = 3
SMART_COAST = 4
SMART_BRAKE = 5
CLOCKWISE = 0
COUNTERCLOCKWISE = 1
SHORTEST_PATH = 2
LONGEST_PATH = 3

def absolute_position(port: int) -> int:
    """
    Get the absolute position of a Motor
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: int
    """

def get_duty_cycle(port: int) -> int:
    """
    Get the pwm of a Motor
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: int
    """

def relative_position(port: int) -> int:
    """
    Get the relative position of a Motor
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: int
    """

def reset_relative_position(port: int, position: int) -> None:
    """
    Change the position used as the offset when using the
    ``run_to_relative_position`` function.
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param position: The degree of the motor 
    :rtype: None
    """

def run(port: int, velocity: int, *, acceleration: int = 1000) -> None:
    """
    Start a Motor at a constant speed
    
    ::
    
       from hub import port
       import motor, time
    
       # Start motor
       motor.run(port.A, 1000)
       
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param velocity: The velocity in degrees/sec; Value ranges depends on
        motor type.; Small motor (essential): -660 to 660 Medium motor:
        -1110 to 1110 Large motor: -1050 to 1050 
    :param acceleration: The acceleration (deg/sec�) (1 - 10000) 
    :rtype: None
    """

def run_for_degrees(port: int, degrees: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    Turn a motor for a specific number of degrees When awaited returns a
    status of the movement that corresponds to one of the following
    constants:
    
    ``motor.READY``  ``motor.RUNNING``  ``motor.STALLED`` 
    ``motor.CANCELED``  ``motor.ERROR``  ``motor.DISCONNECTED``
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param degrees: The number of degrees 
    :param velocity: The velocity in degrees/sec; Value ranges depends on
        motor type.; Small motor (essential): -660 to 660 Medium motor:
        -1110 to 1110 Large motor: -1050 to 1050 
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module.; Possible values are
        ``motor.COAST`` to make the motor coast until a stop
        ``motor.BRAKE`` to brake and continue to brake after stop
        ``motor.HOLD`` to tell the motor to hold it’s position
        ``motor.CONTINUE`` to tell the motor to keep running at whatever
        velocity it’s running at until it gets another command
        ``motor.SMART_COAST`` to make the motor brake until stop and then
        coast and compensate for inaccuracies in the next command
        ``motor.SMART_BRAKE`` to make the motor brake and continue to brake
        after stop and compensate for inaccuracies in the next command 
    :param acceleration: The acceleration (deg/sec�) (1 - 10000) 
    :param deceleration: The deceleration (deg/sec�) (1 - 10000) 
    :rtype: Awaitable
    """

def run_for_time(port: int, duration: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    Run a Motor for a limited amount of time When awaited returns a status
    of the movement that corresponds to one of the following constants:
    
    ``motor.READY``  ``motor.RUNNING``  ``motor.STALLED`` 
    ``motor.ERROR``  ``motor.DISCONNECTED``
    
    ::
    
       from hub import port
       import runloop
       import motor
    
       async def main():
           # Run at 1000 velocity for 1 second
           await motor.run_for_time(port.A, 1000, 1000)
    
           # Run at 280 velocity for 1 second
           await motor_pair.run_for_time(port.A, 1000, 280)
    
           # Run at 280 velocity for 10 seconds with a slow deceleration
           await motor_pair.run_for_time(port.A, 10000, 280, deceleration=10)
    
       runloop.run(main())

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param duration: The duration in milliseconds 
    :param velocity: The velocity in degrees/sec; Value ranges depends on
        motor type.; Small motor (essential): -660 to 660 Medium motor:
        -1110 to 1110 Large motor: -1050 to 1050 
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module.; Possible values are
        ``motor.COAST`` to make the motor coast until a stop
        ``motor.BRAKE`` to brake and continue to brake after stop
        ``motor.HOLD`` to tell the motor to hold it’s position
        ``motor.CONTINUE`` to tell the motor to keep running at whatever
        velocity it’s running at until it gets another command
        ``motor.SMART_COAST`` to make the motor brake until stop and then
        coast and compensate for inaccuracies in the next command
        ``motor.SMART_BRAKE`` to make the motor brake and continue to brake
        after stop and compensate for inaccuracies in the next command 
    :param acceleration: The acceleration (deg/sec�) (1 - 10000) 
    :param deceleration: The deceleration (deg/sec�) (1 - 10000) 
    :rtype: Awaitable
    """

def run_to_absolute_position(port: int, position: int, velocity: int, *, direction: int = SHORTEST_PATH, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    Turn a motor to an absolute position. When awaited returns a status of
    the movement that corresponds to one of the following constants:
    
    ``motor.READY``  ``motor.RUNNING``  ``motor.STALLED`` 
    ``motor.CANCELED``  ``motor.ERROR``  ``motor.DISCONNECTED``
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param position: The degree of the motor 
    :param velocity: The velocity in degrees/sec; Value ranges depends on
        motor type.; Small motor (essential): -660 to 660 Medium motor:
        -1110 to 1110 Large motor: -1050 to 1050 
    :param direction: The direction to turn. Options are:;
        ``motor.CLOCKWISE``  ``motor.COUNTERCLOCKWISE`` 
        ``motor.SHORTEST_PATH``  ``motor.LONGEST_PATH`` 
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module.; Possible values are
        ``motor.COAST`` to make the motor coast until a stop
        ``motor.BRAKE`` to brake and continue to brake after stop
        ``motor.HOLD`` to tell the motor to hold it’s position
        ``motor.CONTINUE`` to tell the motor to keep running at whatever
        velocity it’s running at until it gets another command
        ``motor.SMART_COAST`` to make the motor brake until stop and then
        coast and compensate for inaccuracies in the next command
        ``motor.SMART_BRAKE`` to make the motor brake and continue to brake
        after stop and compensate for inaccuracies in the next command 
    :param acceleration: The acceleration (deg/sec�) (1 - 10000) 
    :param deceleration: The deceleration (deg/sec�) (1 - 10000) 
    :rtype: Awaitable
    """

def run_to_relative_position(port: int, position: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    Turn a motor to a position relative to the current position. When
    awaited returns a status of the movement that corresponds to one of the
    following constants:
    
    ``motor.READY``  ``motor.RUNNING``  ``motor.STALLED`` 
    ``motor.CANCELED``  ``motor.ERROR``  ``motor.DISCONNECTED``
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param position: The degree of the motor 
    :param velocity: The velocity in degrees/sec; Value ranges depends on
        motor type.; Small motor (essential): -660 to 660 Medium motor:
        -1110 to 1110 Large motor: -1050 to 1050 
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module.; Possible values are
        ``motor.COAST`` to make the motor coast until a stop
        ``motor.BRAKE`` to brake and continue to brake after stop
        ``motor.HOLD`` to tell the motor to hold it’s position
        ``motor.CONTINUE`` to tell the motor to keep running at whatever
        velocity it’s running at until it gets another command
        ``motor.SMART_COAST`` to make the motor brake until stop and then
        coast and compensate for inaccuracies in the next command
        ``motor.SMART_BRAKE`` to make the motor brake and continue to brake
        after stop and compensate for inaccuracies in the next command 
    :param acceleration: The acceleration (deg/sec�) (1 - 10000) 
    :param deceleration: The deceleration (deg/sec�) (1 - 10000) 
    :rtype: Awaitable
    """

def set_duty_cycle(port: int, pwm: int) -> None:
    """
    Start a Motor with a specific pwm
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param pwm: The PWM value (-10000-10000) 
    :rtype: None
    """

def stop(port: int, *, stop: int = BRAKE) -> None:
    """
    Stop the motor given by ``port``. If no ``port`` is specified, stop all
    attached motors.
    
    ::
    
       from hub import port
       import motor, time
    
       # Start motor
       motor.run(port.A, 1000)
    
       # Wait for 2 seconds
       time.sleep_ms(2000)
    
       # Stop motor
       motor.stop(port.A)

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module.; Possible values are
        ``motor.COAST`` to make the motor coast until a stop
        ``motor.BRAKE`` to brake and continue to brake after stop
        ``motor.HOLD`` to tell the motor to hold it’s position
        ``motor.CONTINUE`` to tell the motor to keep running at whatever
        velocity it’s running at until it gets another command
        ``motor.SMART_COAST`` to make the motor brake until stop and then
        coast and compensate for inaccuracies in the next command
        ``motor.SMART_BRAKE`` to make the motor brake and continue to brake
        after stop and compensate for inaccuracies in the next command 
    :rtype: None
    """

def velocity(port: int) -> int:
    """
    Get the velocity (deg/sec) of a motor (*NOTE*: empirical testing suggests the
    unit is *not* in deg/sec)
    

    :param port: A port from the ``port`` submodule in the ``hub`` module 
    :rtype: int
    """

def status() -> int:
    """
    **UNDOCUMENTED** Get the motor status as one of :
    ``motor.READY``, ``motor.RUNNING``, ``motor.STALLED``,
    ``motor.CANCELLED``, ``motor.ERROR``, ``motor.DISCONNECTED``. *NOTE*:
    ``motor.run`` does not set status to ``motor.RUNNING``; other ``run_*``
    functions do.
    

    :rtype: int
    """

def info() -> tuple[int, int]:
    """
    **UNDOCUMENTED** Retrieve the device ID and maximum speed of the motor as
    a tuple.
    

    :rtype: tuple[device_id: int, max_speed: int)
    """

