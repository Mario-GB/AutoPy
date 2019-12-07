from mkeniump.project.core.navigator import Navigator
import mkeniump.project.core.keywords as kw
import threading as tr


def demo_telegram():
    driver = Navigator.get_navigator().get_driver()
    driver.get("https://www.google.com")
    driver.close()



def demo_traza():
    print("demo", tr.current_thread().getName())


def main_method():
    kw.define("hola", "a", "b")
    kw.define("hola2", "a2", "b2")
    kw.get_all_elemenst()


print("=========================")
main_method()
print("=========================")

