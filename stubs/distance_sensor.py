def clear(port):
	"""Turns off all the lights in the Distance Sensor connected to `port`.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype None
	"""
	pass

def distance(port):
	"""Retrieve the distance in millimeters captured by the Distance Sensor connected to `port`. If the Distance Sensor cannot read a valid distance it will return -1.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def get_pixel(port, x, y):
	"""Retrieve the intensity of a specific light on the Distance Sensor connected to `port`.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param x: The X value (0 - 3)
	:type x: int
	:param y: The Y value, range (0 - 3)
	:type y: int
	:rtype int
	"""
	pass

def set_pixel(port, x, y, intensity):
	"""Changes the intensity of a specific light on the Distance Sensor connected to `port`.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param x: The X value (0 - 3)
	:type x: int
	:param y: The Y value, range (0 - 3)
	:type y: int
	:param intensity: How bright to light up the pixel
	:type intensity: int
	:rtype None
	"""
	pass

def show(port, pixels):
	"""Change all the lights at the same time.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param pixels: A list containing intensity values for all 4 pixels.
	:type pixels: bytes
	:rtype None
	"""
	pass

