import os
from selenium import webdriver
from mkeniump.project.utils import log
from mkeniump.project.utils.properties import get_navigator_properties
from mkeniump.project.resource.properties.constants import *


# Get a singlenton navigator
def get_navigator():
    if _Navigator.single is None:
        _Navigator.single = _Navigator()
    return _Navigator.single


class _Navigator:

    # The only object of class
    single = None

    # Attributes of class
    __driver = None

    # Constructor
    # def __init__(self, type_driver):
    #     if type_driver == self.CHROME:
    #         self.driver = webdriver.Chrome()
    #     # elif type_driver == self.FIREFOX:
    #     #     self.driver = webdriver.Firefox('./resource/')
    #
    #     self.driver = webdriver.Remote(
    #         command_executor='http://127.0.0.1:4444/wd/hub',
    #         desired_capabilities=DesiredCapabilities.FIREFOX)
    #     self.driver.session_id = 'c3b95672-66ce-4119-bc00-4ce657c1a213'

    def __init__(self):

        navigator_properties = get_navigator_properties()

        if navigator_properties.get(NODE_DRIVER) == CHROME:
            self.__driver = webdriver.Chrome(ROUT_DRIVERS)
        elif navigator_properties.get(NODE_DRIVER) == FIREFOX:
            print(os.listdir(ROUT_DRIVERS))
            self.__driver = webdriver.Firefox(ROUT_DRIVERS)
        else:
            log.error(ERROR_NAVIGATOR)

        self.__driver.set_window_size(
            navigator_properties.get(ATTRIBUTE_WIDTH),
            navigator_properties.get(ATTRIBUTE_HEIGHT)
        )

    def get_driver(self):
        return self.__driver
