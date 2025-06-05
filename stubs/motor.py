def absolute_position(port):
	"""Get the absolute position of a Motor
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def get_duty_cycle(port):
	"""Get the pwm of a Motor
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def relative_position(port):
	"""Get the relative position of a Motor
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def reset_relative_position(port, position):
	"""Change the position used as the offset when using the `run_to_relative_position` function.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param position: The degree of the motor
	:type position: int
	:rtype None
	"""
	pass

def run(port, velocity, *, acceleration = 1000):
	"""Start a Motor at a constant speed
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param velocity: The velocity in degrees/sec
	:type velocity: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:rtype None
	"""
	pass

def run_for_degrees(port, degrees, velocity, *, stop = BRAKE, acceleration = 1000, deceleration = 1000):
	"""Turn a motor for a specific number of degrees<br />
	When awaited returns a status of the movement that corresponds to one of the following constants:
	
	`motor.READY`<br />
	`motor.RUNNING`<br />
	`motor.STALLED`<br />
	`motor.CANCELED`<br />
	`motor.ERROR`<br />
	`motor.DISCONNECTED`
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param degrees: The number of degrees
	:type degrees: int
	:param velocity: The velocity in degrees/sec
	:type velocity: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:param deceleration: The deceleration (deg/sec²) (1 - 10000)
	:type deceleration: int
	:rtype Awaitable
	"""
	pass

def run_for_time(port, duration, velocity, *, stop = BRAKE, acceleration = 1000, deceleration = 1000):
	"""Run a Motor for a limited amount of time<br />
	When awaited returns a status of the movement that corresponds to one of the following constants:
	
	`motor.READY`<br />
	`motor.RUNNING`<br />
	`motor.STALLED`<br />
	`motor.ERROR`<br />
	`motor.DISCONNECTED`
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param duration: The duration in milliseconds
	:type duration: int
	:param velocity: The velocity in degrees/sec
	:type velocity: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:param deceleration: The deceleration (deg/sec²) (1 - 10000)
	:type deceleration: int
	:rtype Awaitable
	"""
	pass

def run_to_absolute_position(port, position, velocity, *, direction = motor.SHORTEST_PATH, stop = BRAKE, acceleration = 1000, deceleration = 1000):
	"""Turn a motor to an absolute position.<br />
	When awaited returns a status of the movement that corresponds to one of the following constants:
	
	`motor.READY`<br />
	`motor.RUNNING`<br />
	`motor.STALLED`<br />
	`motor.CANCELED`<br />
	`motor.ERROR`<br />
	`motor.DISCONNECTED`
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param position: The degree of the motor
	:type position: int
	:param velocity: The velocity in degrees/sec
	:type velocity: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param direction: The direction to turn.<br>Options are:
	:type direction: int
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:param deceleration: The deceleration (deg/sec²) (1 - 10000)
	:type deceleration: int
	:rtype Awaitable
	"""
	pass

def run_to_relative_position(port, position, velocity, *, stop = BRAKE, acceleration = 1000, deceleration = 1000):
	"""Turn a motor to a position relative to the current position.<br />
	When awaited returns a status of the movement that corresponds to one of the following constants:
	
	`motor.READY`<br />
	`motor.RUNNING`<br />
	`motor.STALLED`<br />
	`motor.CANCELED`<br />
	`motor.ERROR`<br />
	`motor.DISCONNECTED`
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param position: The degree of the motor
	:type position: int
	:param velocity: The velocity in degrees/sec
	:type velocity: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:param deceleration: The deceleration (deg/sec²) (1 - 10000)
	:type deceleration: int
	:rtype Awaitable
	"""
	pass

def set_duty_cycle(port, pwm):
	"""Start a Motor with a specific pwm
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param pwm: The PWM value (-10000-10000)
	:type pwm: int
	:rtype None
	"""
	pass

def stop(port, *, stop = BRAKE):
	"""Stops a motor
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:rtype None
	"""
	pass

def velocity(port):
	"""Get the velocity (deg/sec) of a Motor
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

