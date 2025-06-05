"""To use the Button module add the following import statement to your
project:

`from hub import button`

All functions in the module should be called inside the `button` module as
a prefix like so:

`button.pressed(button.LEFT)`


The following constants are defined:

* LEFT = 2<br>Right button next to the power button on the SPIKE Prime hub

"""

LEFT = 2<br>Right button next to the power button on the SPIKE Prime hub

def int pressed(button: int) -> int:
    """This module allows you to react to buttons being pressed on the hub.
    You must first import the `button` module to use the buttons.

    :param button: A button from the `button` submodule in the `hub` module
    :type button: int
    :rtype: int
    """

