"""The `music` module is used make music in the SPIKE App

To use the `music` module simply import the module like so:

`from app import music`

`music` details

"""

def play_drum(drum: int) -> None:
    """

    :param drum: The drum name. See all available values in the app.sound
    module.
    :type drum: int
    :rtype: None
    """

def play_instrument(instrument: int, note: int, duration: int) -> None:
    """

    :param instrument: The instrument name. See all available values in the
    app.music module.
    :type instrument: int
    :param note: The midi note to play (0-130)
    :type note: int
    :param duration: The duration in milliseconds
    :type duration: int
    :rtype: None
    """

