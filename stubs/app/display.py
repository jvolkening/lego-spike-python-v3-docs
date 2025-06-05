"""The `display` module is used show images in the SPIKE App

To use the `display` module simply import the module like so:

`from app import display`

`display` details

"""

def hide() -> None:
    """

    :rtype: None
    """

def image(image: int) -> None:
    """

    :param image: The id of the image to show. The range of available
    images is 1 to 21. There are consts on the `display` module for these
    :type image: int
    :rtype: None
    """

def show(fullscreen: bool) -> None:
    """

    :param fullscreen: Show in full screen
    :type fullscreen: bool
    :rtype: None
    """

def text(text: str) -> None:
    """

    :param text: The text to display
    :type text: str
    :rtype: None
    """

