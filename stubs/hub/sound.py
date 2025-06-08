"""The ``sound`` module includes functions to play sounds from the Spike hub
speaker.

To use the ``sound`` module, add the following import statement to your
project:

::

    from hub import sound

All functions in the module should be called inside the ``sound`` module
as a prefix like so:

::

    sound.stop()

The following constants are defined:

* ``ANY`` = -2
* ``DEFAULT`` = -1
* ``WAVEFORM_SINE`` = 0 *(differs from the official docs)*
* ``WAVEFORM_TRIANGLE`` = 1
* ``WAVEFORM_SQUARE`` = 2
* ``WAVEFORM_SAWTOOTH`` = 3
"""

from typing import Awaitable

ANY = -2
DEFAULT = -1
WAVEFORM_SINE = 0
WAVEFORM_TRIANGLE = 1
WAVEFORM_SQUARE = 2
WAVEFORM_SAWTOOTH = 3


def beep(
    freq: int = 440,
    duration: int = 500,
    volume: int = 100,
    *,
    attack: int = 0,
    decay: int = 0,
    sustain: int = 100,
    release: int = 0,
    transition: int = 10,
    waveform: int = WAVEFORM_SINE,
    channel: int = DEFAULT
) -> Awaitable:
    """Play a tone from the hub.

    :param freq: The frequency to play
    :param duration: The duration in milliseconds
    :param volume: The volume relative to baseline (0–100)
    :param attack: The time taken for initial run-up of level from nil to
        peak, beginning when the key is pressed
    :param decay: The time taken for the subsequent run down from the
        attack level to the designated sustain level
    :param sustain: The level during the main sequence of the sound’s
        duration, until the key is released
    :param release: The time taken for the level to decay from the sustain
        level to zero after the key is released
    :param transition: Time in milliseconds to transition into the sound if
        something is already playing in the channel
    :param waveform: The synthesized waveform. Use one of the constants in
        the ``hub.sound`` module
    :param channel: The desired channel to play on; options are:
        ``sound.DEFAULT`` and ``sound.ANY``
    :rtype: Awaitable
    """


def stop() -> None:
    """Stop all noise from the hub.

    :rtype: None
    """


def volume(volume: int) -> None:
    """Set the baseline volume of the speaker.

    :param volume: The volume (0–100)
    :rtype: None
    """


def sound(unknown) -> None:
    """**UNDOCUMENTED** Plays a sound file from the hub (maybe?).

    :rtype: None
    """
