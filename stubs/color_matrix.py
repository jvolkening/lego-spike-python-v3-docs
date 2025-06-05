def clear(port):
	"""Turn off all pixels on a Color Matrix
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:rtype None
	"""
	pass

def get_pixel(port, x, y):
	"""Retrieve a specific pixel represented as a tuple containing the color and intensity
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param x: The X value (0 - 2)
	:type x: int
	:param y: The Y value, range (0 - 2)
	:type y: int
	:rtype tuple
	"""
	pass

def set_pixel(port, x, y, pixel):
	"""Change a single pixel on a Color Matrix
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param x: The X value (0 - 2)
	:type x: int
	:param y: The Y value, range (0 - 2)
	:type y: int
	:param pixel: Tuple containing color and intensity, meaning how bright to light up the pixel
	:type pixel: tuple[color: int, intensity: int]
	:rtype None
	"""
	pass

def show(port, pixels]):
	"""Change all pixels at once on a Color Matrix
	:param port: A port from the <code>port</code> submodule in the <code>hub</code> module
	:type port: int
	:param pixels: A list containing color and intensity value tuples for all 9 pixels.
	:type pixels: list[tuple[int, int]]
	:rtype None
	"""
	pass

