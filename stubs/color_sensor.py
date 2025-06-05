def color(port):
	"""Returns the color value of the detected color. Use the `color` module to map the color value to a specific color.
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def reflection(port):
	"""Retrieves the intensity of the reflected light (0-100%).
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype int
	"""
	pass

def rgbi(port):
	"""Retrieves the overall color intensity and intensity of red, green and blue.
	
	Returns tuple[red: int, green: int, blue: int, intensity: int]
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype tuple
	"""
	pass

