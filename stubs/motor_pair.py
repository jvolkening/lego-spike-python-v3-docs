"""The ``motor_pair`` module is used to run motors in a synchronized fashion.
This mode is optimal for creating drivebases where you'd want a pair of motors
to start and stop at the same time.

To use the ``motor_pair`` module, add the following import statement to your
project:

::

    import motor_pair

All functions in the module should be called inside the ``motor_pair``
module as a prefix like so:

::

    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

The following constants are defined:

* ``PAIR_1`` = 0
* ``PAIR_2`` = 1
* ``PAIR_3`` = 2
"""

from typing import Awaitable
import motor

PAIR_1 = 0
PAIR_2 = 1
PAIR_3 = 2


def move(
    pair: int, steering: int, *, velocity: int = 360, acceleration: int = 1000
) -> None:
    """Move a Motor Pair at a constant speed until a new command is given.

    ::

        from hub import port
        import runloop
        import motor_pair

        async def main():
            # Pair motors on port A and B
            motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

            await runloop.sleep_ms(2000)

            # Move straight at default velocity
            motor_pair.move(motor_pair.PAIR_1, 0)

            await runloop.sleep_ms(2000)

            # Move straight at a specific velocity
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)

            await runloop.sleep_ms(2000)

            # Move straight at a specific velocity and acceleration
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=280,
                acceleration=100)

        runloop.run(main())

    :param pair: The pair slot of the Motor Pair
    :param steering: The steering (-100 to 100)
    :param velocity: The velocity in degrees/sec; Value ranges depends on
        motor type: Small motor (essential): -660 to 660; Medium motor:
        -1110 to 1110; Large motor: -1050 to 1050
    :param acceleration: The acceleration (deg/sec²) (1–10000)
    :rtype: None
    """


def move_for_degrees(
    pair: int,
    degrees: int,
    steering: int,
    *,
    velocity: int = 360,
    stop: int = motor.BRAKE,
    acceleration: int = 1000,
    deceleration: int = 1000
) -> Awaitable:
    """Move a Motor Pair at a constant speed for a specific number of degrees.
    When awaited, returns a status of the movement that corresponds to one of
    the following constants from the motor module:

    * ``motor.READY``
    * ``motor.RUNNING``
    * ``motor.STALLED``
    * ``motor.CANCELED``
    * ``motor.ERROR``
    * ``motor.DISCONNECTED``

    ::

        from hub import port
        import runloop
        import motor_pair

        async def main():
            # Pair motors on port A and B
            motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

            # Move straight at default velocity for 90 degrees
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0)

            # Move straight at a specific velocity
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0,
                velocity=280)

            # Move straight at a specific velocity with a slow deceleration
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0,
                velocity=280, deceleration=10)

        runloop.run(main())

    :param pair: The pair slot of the Motor Pair
    :param degrees: The number of degrees
    :param steering: The steering (-100 to 100)
    :param velocity: The velocity in degrees/sec; Value ranges depends on
        motor type: Small motor (essential): -660 to 660; Medium motor:
        -1110 to 1110; Large motor: -1050 to 1050.
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module. Possible values are:

        * ``motor.COAST`` to make the motor coast until a stop
        * ``motor.BRAKE`` to brake and continue to brake after stop
        * ``motor.HOLD`` to tell the motor to hold it's position
        * ``motor.CONTINUE`` to tell the motor to keep running at whatever \
            velocity it's running at until it gets another command
        * ``motor.SMART_COAST`` to make the motor brake until stop and then \
            coast and compensate for inaccuracies in the next command
        * ``motor.SMART_BRAKE`` to make the motor brake and continue to brake \
            after stop and compensate for inaccuracies in the next command

    :param acceleration: The acceleration (deg/sec²) (1–10000)
    :param deceleration: The deceleration (deg/sec²) (1–10000)
    :rtype: Awaitable
    """


