"""
The ``hub`` package is home to all of the modules used to interact with
various integrated inputs (gyroscope, buttons) and outputs (lights, sound) on
a Spike Hub (e.g. LEGO parts 45601 or 45609). This package also contains the
`hub` module with several direct functions used to interrogate and control the
hub itself.

To use the ``hub`` module itself, add the following import statement to
your project:

::

   import hub

All functions in the module should be called inside the ``hub``
module as a prefix like so:

::

   t = hub.temperature()

**NOTE**: The ``hub`` module contains a number of functions that are not
documented in the official LEGO materials. These are marked as
**UNDOCUMENTED** in the function descriptions below. Their behavior has been
determined empirically and they should be used with caution.

"""

def device_uuid() -> str:
    """
    Retrieves the device id.
    

    :rtype: str
    """

def hardware_id() -> str:
    """
    Retrieves the hardware id.
    

    :rtype: str
    """

def power_off() -> int:
    """
    Turns off the hub.
    

    :rtype: int
    """

def temperature() -> int:
    """
    Retrieves the hub temperature. Measured in decidegrees celsius (d�C)
    which is 1 / 10 of a degree celsius (�C)
    

    :rtype: int
    """

def soft_reset() -> int:
    """
    **UNDOCUMENTED** Sends a soft reset command to the hub.

    :rtype: int
    """

def reset() -> int:
    """
    **UNDOCUMENTED** Sends a hard reset command to the hub.

    :rtype: int
    """

def bootloader() -> int:
    """
    **UNDOCUMENTED** Retrieves the hub bootloader.

    :rtype: int
    """

def battery_voltage() -> int:
    """
    **UNDOCUMENTED** Retrieves the battery voltage.

    :rtype: int
    """

def battery_temperature() -> int:
    """
    **UNDOCUMENTED** Retrieves the battery temperature.

    :rtype: int
    """

def battery_current() -> int:
    """
    **UNDOCUMENTED** Retrieves the battery current.

    :rtype: int
    """

def usb_charge_current() -> int:
    """
    **UNDOCUMENTED** Retrieves the USB charge current.

    :rtype: int
    """
