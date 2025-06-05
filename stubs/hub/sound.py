def beep(freq = 440, duration = 500, volume = 100, *, attack = 0, decay = 0, sustain = 100, release = 0, transition = 10, waveform = WAVEFORM_SINE, channel = DEFAULT):
	"""Plays a beep sound from the hub
	:param freq: The frequency to play
	:type freq: int
	:param duration: The duration in milliseconds
	:type duration: int
	:param volume: The volume (0-100)
	:type volume: int
	:param optional keyword arguments: 
	:type optional keyword arguments: 
	:param attack: The time taken for initial run-up of level from nil to peak, beginning when the key is pressed.
	:type attack: int
	:param decay: The time taken for the subsequent run down from the attack level to the designated sustain level.
	:type decay: int
	:param sustain: The level during the main sequence of the sound's duration, until the key is released.
	:type sustain: int
	:param release: The time taken for the level to decay from the sustain level to zero after the key is released
	:type release: int
	:param transition: time in milliseconds to transition into the sound if something is already playing in the channel
	:type transition: int
	:param waveform: The synthesized waveform. Use one of the constants in the <code>hub.sound</code> module.
	:type waveform: int
	:param channel: The desired channel to play on, options are <code>sound.DEFAULT</code> and <code>sound.ANY</code>
	:type channel: int
	:rtype Awaitable
	"""
	pass

def stop():
	"""Stops all noise from the hub
	:rtype None
	"""
	pass

def volume(volume):
	"""
	:param volume: The volume (0-100)
	:type volume: int
	:rtype None
	"""
	pass

