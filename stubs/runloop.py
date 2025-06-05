"""The `runloop` module contains all functions and constants to use the
Runloop.

To use the Runloop module add the following import statement to your
project:

`import runloop`

All functions in the module should be called inside the `runloop` module as
a prefix like so:

`runloop.run(some_async_function())`

"""

def run(*functions: Awaitable) -> None:
    """Start any number of parallel `async` functions. This is the function
    you should use to create programs with a similar structure to Word
    Blocks.

    :param *functions: The functions to run
    :type *functions: awaitable
    :rtype: None
    """

def sleep_ms(duration: int) -> Awaitable:
    """Pause the execution of the application for any amount of
    milliseconds.

    :param duration: The duration in milliseconds
    :type duration: int
    :rtype: Awaitable
    """

def until(function: Callable[[], bool], timeout: int = 0) -> Awaitable:
    """Returns an awaitable that will return when the condition in the
    function or lambda passed is `True` or when it times out

    :param function: A callable with no parameters that returns either
    `True` or `False`.<br />Callable is anything that can be called, so a
    `def` or a `lambda`
    :type function: callable[[], bool]
    :param timeout: A timeout for the function in milliseconds.<br />If the
    callable does not return `True` within the timeout, the `until` still
    resolves after the timeout.<br />0 means no timeout, in that case it
    will not resolve until the callable returns `True`
    :type timeout: int
    :rtype: Awaitable
    """

