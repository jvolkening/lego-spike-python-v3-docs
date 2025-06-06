"""
The ``display`` module is used show images in the SPIKE App

To use the ``display`` module simply import the module like so:

::

   from app import display

``display`` details

The following constants are defined:

* IMAGE_ROBOT_1 = 1
* IMAGE_ROBOT_2 = 2
* IMAGE_ROBOT_3 = 3
* IMAGE_ROBOT_4 = 4
* IMAGE_ROBOT_5 = 5
* IMAGE_HUB_1 = 6
* IMAGE_HUB_2 = 7
* IMAGE_HUB_3 = 8
* IMAGE_HUB_4 = 9
* IMAGE_AMUSEMENT_PARK = 10
* IMAGE_BEACH = 11
* IMAGE_HAUNTED_HOUSE = 12
* IMAGE_CARNIVAL = 13
* IMAGE_BOOKSHELF = 14
* IMAGE_PLAYGROUND = 15
* IMAGE_MOON = 16
* IMAGE_CAVE = 17
* IMAGE_OCEAN = 18
* IMAGE_POLAR_BEAR = 19
* IMAGE_PARK = 20
* IMAGE_RANDOM = 21
"""

IMAGE_ROBOT_1 = 1
IMAGE_ROBOT_2 = 2
IMAGE_ROBOT_3 = 3
IMAGE_ROBOT_4 = 4
IMAGE_ROBOT_5 = 5
IMAGE_HUB_1 = 6
IMAGE_HUB_2 = 7
IMAGE_HUB_3 = 8
IMAGE_HUB_4 = 9
IMAGE_AMUSEMENT_PARK = 10
IMAGE_BEACH = 11
IMAGE_HAUNTED_HOUSE = 12
IMAGE_CARNIVAL = 13
IMAGE_BOOKSHELF = 14
IMAGE_PLAYGROUND = 15
IMAGE_MOON = 16
IMAGE_CAVE = 17
IMAGE_OCEAN = 18
IMAGE_POLAR_BEAR = 19
IMAGE_PARK = 20
IMAGE_RANDOM = 21

def hide() -> None:
    """
    
    :rtype: None
    """

def image(image: int) -> None:
    """
    
    :param image: The id of the image to show. The range of available
        images is 1 to 21. There are consts on the ``display`` module for
        these 
    :rtype: None
    """

def show(fullscreen: bool) -> None:
    """
    
    :param fullscreen: Show in full screen 
    :rtype: None
    """

def text(text: str) -> None:
    """
    
    :param text: The text to display 
    :rtype: None
    """