def move_for_time(
    pair: int,
    duration: int,
    steering: int,
    *,
    velocity: int = 360,
    stop: int = motor.BRAKE,
    acceleration: int = 1000,
    deceleration: int = 1000
) -> Awaitable:
    """Move a Motor Pair at a constant speed for a specific duration. When
    awaited, returns a status of the movement that corresponds to one of the
    following constants from the motor module:

    * ``motor.READY``
    * ``motor.RUNNING``
    * ``motor.STALLED``
    * ``motor.CANCELED``
    * ``motor.ERROR``
    * ``motor.DISCONNECTED``

    ::

        from hub import port
        import runloop
        import motor_pair

        async def main():
            # Pair motors on port A and B
            motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

            # Move straight at default velocity for 1 second
            await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0)

            # Move straight at a specific velocity for 1 second
            await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0,
                velocity=280)

            # Move straight at a specific velocity for 10 seconds with a slow
            # deceleration
            await motor_pair.move_for_time(motor_pair.PAIR_1, 10000, 0,
                velocity=280, deceleration=10)

        runloop.run(main())

    :param pair: The pair slot of the Motor Pair
    :param duration: The duration in milliseconds
    :param steering: The steering (-100 to 100)
    :param velocity: The velocity in degrees/sec; value ranges depends on
        motor type: Small motor (essential): -660 to 660; Medium motor:
        -1110 to 1110; Large motor: -1050 to 1050.
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module. Possible values are:

        * ``motor.COAST`` to make the motor coast until a stop
        * ``motor.BRAKE`` to brake and continue to brake after stop
        * ``motor.HOLD`` to tell the motor to hold it's position
        * ``motor.CONTINUE`` to tell the motor to keep running at whatever \
            velocity it's running at until it gets another command
        * ``motor.SMART_COAST`` to make the motor brake until stop and then \
            coast and compensate for inaccuracies in the next command
        * ``motor.SMART_BRAKE`` to make the motor brake and continue to brake \
            after stop and compensate for inaccuracies in the next command

    :param acceleration: The acceleration (deg/sec²) (1–10000)
    :param deceleration: The deceleration (deg/sec²) (1–10000)
    :rtype: Awaitable
    """


def move_tank(
    pair: int,
    left_velocity: int,
    right_velocity: int,
    *,
    acceleration: int = 1000
) -> None:
    """Perform a tank move on a Motor Pair at a constant speed until a new
    command is given.

    ::

        from hub import port
        import runloop
        import motor_pair

        async def main():
            # Pair motors on port A and B
            motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

            # Move straight at default velocity
            motor_pair.move_tank(motor_pair.PAIR_1, 1000, 1000)

            await runloop.sleep_ms(2000)

            # Turn right
            motor_pair.move_tank(motor_pair.PAIR_1, 0, 1000)

            await runloop.sleep_ms(2000)

            # Perform tank turn
            motor_pair.move_tank(motor_pair.PAIR_1, 1000, -1000)

        runloop.run(main())

    :param pair: The pair slot of the Motor Pair
    :param left_velocity: The velocity (deg/sec) of the left motor
    :param right_velocity: The velocity (deg/sec) of the right motor
    :param acceleration: The acceleration (deg/sec²) (1–10000)
    :rtype: None
    """


def move_tank_for_degrees(
    pair: int,
    degrees: int,
    left_velocity: int,
    right_velocity: int,
    *,
    stop: int = motor.BRAKE,
    acceleration: int = 1000,
    deceleration: int = 1000
) -> Awaitable:
    """Perform a tank move on a Motor Pair for a specific number of degrees.
    When awaited, returns a status of the movement that
    corresponds to one of the following constants from the motor module:

    * ``motor.READY``
    * ``motor.RUNNING``
    * ``motor.STALLED``
    * ``motor.CANCELED``
    * ``motor.ERROR``
    * ``motor.DISCONNECTED``

    ::

        from hub import port
        import runloop
        import motor_pair

        async def main():
            # Pair motors on port A and B
            motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

            # Move straight at default velocity for 360 degrees
            await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360,
                1000, 1000)

            # Turn right for 180 degrees
            await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180,
                0, 1000)

            # Perform tank turn for 720 degrees
            await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 720,
                1000, -1000)

        runloop.run(main())

    :param pair: The pair slot of the Motor Pair
    :param degrees: The number of degrees
    :param left_velocity: The velocity (deg/sec) of the left motor
    :param right_velocity: The velocity (deg/sec) of the right motor
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module. Possible values are:

        * ``motor.COAST`` to make the motor coast until a stop
        * ``motor.BRAKE`` to brake and continue to brake after stop
        * ``motor.HOLD`` to tell the motor to hold it's position
        * ``motor.CONTINUE`` to tell the motor to keep running at whatever \
            velocity it's running at until it gets another command
        * ``motor.SMART_COAST`` to make the motor brake until stop and then \
            coast and compensate for inaccuracies in the next command
        * ``motor.SMART_BRAKE`` to make the motor brake and continue to brake \
            after stop and compensate for inaccuracies in the next command

    :param acceleration: The acceleration (deg/sec²) (1–10000)
    :param deceleration: The deceleration (deg/sec²) (1–10000)
    :rtype: Awaitable
    """


