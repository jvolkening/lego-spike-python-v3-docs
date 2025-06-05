def acceleration(raw_unfiltered):
	"""Returns a tuple containing x, y &amp; z acceleration values as integers. The values are mili G, so 1 / 1000 G
	:param raw_unfiltered: If we want the data back raw and unfiltered
	:type raw_unfiltered: bool
	:rtype tuple
	"""
	pass

def angular_velocity(raw_unfiltered):
	"""Returns a tuple containing x, y &amp; z angular velocity values as integers. The values are decidegrees per second
	:param raw_unfiltered: If we want the data back raw and unfiltered
	:type raw_unfiltered: bool
	:rtype tuple
	"""
	pass

def gesture():
	"""Returns the gesture recognized.
	
	Possible values are:
	
	`motion_sensor.TAPPED`<br />
	`motion_sensor.DOUBLE_TAPPED`<br />
	`motion_sensor.SHAKEN`<br />
	`motion_sensor.FALLING`<br />
	`motion_sensor.UNKNOWN`
	:rtype int
	"""
	pass

def get_yaw_face():
	"""Retrieve the face of the hub that yaw is relative to.<br />
	If you put the hub on a flat surface with the face returned pointing up, when you rotate the hub only the yaw will update<br />
	`motion_sensor.TOP` The SPIKE Prime hub face with the USB charging port.<br />
	`motion_sensor.FRONT` The SPIKE Prime hub face with the Light Matrix.<br />
	`motion_sensor.RIGHT` The right side of the SPIKE Prime hub when facing the front hub face.<br />
	`motion_sensor.BOTTOM` The side of the SPIKE Prime hub where the battery is.<br />
	`motion_sensor.BACK` The SPIKE Prime hub face where the speaker is.<br />
	`motion_sensor.LEFT` The left side of the SPIKE Prime hub when facing the front hub face.
	:rtype int
	"""
	pass

def quaternion():
	"""Returns the hub orientation quaternion as a tuple[w: float, x: float, y: float, z: float].
	:rtype tuple
	"""
	pass

def reset_tap_count():
	"""Reset the tap count returned by the `tap_count` function
	:rtype None
	"""
	pass

def reset_yaw(angle):
	"""Change the yaw angle offset.<br />
	The angle set will be the new yaw value.
	:param angle: 
	:type angle: int
	:rtype None
	"""
	pass

def set_yaw_face(up):
	"""Change what hub face is used as the yaw face.If you put the hub on a flat surface with this face pointing up, when you rotate the hub only the yaw will update
	:param up: The hub face that should be set as the upwards facing hub face.<br>Available values are:
	:type up: int
	:rtype bool
	"""
	pass

def stable():
	"""Whether or not the hub is resting flat.
	:rtype bool
	"""
	pass

def tap_count():
	"""Returns the number of taps recognized since the program started or last time `motion_sensor.reset_tap_count()` was called.
	:rtype int
	"""
	pass

def tilt_angles():
	"""Returns a tuple containing yaw pitch and roll values as integers. Values are decidegrees
	:rtype tuple
	"""
	pass

def up_face():
	"""Returns the Hub face that is currently facing up<br />
	`motion_sensor.TOP` The SPIKE Prime hub face with the USB charging port.<br />
	`motion_sensor.FRONT` The SPIKE Prime hub face with the Light Matrix.<br />
	`motion_sensor.RIGHT` The right side of the SPIKE Prime hub when facing the front hub face.<br />
	`motion_sensor.BOTTOM` The side of the SPIKE Prime hub where the battery is.<br />
	`motion_sensor.BACK` The SPIKE Prime hub face where the speaker is.<br />
	`motion_sensor.LEFT` The left side of the SPIKE Prime hub when facing the front hub face.
	:rtype int
	"""
	pass

