"""The ``runloop`` module contains all functions and constants to use the
Runloop.

To use the ``runloop`` module, add the following import statement to your
project:

::

    import runloop

All functions in the module should be called inside the ``runloop``
module as a prefix like so:

::

    runloop.run(some_async_function())



The following constants are defined:

* ``WAITING`` = 0
* ``SUCCESS`` = 1
* ``TIMEOUT`` = 2
* ``CANCELLED`` = 3
"""

from typing import Awaitable
from typing import Callable
from typing import Iterator


def run(*functions: Awaitable) -> None:
    """Start any number of parallel ``async`` functions. This is the function
    you should use to create programs with a similar structure to Word Blocks.

    :param functions: A tuple of the functions to run
    :rtype: None
    """


def sleep_ms(duration: int) -> Awaitable:
    """Pause the execution of the application for any amount of milliseconds.

    ::

        from hub import light_matrix
        import runloop

        async def main():
            light_matrix.write("Hi!")
            # Wait for ten seconds
            await runloop.sleep_ms(10000)
            light_matrix.write("Are you still here?")

        runloop.run(main())



    :param duration: The duration in milliseconds
    :rtype: Awaitable
    """


def until(function: Callable[[], bool], timeout: int = 0) -> Awaitable:
    """Returns an awaitable that will return when the condition in the function
    or lambda passed is ``True`` or when it times out.

    ::

        import color_sensor
        import color
        from hub import port
        import runloop

        def is_color_red():
            return color_sensor.color(port.A) is color.RED

        async def main():
            # Wait until Color Sensor sees red
            await runloop.until(is_color_red)
            print("Red!")

        runloop.run(main())



    :param function: A callable with no parameters that returns either
        ``True`` or ``False``. Callable is anything that can be called, so
        a ``def`` or a ``lambda``
    :param timeout: A timeout for the function in milliseconds. If the
        callable does not return ``True`` within the timeout, the ``until``
        still resolves after the timeout. 0 means no timeout, in that case
        it will not resolve until the callable returns ``True``.
    :rtype: Awaitable
    """


def wait(unknown: Iterator) -> Awaitable:
    """Currently undocumented and not understood; use with caution.

    :param unknown: Meaning unknown
    :rtype: Awaitable
    """
