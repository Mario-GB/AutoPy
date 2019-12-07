from xml.dom import minidom
from mkeniump.project.resource.properties.constants import \
    ROUT_PROPERTIES,\
    FILE_NAVIGATOR_CONFIG,\
    FILE_WAITER_CONFIG,\
    NODE_DRIVER,\
    NODE_SCREEN,\
    ATTRIBUTE_HEIGHT,\
    ATTRIBUTE_WIDTH,\
    NODE_DEFAULT_TIME,\
    NODE_LONG_TIME,\
    NODE_SHORT_TIME


def __read(file):
    rout_file = ROUT_PROPERTIES + file
    return minidom.parse(rout_file)


def get_navigator_properties():
    document = __read(FILE_NAVIGATOR_CONFIG)

    type_driver = document.getElementsByTagName(NODE_DRIVER)[0].firstChild.data
    screen = document.getElementsByTagName(NODE_SCREEN)[0]
    screen_width = screen.getAttribute(ATTRIBUTE_WIDTH)
    screen_height = screen.getAttribute(ATTRIBUTE_HEIGHT)

    return {NODE_DRIVER: type_driver, ATTRIBUTE_WIDTH: screen_width, ATTRIBUTE_HEIGHT: screen_height}


def get_waiter_properties():
    document = __read(FILE_WAITER_CONFIG)

    default_time = document.getElementsByTagName(NODE_DEFAULT_TIME)
    long_time = document.getElementsByTagName(NODE_LONG_TIME)
    short_time = document.getElementsByTagName(NODE_SHORT_TIME)

    return {NODE_DEFAULT_TIME: default_time, NODE_LONG_TIME:long_time, NODE_SHORT_TIME:short_time}