def play(sound_name, volume = 100, pitch = 0, pan = 0):
	"""Play a sound in the SPIKE App
	:param sound_name: The sound name as seen in the Word Blocks sound extension
	:type sound_name: str
	:param volume: The volume (0-100)
	:type volume: int
	:param pitch: The pitch of the sound
	:type pitch: int
	:param pan: The pan effect determines which speaker is emitting the sound, with "-100" being only the left speaker, "0" being normal, and "100" being only the right speaker.
	:type pan: int
	:rtype Awaitable
	"""
	pass

def set_attributes(volume, pitch, pan):
	"""
	:param volume: The volume (0-100)
	:type volume: int
	:param pitch: The pitch of the sound
	:type pitch: int
	:param pan: The pan effect determines which speaker is emitting the sound, with "-100" being only the left speaker, "0" being normal, and "100" being only the right speaker.
	:type pan: int
	:rtype None
	"""
	pass

def stop():
	"""
	:rtype None
	"""
	pass

