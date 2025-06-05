def run(*functions):
	"""Start any number of parallel `async` functions. This is the function you should use to create programs with a similar structure to Word Blocks.
	:param *functions: The functions to run
	:type *functions: awaitable
	:rtype None
	"""
	pass

def sleep_ms(duration):
	"""Pause the execution of the application for any amount of milliseconds.
	:param duration: The duration in milliseconds
	:type duration: int
	:rtype Awaitable
	"""
	pass

def until(function, bool], timeout = 0):
	"""Returns an awaitable that will return when the condition in the function or lambda passed is `True` or when it times out
	:param function: A callable with no parameters that returns either <code>True</code> or <code>False</code>.<br>Callable is anything that can be called, so a <code>def</code> or a <code>lambda</code>
	:type function: callable[[], bool]
	:param timeout: A timeout for the function in milliseconds.<br>If the callable does not return <code>True</code> within the timeout, the <code>until</code> still resolves after the timeout.<br>0 means no timeout, in that case it will not resolve until the callable returns <code>True</code>
	:type timeout: int
	:rtype Awaitable
	"""
	pass

