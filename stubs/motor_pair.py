def move(pair, steering, *, velocity = 360, acceleration = 1000):
	"""Move a Motor Pair at a constant speed until a new command is given.
	:param pair: The pair slot of the Motor Pair.
	:type pair: int
	:param steering: The steering (-100 to 100)
	:type steering: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param velocity: The velocity in degrees/sec
	:type velocity: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:rtype None
	"""
	pass

def move_for_degrees(pair, degrees, steering, *, velocity = 360, stop = motor.BRAKE, acceleration = 1000, deceleration = 1000):
	"""Move a Motor Pair at a constant speed for a specific number of degrees.<br />
	When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:
	
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
	:param velocity: The velocity in degrees/sec
	:type velocity: int
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:param deceleration: The deceleration (deg/sec²) (1 - 10000)
	:type deceleration: int
	:rtype Awaitable
	"""
	pass

def move_for_time(pair, duration, steering, *, velocity = 360, stop = motor.BRAKE, acceleration = 1000, deceleration = 1000):
	"""Move a Motor Pair at a constant speed for a specific duration.<br />
	When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:
	
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
	:param velocity: The velocity in degrees/sec
	:type velocity: int
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:param deceleration: The deceleration (deg/sec²) (1 - 10000)
	:type deceleration: int
	:rtype Awaitable
	"""
	pass

def move_tank(pair, left_velocity, right_velocity, *, acceleration = 1000):
	"""Perform a tank move on a Motor Pair at a constant speed until a new command is given.
	:param pair: The pair slot of the Motor Pair.
	:type pair: int
	:param left_velocity: The velocity (deg/sec) of the left motor.
	:type left_velocity: int
	:param right_velocity: The velocity (deg/sec) of the right motor.
	:type right_velocity: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:rtype None
	"""
	pass

def move_tank_for_degrees(pair, degrees, left_velocity, right_velocity, *, stop = motor.BRAKE, acceleration = 1000, deceleration = 1000):
	"""Perform a tank move on a Motor Pair at a constant speed until a new command is given.<br />
	When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:
	
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
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:param deceleration: The deceleration (deg/sec²) (1 - 10000)
	:type deceleration: int
	:rtype Awaitable
	"""
	pass

def move_tank_for_time(pair, left_velocity, right_velocity, duration, *, stop = motor.BRAKE, acceleration = 1000, deceleration = 1000):
	"""Perform a tank move on a Motor Pair at a constant speed for a specific amount of time.<br />
	When awaited returns a status of the movement that corresponds to one of the following constants from the motor module:
	
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
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:param acceleration: The acceleration (deg/sec²) (1 - 10000)
	:type acceleration: int
	:param deceleration: The deceleration (deg/sec²) (1 - 10000)
	:type deceleration: int
	:rtype Awaitable
	"""
	pass

def pair(pair, left_motor, right_motor):
	"""pair two motors (`left_motor` &amp; `right_motor`) and store the paired motors in `pair`.<br />
	Use `pair` in all subsequent `motor_pair` related function calls.
	:param pair: The pair slot of the Motor Pair.
	:type pair: int
	:param left_motor: The port of the left motor. Use the <code>port</code> submodule in the <code>hub</code> module.
	:type left_motor: int
	:param right_motor: The port of the right motor. Use the <code>port</code> submodule in the <code>hub</code> module.
	:type right_motor: int
	:rtype None
	"""
	pass

def stop(pair, *, stop = motor.BRAKE):
	"""Stops a Motor Pair.
	:param pair: The pair slot of the Motor Pair.
	:type pair: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param stop: The behavior of the Motor after it has stopped. Use the constants in the <code>motor</code> module.
	:type stop: int
	:rtype None
	"""
	pass

def unpair(pair):
	"""Unpair a Motor Pair.
	:param pair: The pair slot of the Motor Pair.
	:type pair: int
	:rtype None
	"""
	pass

