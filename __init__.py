import mkeniump.project.core.navigator as nav
import mkeniump.project.core.keywords as kw
import threading as tr


def demo_telegram():
    driver = nav.get_navigator().get_driver()
    driver.get("https://www.google.com")
    driver.close()


def demo_traza():
    print("demo", tr.current_thread().getName())


def main_method():
    demo_telegram()
    kw.define("searchInput", "//input[@class='gLFyf gsfi']")
    print(kw.get_all_elements())


print("=========================")
main_method()
print("=========================")

