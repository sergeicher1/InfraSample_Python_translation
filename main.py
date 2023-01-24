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
# -- Description                              | # This is a sample Python script for testing #
# Usage Example
# For fast testing features before implementing a complex usage in infrastructure
# ------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)

if __name__ == '__main__':
    pass
