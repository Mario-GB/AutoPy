from mkeniump.project.utils.properties import get_waiter_properties
from mkeniump.project.core.navigator import get_navigator
from selenium.webdriver.support.ui import WebDriverWait as Wdw
from selenium.webdriver.support import expected_conditions as ec
from mkeniump.project.resource.properties.constants import NODE_DEFAULT_TIME,\
    ERROR_UNTIL_FAIL


def get_waiter():
    if _Waiter.single is None:
        _Waiter.single = _Waiter()
    return _Waiter.single


def use_waiter_util(condition):
    get_waiter().until(condition, ERROR_UNTIL_FAIL.format(method=condition))


class _Waiter:

    single = None

    def __init__(self):
        Wdw(
            driver=get_navigator().get_driver(),
            timeout=get_waiter_properties().get(NODE_DEFAULT_TIME)
        )
