def data(port):
	"""Retrieve the raw LPF-2 data from a device.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype tuple
	"""
	pass

def id(port):
	"""Retrieve the device id of a device. Each device has an id based on its type.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def get_duty_cycle(port):
	"""Retrieve the duty cycle for a device. Returned values is in range 0 to 10000
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def ready(port):
	"""When a device is attached to the hub it might take a short amount of time before it's ready to accept requests.<br />
	Use `ready` to test for the readiness of the attached devices.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype bool
	"""
	pass

def set_duty_cycle(port, duty_cycle):
	"""Set the duty cycle on a device. Range 0 to 10000
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param duty_cycle: The PWM value (0-10000)
	:type duty_cycle: int
	:rtype None
	"""
	pass

