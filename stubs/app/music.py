"""
The ``music`` module is used make music in the SPIKE App

To use the ``music`` module simply import the module like so:

::

   from app import music

``music`` details

The following constants are defined:

* ``DRUM_BASS`` = 2
* ``DRUM_BONGO`` = 13
* ``DRUM_CABASA`` = 15
* ``DRUM_CLAVES`` = 9
* ``DRUM_CLOSED_HI_HAT`` = 6
* ``DRUM_CONGA`` = 14
* ``DRUM_COWBELL`` = 11
* ``DRUM_CRASH_CYMBAL`` = 4
* ``DRUM_CUICA`` = 18
* ``DRUM_GUIRO`` = 16
* ``DRUM_HAND_CLAP`` = 8
* ``DRUM_OPEN_HI_HAT`` = 5
* ``DRUM_SIDE_STICK`` = 3
* ``DRUM_SNARE`` = 1
* ``DRUM_TAMBOURINE`` = 7
* ``DRUM_TRIANGLE`` = 12
* ``DRUM_VIBRASLAP`` = 17
* ``DRUM_WOOD_BLOCK`` = 10
* ``INSTRUMENT_BASS`` = 6
* ``INSTRUMENT_BASSOON`` = 14
* ``INSTRUMENT_CELLO`` = 8
* ``INSTRUMENT_CHOIR`` = 15
* ``INSTRUMENT_CLARINET`` = 10
* ``INSTRUMENT_ELECTRIC_GUITAR`` = 5
* ``INSTRUMENT_ELECTRIC_PIANO`` = 2
* ``INSTRUMENT_FLUTE`` = 12
* ``INSTRUMENT_GUITAR`` = 4
* ``INSTRUMENT_MARIMBA`` = 19
* ``INSTRUMENT_MUSIC_BOX`` = 17
* ``INSTRUMENT_ORGAN`` = 3
* ``INSTRUMENT_PIANO`` = 1
* ``INSTRUMENT_PIZZICATO`` = 7
* ``INSTRUMENT_SAXOPHONE`` = 11
* ``INSTRUMENT_STEEL_DRUM`` = 18
* ``INSTRUMENT_SYNTH_LEAD`` = 20
* ``INSTRUMENT_SYNTH_PAD`` = 21
* ``INSTRUMENT_TROMBONE`` = 9
* ``INSTRUMENT_VIBRAPHONE`` = 16
* ``INSTRUMENT_WOODEN_FLUTE`` = 13
"""

DRUM_BASS = 2
DRUM_BONGO = 13
DRUM_CABASA = 15
DRUM_CLAVES = 9
DRUM_CLOSED_HI_HAT = 6
DRUM_CONGA = 14
DRUM_COWBELL = 11
DRUM_CRASH_CYMBAL = 4
DRUM_CUICA = 18
DRUM_GUIRO = 16
DRUM_HAND_CLAP = 8
DRUM_OPEN_HI_HAT = 5
DRUM_SIDE_STICK = 3
DRUM_SNARE = 1
DRUM_TAMBOURINE = 7
DRUM_TRIANGLE = 12
DRUM_VIBRASLAP = 17
DRUM_WOOD_BLOCK = 10
INSTRUMENT_BASS = 6
INSTRUMENT_BASSOON = 14
INSTRUMENT_CELLO = 8
INSTRUMENT_CHOIR = 15
INSTRUMENT_CLARINET = 10
INSTRUMENT_ELECTRIC_GUITAR = 5
INSTRUMENT_ELECTRIC_PIANO = 2
INSTRUMENT_FLUTE = 12
INSTRUMENT_GUITAR = 4
INSTRUMENT_MARIMBA = 19
INSTRUMENT_MUSIC_BOX = 17
INSTRUMENT_ORGAN = 3
INSTRUMENT_PIANO = 1
INSTRUMENT_PIZZICATO = 7
INSTRUMENT_SAXOPHONE = 11
INSTRUMENT_STEEL_DRUM = 18
INSTRUMENT_SYNTH_LEAD = 20
INSTRUMENT_SYNTH_PAD = 21
INSTRUMENT_TROMBONE = 9
INSTRUMENT_VIBRAPHONE = 16
INSTRUMENT_WOODEN_FLUTE = 13

def play_drum(drum: int) -> None:
    """
    
    :param drum: The drum name. See all available values in the app.sound
        module. 
    :rtype: None
    """

def play_instrument(instrument: int, note: int, duration: int) -> None:
    """
    
    :param instrument: The instrument name. See all available values in the
        app.music module. 
    :param note: The midi note to play (0-130) 
    :param duration: The duration in milliseconds 
    :rtype: None
    """

