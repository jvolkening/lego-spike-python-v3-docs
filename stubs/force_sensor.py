def force(port):
	"""Retrieves the measured force as decinewton. Values range from 0 to 100
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def pressed(port):
	"""Tests whether the button on the sensor is pressed. Returns true if the force sensor connected to port is pressed.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype bool
	"""
	pass

def raw(port):
	"""Returns the raw, uncalibrated force value of the force sensor connected on port `port`
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

