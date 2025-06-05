"""To use a Motor add the following import statement to your project:

`import motor`

All functions in the module should be called inside the `motor` module as a
prefix like so:

`motor.run(port.A, 1000)`

"""

def absolute_position(port: int) -> int:
    """Get the absolute position of a Motor

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def get_duty_cycle(port: int) -> int:
    """Get the pwm of a Motor

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def relative_position(port: int) -> int:
    """Get the relative position of a Motor

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

def reset_relative_position(port: int, position: int) -> None:
    """Change the position used as the offset when using the
    `run_to_relative_position` function.

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param position: The degree of the motor
    :type position: int
    :rtype: None
    """

def run(port: int, velocity: int, *, acceleration: int = 1000) -> None:
    """Start a Motor at a constant speed

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param velocity: The velocity in degrees/secValue ranges depends on
    motor type.Small motor (essential): -660 to 660<br />Medium motor:
    -1110 to 1110<br />Large motor: -1050 to 1050
    :type velocity: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param acceleration: The acceleration (deg/secï¿½) (1 - 10000)
    :type acceleration: int
    :rtype: None
    """

def run_for_degrees(port: int, degrees: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """Turn a motor for a specific number of degrees<br />
    When awaited returns a status of the movement that corresponds to one
    of the following constants:
    
    `motor.READY`<br />
    `motor.RUNNING`<br />
    `motor.STALLED`<br />
    `motor.CANCELED`<br />
    `motor.ERROR`<br />
    `motor.DISCONNECTED`

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param degrees: The number of degrees
    :type degrees: int
    :param velocity: The velocity in degrees/secValue ranges depends on
    motor type.Small motor (essential): -660 to 660<br />Medium motor:
    -1110 to 1110<br />Large motor: -1050 to 1050
    :type velocity: int
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

def run_for_time(port: int, duration: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """Run a Motor for a limited amount of time<br />
    When awaited returns a status of the movement that corresponds to one
    of the following constants:
    
    `motor.READY`<br />
    `motor.RUNNING`<br />
    `motor.STALLED`<br />
    `motor.ERROR`<br />
    `motor.DISCONNECTED`

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param duration: The duration in milliseconds
    :type duration: int
    :param velocity: The velocity in degrees/secValue ranges depends on
    motor type.Small motor (essential): -660 to 660<br />Medium motor:
    -1110 to 1110<br />Large motor: -1050 to 1050
    :type velocity: int
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

def run_to_absolute_position(port: int, position: int, velocity: int, *, direction: int = motor.SHORTEST_PATH, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """Turn a motor to an absolute position.<br />
    When awaited returns a status of the movement that corresponds to one
    of the following constants:
    
    `motor.READY`<br />
    `motor.RUNNING`<br />
    `motor.STALLED`<br />
    `motor.CANCELED`<br />
    `motor.ERROR`<br />
    `motor.DISCONNECTED`

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param position: The degree of the motor
    :type position: int
    :param velocity: The velocity in degrees/secValue ranges depends on
    motor type.Small motor (essential): -660 to 660<br />Medium motor:
    -1110 to 1110<br />Large motor: -1050 to 1050
    :type velocity: int
    :param optional keyword arguments: 
    :type optional keyword arguments: 
    :param direction: The direction to turn.<br />Options
    are:`motor.CLOCKWISE`<br />`motor.COUNTERCLOCKWISE`<br
    />`motor.SHORTEST_PATH`<br />`motor.LONGEST_PATH`
    :type direction: int
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

def run_to_relative_position(port: int, position: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """Turn a motor to a position relative to the current position.<br />
    When awaited returns a status of the movement that corresponds to one
    of the following constants:
    
    `motor.READY`<br />
    `motor.RUNNING`<br />
    `motor.STALLED`<br />
    `motor.CANCELED`<br />
    `motor.ERROR`<br />
    `motor.DISCONNECTED`

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param position: The degree of the motor
    :type position: int
    :param velocity: The velocity in degrees/secValue ranges depends on
    motor type.Small motor (essential): -660 to 660<br />Medium motor:
    -1110 to 1110<br />Large motor: -1050 to 1050
    :type velocity: int
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

def set_duty_cycle(port: int, pwm: int) -> None:
    """Start a Motor with a specific pwm

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :param pwm: The PWM value (-10000-10000)
    :type pwm: int
    :rtype: None
    """

def stop(port: int, *, stop: int = BRAKE) -> None:
    """Stops a motor

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
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

def velocity(port: int) -> int:
    """Get the velocity (deg/sec) of a Motor

    :param port: A port from the `port` submodule in the `hub` module
    :type port: int
    :rtype: int
    """

