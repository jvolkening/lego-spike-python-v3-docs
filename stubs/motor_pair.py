"""The `motor_pair` module is used to run motors in a synchronized fashion.
This mode is optimal for creating drivebases where you'd want a pair of
motors to start and stop at the same time.

To use the `motor_pair` module simply import the module like so:

`import motor_pair`

All functions in the module should be called inside the `motor_pair` module
as a prefix like so:

`motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)`

"""

def move(pair: int, steering: int, *, velocity: int = 360, acceleration: int = 1000) -> None:
    """Move a Motor Pair at a constant speed until a new command is given.

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :param steering: The steering (-100 to 100)
    :type steering: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param velocity: The velocity in degrees/secValue ranges depends on
    motor type.Small motor (essential): -660 to 660<br />Medium motor:
    -1110 to 1110<br />Large motor: -1050 to 1050
    :type velocity: int
    :param acceleration: The acceleration (deg/secï¿½) (1 - 10000)
    :type acceleration: int
    :rtype: None
    """

def move_for_degrees(pair: int, degrees: int, steering: int, *, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """Move a Motor Pair at a constant speed for a specific number of
    degrees.<br />
    When awaited returns a status of the movement that corresponds to one
    of the following constants from the motor module:
    
    `motor.READY`<br />
    `motor.RUNNING`<br />
    `motor.STALLED`<br />
    `motor.CANCELED`<br />
    `motor.ERROR`<br />
    `motor.DISCONNECTED`

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :param degrees: The number of degrees
    :type degrees: int
    :param steering: The steering (-100 to 100)
    :type steering: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param velocity: The velocity in degrees/secValue ranges depends on
    motor type.Small motor (essential): -660 to 660<br />Medium motor:
    -1110 to 1110<br />Large motor: -1050 to 1050
    :type velocity: int
    :param stop: The behavior of the Motor after it has stopped. Use the
    constants in the `motor` module.Possible values are<br />`motor.COAST`
    to make the motor coast until a stop<br />`motor.BRAKE` to brake and
    continue to brake after stop<br />`motor.HOLD` to tell the motor to
    hold it's position<br />`motor.CONTINUE` to tell the motor to keep
    running at whatever velocity it's running at until it gets another
    command<br />`motor.SMART_COAST` to make the motor brake until stop and
    then coast and compensate for inaccuracies in the next command<br
    />`motor.SMART_BRAKE` to make the motor brake and continue to brake
    after stop and compensate for inaccuracies in the next command
    :type stop: int
    :param acceleration: The acceleration (deg/secï¿½) (1 - 10000)
    :type acceleration: int
    :param deceleration: The deceleration (deg/secï¿½) (1 - 10000)
    :type deceleration: int
    :rtype: Awaitable
    """

def move_for_time(pair: int, duration: int, steering: int, *, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """Move a Motor Pair at a constant speed for a specific duration.<br />
    When awaited returns a status of the movement that corresponds to one
    of the following constants from the motor module:
    
    `motor.READY`<br />
    `motor.RUNNING`<br />
    `motor.STALLED`<br />
    `motor.CANCELED`<br />
    `motor.ERROR`<br />
    `motor.DISCONNECTED`

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :param duration: The duration in milliseconds
    :type duration: int
    :param steering: The steering (-100 to 100)
    :type steering: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param velocity: The velocity in degrees/secValue ranges depends on
    motor type.Small motor (essential): -660 to 660<br />Medium motor:
    -1110 to 1110<br />Large motor: -1050 to 1050
    :type velocity: int
    :param stop: The behavior of the Motor after it has stopped. Use the
    constants in the `motor` module.Possible values are<br />`motor.COAST`
    to make the motor coast until a stop<br />`motor.BRAKE` to brake and
    continue to brake after stop<br />`motor.HOLD` to tell the motor to
    hold it's position<br />`motor.CONTINUE` to tell the motor to keep
    running at whatever velocity it's running at until it gets another
    command<br />`motor.SMART_COAST` to make the motor brake until stop and
    then coast and compensate for inaccuracies in the next command<br
    />`motor.SMART_BRAKE` to make the motor brake and continue to brake
    after stop and compensate for inaccuracies in the next command
    :type stop: int
    :param acceleration: The acceleration (deg/secï¿½) (1 - 10000)
    :type acceleration: int
    :param deceleration: The deceleration (deg/secï¿½) (1 - 10000)
    :type deceleration: int
    :rtype: Awaitable
    """

def move_tank(pair: int, left_velocity: int, right_velocity: int, *, acceleration: int = 1000) -> None:
    """Perform a tank move on a Motor Pair at a constant speed until a new
    command is given.

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :param left_velocity: The velocity (deg/sec) of the left motor.
    :type left_velocity: int
    :param right_velocity: The velocity (deg/sec) of the right motor.
    :type right_velocity: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param acceleration: The acceleration (deg/secï¿½) (1 - 10000)
    :type acceleration: int
    :rtype: None
    """

def move_tank_for_degrees(pair: int, degrees: int, left_velocity: int, right_velocity: int, *, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """Perform a tank move on a Motor Pair at a constant speed until a new
    command is given.<br />
    When awaited returns a status of the movement that corresponds to one
    of the following constants from the motor module:
    
    `motor.READY`<br />
    `motor.RUNNING`<br />
    `motor.STALLED`<br />
    `motor.CANCELED`<br />
    `motor.ERROR`<br />
    `motor.DISCONNECTED`

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :param degrees: The number of degrees
    :type degrees: int
    :param left_velocity: The velocity (deg/sec) of the left motor.
    :type left_velocity: int
    :param right_velocity: The velocity (deg/sec) of the right motor.
    :type right_velocity: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param stop: The behavior of the Motor after it has stopped. Use the
    constants in the `motor` module.Possible values are<br />`motor.COAST`
    to make the motor coast until a stop<br />`motor.BRAKE` to brake and
    continue to brake after stop<br />`motor.HOLD` to tell the motor to
    hold it's position<br />`motor.CONTINUE` to tell the motor to keep
    running at whatever velocity it's running at until it gets another
    command<br />`motor.SMART_COAST` to make the motor brake until stop and
    then coast and compensate for inaccuracies in the next command<br
    />`motor.SMART_BRAKE` to make the motor brake and continue to brake
    after stop and compensate for inaccuracies in the next command
    :type stop: int
    :param acceleration: The acceleration (deg/secï¿½) (1 - 10000)
    :type acceleration: int
    :param deceleration: The deceleration (deg/secï¿½) (1 - 10000)
    :type deceleration: int
    :rtype: Awaitable
    """

def move_tank_for_time(pair: int, left_velocity: int, right_velocity: int, duration: int, *, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """Perform a tank move on a Motor Pair at a constant speed for a
    specific amount of time.<br />
    When awaited returns a status of the movement that corresponds to one
    of the following constants from the motor module:
    
    `motor.READY`<br />
    `motor.RUNNING`<br />
    `motor.STALLED`<br />
    `motor.CANCELED`<br />
    `motor.ERROR`<br />
    `motor.DISCONNECTED`

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :param duration: The duration in milliseconds
    :type duration: int
    :param left_velocity: The velocity (deg/sec) of the left motor.
    :type left_velocity: int
    :param right_velocity: The velocity (deg/sec) of the right motor.
    :type right_velocity: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param stop: The behavior of the Motor after it has stopped. Use the
    constants in the `motor` module.Possible values are<br />`motor.COAST`
    to make the motor coast until a stop<br />`motor.BRAKE` to brake and
    continue to brake after stop<br />`motor.HOLD` to tell the motor to
    hold it's position<br />`motor.CONTINUE` to tell the motor to keep
    running at whatever velocity it's running at until it gets another
    command<br />`motor.SMART_COAST` to make the motor brake until stop and
    then coast and compensate for inaccuracies in the next command<br
    />`motor.SMART_BRAKE` to make the motor brake and continue to brake
    after stop and compensate for inaccuracies in the next command
    :type stop: int
    :param acceleration: The acceleration (deg/secï¿½) (1 - 10000)
    :type acceleration: int
    :param deceleration: The deceleration (deg/secï¿½) (1 - 10000)
    :type deceleration: int
    :rtype: Awaitable
    """

def pair(pair: int, left_motor: int, right_motor: int) -> None:
    """pair two motors (`left_motor` &amp; `right_motor`) and store the
    paired motors in `pair`.<br />
    Use `pair` in all subsequent `motor_pair` related function calls.

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :param left_motor: The port of the left motor. Use the `port` submodule
    in the `hub` module.
    :type left_motor: int
    :param right_motor: The port of the right motor. Use the `port`
    submodule in the `hub` module.
    :type right_motor: int
    :rtype: None
    """

def stop(pair: int, *, stop: int = motor.BRAKE) -> None:
    """Stops a Motor Pair.

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param stop: The behavior of the Motor after it has stopped. Use the
    constants in the `motor` module.Possible values are<br />`motor.COAST`
    to make the motor coast until a stop<br />`motor.BRAKE` to brake and
    continue to brake after stop<br />`motor.HOLD` to tell the motor to
    hold it's position<br />`motor.CONTINUE` to tell the motor to keep
    running at whatever velocity it's running at until it gets another
    command<br />`motor.SMART_COAST` to make the motor brake until stop and
    then coast and compensate for inaccuracies in the next command<br
    />`motor.SMART_BRAKE` to make the motor brake and continue to brake
    after stop and compensate for inaccuracies in the next command
    :type stop: int
    :rtype: None
    """

def unpair(pair: int) -> None:
    """Unpair a Motor Pair.

    :param pair: The pair slot of the Motor Pair.
    :type pair: int
    :rtype: None
    """