def move_tank_for_time(
    pair: int,
    left_velocity: int,
    right_velocity: int,
    duration: int,
    *,
    stop: int = motor.BRAKE,
    acceleration: int = 1000,
    deceleration: int = 1000
) -> Awaitable:
    """Perform a tank move on a Motor Pair for a specific
    amount of time. When awaited, returns a status of the movement that
    corresponds to one of the following constants from the motor module:

    * ``motor.READY``
    * ``motor.RUNNING``
    * ``motor.STALLED``
    * ``motor.CANCELED``
    * ``motor.ERROR``
    * ``motor.DISCONNECTED``

    ::

        from hub import port
        import runloop
        import motor_pair

        async def main():
            # Pair motors on port A and B
            motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

            # Move straight at default velocity for 1 second
            await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000,
                1000, 1000)

            # Turn right for 3 seconds
            await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0,
                1000, 3000)

            # Perform tank turn for 2 seconds
            await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000,
                -1000, 2000)

        runloop.run(main())

    :param pair: The pair slot of the Motor Pair
    :param duration: The duration in milliseconds
    :param left_velocity: The velocity (deg/sec) of the left motor
    :param right_velocity: The velocity (deg/sec) of the right motor
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module. Possible values are:

        * ``motor.COAST`` to make the motor coast until a stop
        * ``motor.BRAKE`` to brake and continue to brake after stop
        * ``motor.HOLD`` to tell the motor to hold it's position
        * ``motor.CONTINUE`` to tell the motor to keep running at whatever \
            velocity it's running at until it gets another command
        * ``motor.SMART_COAST`` to make the motor brake until stop and then \
            coast and compensate for inaccuracies in the next command
        * ``motor.SMART_BRAKE`` to make the motor brake and continue to brake \
            after stop and compensate for inaccuracies in the next command

    :param acceleration: The acceleration (deg/sec²) (1–10000)
    :param deceleration: The deceleration (deg/sec²) (1–10000)
    :rtype: Awaitable
    """


def pair(pair: int, left_motor: int, right_motor: int) -> None:
    """Pair two motors (``left_motor`` & ``right_motor``) and store the paired
    motors in ``pair``. Use ``pair`` in all subsequent ``motor_pair``-related
    function calls.

    ::

        import motor_pair
        from hub import port

        motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    :param pair: The pair slot of the Motor Pair
    :param left_motor: The port of the left motor. Use the ``port``
        submodule in the ``hub`` module.
    :param right_motor: The port of the right motor. Use the ``port``
        submodule in the ``hub`` module.
    :rtype: None
    """


def stop(pair: int, *, stop: int = motor.BRAKE) -> None:
    """Stop a Motor Pair.

    ::

        import motor_pair

        motor_pair.stop(motor_pair.PAIR_1)

    :param pair: The pair slot of the Motor Pair
    :param stop: The behavior of the Motor after it has stopped. Use the
        constants in the ``motor`` module. Possible values are:

        * ``motor.COAST`` to make the motor coast until a stop
        * ``motor.BRAKE`` to brake and continue to brake after stop
        * ``motor.HOLD`` to tell the motor to hold it's position
        * ``motor.CONTINUE`` to tell the motor to keep running at whatever \
            velocity it's running at until it gets another command
        * ``motor.SMART_COAST`` to make the motor brake until stop and then \
            coast and compensate for inaccuracies in the next command
        * ``motor.SMART_BRAKE`` to make the motor brake and continue to brake \
            after stop and compensate for inaccuracies in the next command

    :rtype: None
    """


def unpair(pair: int) -> None:
    """Unpair a Motor Pair.

    ::

        import motor_pair

        motor_pair.unpair(motor_pair.PAIR_1)

    :param pair: The pair slot of the Motor Pair
    :rtype: None
    """
