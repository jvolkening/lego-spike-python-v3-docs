"""The ``motion_sensor`` module includes functions to interact with the
internal motion sensor (gyroscope) in the SPIKE hubs.

To use the ``motion_sensor`` module, add the following import statement to
your project:

::

    from hub import motion_sensor

All functions in the module should be called inside the
``motion_sensor`` module as a prefix like so:

::

    motion_sensor.up_face()

The following constants are defined:

* ``TAPPED`` = 0
* ``DOUBLE_TAPPED`` = 1
* ``SHAKEN`` = 2
* ``FALLING`` = 3
* ``UNKNOWN`` = -1
* ``TOP`` = 0 (the SPIKE Prime hub face with the Light Matrix)
* ``FRONT`` = 1 (the SPIKE Prime hub face where the speaker is)
* ``RIGHT`` = 2 (the right side of the SPIKE Prime hub when facing the
    front hub face)
* ``BOTTOM`` = 3 (the side of the SPIKE Prime hub where the battery is)
* ``BACK`` = 4 (the SPIKE Prime hub face with the USB charging port)
* ``LEFT`` = 5 (the left side of the SPIKE Prime hub when facing the front
    hub face)
"""

TAPPED = 0
DOUBLE_TAPPED = 1
SHAKEN = 2
FALLING = 3
UNKNOWN = -1
TOP = 0
FRONT = 1
RIGHT = 2
BOTTOM = 3
BACK = 4
LEFT = 5


def acceleration(raw_unfiltered: bool) -> tuple[int, int, int]:
    """Get a tuple containing x, y & z acceleration values as integers. The
    values are mili G, so 1 / 1000 G.

    :param raw_unfiltered: If we want the data back raw and unfiltered
    :rtype: tuple
    """


def angular_velocity(raw_unfiltered: bool) -> tuple[int, int, int]:
    """Get a tuple containing x, y & z angular velocity values as integers. The
    values are decidegrees per second.

    :param raw_unfiltered: If we want the data back raw and unfiltered
    :rtype: tuple
    """


def gesture() -> int:
    """Get the gesture recognized.

    Possible values are:

    ``motion_sensor.TAPPED``  ``motion_sensor.DOUBLE_TAPPED``
    ``motion_sensor.SHAKEN``  ``motion_sensor.FALLING``
    ``motion_sensor.UNKNOWN``

    :rtype: int
    """


def get_yaw_face() -> int:
    """Get the face of the hub that yaw is relative to. If you put the hub on a
    flat surface with the face returned pointing up, when you rotate the hub
    only the yaw will update ``motion_sensor.TOP`` The SPIKE Prime hub face
    with the USB charging port. ``motion_sensor.FRONT`` The SPIKE Prime hub
    face with the Light Matrix. ``motion_sensor.RIGHT`` The right side of the
    SPIKE Prime hub when facing the front hub face. ``motion_sensor.BOTTOM``
    The side of the SPIKE Prime hub where the battery is.
    ``motion_sensor.BACK`` The SPIKE Prime hub face where the speaker is.
    ``motion_sensor.LEFT`` The left side of the SPIKE Prime hub when facing the
    front hub face.

    :rtype: int
    """


def quaternion() -> tuple[float, float, float, float]:
    """Get the hub orientation quaternion as a tuple[w: float, x: float, y:
    float, z: float].

    :rtype: tuple
    """


def reset_tap_count() -> None:
    """Reset the tap count returned by the ``tap_count`` function.

    :rtype: None
    """


def reset_yaw(angle: int) -> None:
    """Set the yaw angle offset. The angle set will be the new yaw value.

    :rtype: None
    """


def set_yaw_face(up: int) -> bool:
    """Set what hub face is used as the yaw face.If you put the hub on a flat
    surface with this face pointing up, when you rotate the hub only the yaw
    will update.

    :param up: The hub face that should be set as the upwards facing hub
        face. Available values are:

        * ``motion_sensor.TOP`` The SPIKE Prime hub face with the USB
            charging port
        * ``motion_sensor.FRONT`` The SPIKE Prime hub face with the
            Light Matrix
        *  ``motion_sensor.RIGHT`` The right side of the SPIKE Prime
            hub when facing the front hub face
        * ``motion_sensor.BOTTOM`` The side of the SPIKE Prime hub
            where the battery is
        * ``motion_sensor.BACK`` The SPIKE Prime hub face where the speaker is
        * ``motion_sensor.LEFT`` The left side of the SPIKE Prime hub when
            facing the front hub face

    :rtype: bool
    """


def stable() -> bool:
    """Whether or not the hub is resting flat.

    :rtype: bool
    """


def tap_count() -> int:
    """Get the number of taps recognized since the program started or last time
    ``motion_sensor.reset_tap_count()`` was called.

    :rtype: int
    """


def tilt_angles() -> tuple[int, int, int]:
    """Get a tuple containing yaw pitch and roll values as integers. Values are
    decidegrees.

    :rtype: tuple
    """


def up_face() -> int:
    """Get the Hub face that is currently facing up:

    * ``motion_sensor.TOP`` The SPIKE Prime hub face with the USB
        charging port
    * ``motion_sensor.FRONT`` The SPIKE Prime hub face with the
        Light Matrix
    *  ``motion_sensor.RIGHT`` The right side of the SPIKE Prime
        hub when facing the front hub face
    * ``motion_sensor.BOTTOM`` The side of the SPIKE Prime hub
        where the battery is
    * ``motion_sensor.BACK`` The SPIKE Prime hub face where the speaker is
    * ``motion_sensor.LEFT`` The left side of the SPIKE Prime hub when
        facing the front hub face

    :rtype: int
    """
