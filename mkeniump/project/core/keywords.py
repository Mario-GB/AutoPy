from mkeniump.project.core.navigator import get_navigator
from mkeniump.project.resource.properties.constants import MK_ELEMENT_NAME,\
    MK_ELEMENT_TYPE,\
    MK_ELEMENT_TYPE_VALUE,\
    ERROR_ELEMENT_NOT_FIND
from selenium.webdriver.common.by import By


def driver():
    return get_navigator().get_driver()


# name is the name of element, type is to find this and value is the type's value
    # For example button_one, xpath, //button[@action='submit']
def define(name_element, type_element, value_element):
    if _Element.get_element(name_element=name_element) is not None:
        raise ValueError("Element's name is repeat".format(name_element))#TODO excepcion
    _Element.add(name_element, type_element, value_element)
    return name_element


def define(name_element, value_element):
    return define(name_element=name_element, type_element=By.XPATH, value_element=value_element)


def _will_use(name_element):
    element = _Element.get_element(name_element=name_element)
    if not element.get_is_find():
        element.finda_selenium_element()
    return element.get_selenium_element

def test(**kwargs):
    ---

def my_exceptions(my_ex, **kwargs):
    try:
        for k, v in kwargs.items():
            print(k, v)
    except my_ex:
        pass


class _Element:

    # The first element is None
    elements = {}

    @classmethod
    def get_element(cls, name_element):
        return cls.elements.get(name_element)

    @classmethod
    def add(cls, name_element, type_element, value_element):
        tmp_element = _Element(name_element, type_element, value_element)
        cls.elements.add(
            {tmp_element.get_name(): tmp_element}
        )

    def __init__(self, name_element, type_element, value_element):
        self.name_element = name_element
        self.type_element = type_element
        self.value_element = value_element
        self.is_find = False
        self.selenium_element = None

    def get_name(self):
        return self.name_element

    def get_type(self):
        return self.type_element

    def get_type_value(self):
        return self.value_element

    def get_is_find(self):
        return self.is_find

    def get_selenium_element(self):
        return self.selenium_element

    def find_selenium_element(self):
        self.selenium_element = driver().find_element(by=self.get_type(), value=self.get_type_value())