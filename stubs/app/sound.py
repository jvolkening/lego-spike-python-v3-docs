"""
The `sound` module is used play sounds in the SPIKE App

To use the `sound` module simply import the module like so:

::

	from app import sound

`sound` details
"""

from typing import Awaitable

def play(sound_name: str, volume: int = 100, pitch: int = 0, pan: int = 0) -> Awaitable:
    """
    Play a sound in the SPIKE App

    :param sound_name: The sound name as seen in the Word Blocks sound
        extension
    :param volume: The volume (0-100)
    :param pitch: The pitch of the sound
    :param pan: The pan effect determines which speaker is emitting the
        sound, with "-100" being only the left speaker, "0" being normal,
        and "100" being only the right speaker.
    :rtype: Awaitable
    """

def set_attributes(volume: int, pitch: int, pan: int) -> None:
    """
    
    :param volume: The volume (0-100)
    :param pitch: The pitch of the sound
    :param pan: The pan effect determines which speaker is emitting the
        sound, with "-100" being only the left speaker, "0" being normal,
        and "100" being only the right speaker.
    :rtype: None
    """

def stop() -> None:
    """
    
    :rtype: None
    """

