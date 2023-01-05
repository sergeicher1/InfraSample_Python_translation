# ------------------------------------------------------------------------------------------------
# -- coding                                   | utf-8
# -- Author                                   | Sergei Chernyahovsky
# -- Site                                     | http://sergeicher.pro/
# -- Favorite Quote                           | “Always code as if the guy who ends up
#                                                   maintaining your code will be a violent
#                                                       psychopath who knows where you live”
# -- Language                                 | Python
# -- Version                                  | 3.11
# -- WebDriver                                | Selenium
# -- Version                                  | 4.6.0
# -- Description                              | Event Listeners, for online reporting to console
# Usage Example
# In conftest.py -> In InitWebDriver:
# globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
# ------------------------------------------------------------------------------------------------

from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from colorama import Fore, Style


class EventListener(AbstractEventListener):
    button_text = None

    def before_navigate_to(self, url, driver):
        print(f"{Fore.YELLOW}Before Navigating to{Style.RESET_ALL}", url)

    def after_navigate_to(self, url, driver):
        print(f"{Fore.GREEN}After Navigating to{Style.RESET_ALL}", url)

    def before_navigate_back(self, driver):
        print(f"{Fore.YELLOW}Before Navigating Back{Style.RESET_ALL}", driver.current_url)

    def after_navigate_back(self, driver):
        print(f"{Fore.GREEN}After Navigating Back{Style.RESET_ALL}", driver.current_url)

    def before_navigate_forward(self, driver):
        print(f"{Fore.YELLOW}Before Navigating Forward{Style.RESET_ALL}", driver.current_url)

    def after_navigate_forward(self, driver):
        print(f"{Fore.GREEN}After Navigating Forward{Style.RESET_ALL}", driver.current_url)

    def before_find(self, by, value, driver):
        print(f"{Fore.YELLOW}Before Find Element:{Style.RESET_ALL}", value)

    def after_find(self, by, value, driver):
        print(f"{Fore.GREEN}After Find Element{Style.RESET_ALL}", value)

    def before_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print(f"{Fore.YELLOW}Before Change Value {Style.RESET_ALL}", element.get_attribute("value"))
        else:
            print(f"{Fore.YELLOW}Before Change Value {Style.RESET_ALL}", element.text)

    def after_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print(f"{Fore.GREEN}After Change Value {Style.RESET_ALL}", element.get_attribute("value"))
        else:
            print(f"{Fore.GREEN}After Change Value {Style.RESET_ALL}", element.text)

    def before_click(self, element, driver):
        EventListener.button_text = element.get_attribute("value")
        if element.tag_name == "input":
            print(f"{Fore.YELLOW}Before Click {Style.RESET_ALL}", EventListener.button_text)
        else:
            print(f"{Fore.YELLOW}Before Click {Style.RESET_ALL}", EventListener.button_text)

    def after_click(self, element, driver):
        print(f"{Fore.GREEN}After Click {Style.RESET_ALL}", EventListener.button_text)

    def before_execute_script(self, script, driver):
        print(f"{Fore.YELLOW}Before Execute Script {Style.RESET_ALL}", script)

    def after_execute_script(self, script, driver):
        print(f"{Fore.GREEN}After Execute Script {Style.RESET_ALL}", script)

    def before_close(self, driver):
        print(f"{Fore.YELLOW}Before Closing Tab{Style.RESET_ALL}")

    def after_close(self, driver):
        print(f"{Fore.GREEN}After Closing Tab{Style.RESET_ALL}")

    def before_quit(self, driver):
        print(f"{Fore.YELLOW}Before Quiting Session{Style.RESET_ALL}")

    def after_quit(self, driver):
        print(f"{Fore.GREEN}After Quiting Session{Style.RESET_ALL}")

    def on_exception(self, exception, driver):
        print(f"{Fore.RED}On Exception: {Style.RESET_ALL}", exception)
