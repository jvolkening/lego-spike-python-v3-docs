def clear():
	"""Switches off all of the pixels on the Light Matrix.
	:rtype None
	"""
	pass

def get_orientation():
	"""Retrieve the current orientation of the Light Matrix.<br />
	 Can be used with the following constants: `orientation.UP`, `orientation.LEFT`, `orientation.RIGHT`, `orientation.DOWN`
	:rtype int
	"""
	pass

def get_pixel(x, y):
	"""Retrieve the intensity of a specific pixel on the Light Matrix.
	:param x: The X value, range (0 - 4)
	:type x: int
	:param y: The Y value, range (0 - 4)
	:type y: int
	:rtype int
	"""
	pass

def set_orientation(top):
	"""Change the orientation of the Light Matrix. All subsequent calls will use the new orientation.<br />
	 Can be used with the following constants: `orientation.UP`, `orientation.LEFT`, `orientation.RIGHT`, `orientation.DOWN`
	:param top: The side of the hub to be the top
	:type top: int
	:rtype int
	"""
	pass

def set_pixel(x, y, intensity):
	"""Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.
	:param x: The X value, range (0 - 4)
	:type x: int
	:param y: The Y value, range (0 - 4)
	:type y: int
	:param intensity: How bright to light up the pixel
	:type intensity: int
	:rtype None
	"""
	pass

def show(pixels):
	"""Change all the lights at the same time.
	:param pixels: A list containing light intensity values for all 25 pixels.
	:type pixels: iterable
	:rtype None
	"""
	pass

def show_image(image):
	"""Display one of the built in images on the display.
	:param image: The id of the image to show. The range of available images is 1 to 67. There are consts on the <code>light_matrix</code> module for these.
	:type image: int
	:rtype None
	"""
	pass

def write(text, intensity = 100, time_per_character = 500):
	"""Displays text on the Light Matrix, one letter at a time, scrolling from right to left except if there is a single character to show which will not scroll
	:param text: The text to display
	:type text: str
	:param intensity: How bright to light up the pixel
	:type intensity: int
	:param time_per_character: How long to show each character on the display
	:type time_per_character: int
	:rtype Awaitable
	"""
	pass

