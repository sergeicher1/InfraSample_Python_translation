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
# -- Description                              | This is a configuration file for the entire Project
# Usage Example
# In the Objects Initialization section for global usage, define objects:
# driver = None
# action = None
# dbConnector = None
# Then using @pytest.fixture(), define configurations for tests
# ------------------------------------------------------------------------------------------------


import allure
import pytest
import mysql.connector
from datetime import datetime
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Extensions.external_files import XML
from Utilities.event_listeners import EventListener
from Utilities.manage_pages import ManagePages

'''Objects Initialization'''
driver = None
action = None
db_connector = None

'''Path to data.xml'''
dataPath = "D:\\pyCharm\\InfrastructureSample\\Configuration\\data.xml"

'''WebDriver Initialization'''


@pytest.fixture(scope="class")
def InitWebDriver(request):
    # global driver  See if needed
    e_driver = GetWebDriver()
    globals()["driver"] = EventFiringWebDriver(e_driver, EventListener())
    driver = globals()["driver"]
    driver.maximize_window()
    driver.implicitly_wait(int(XML.ReadData(dataPath, "WaitTime")))
    driver.get(XML.ReadData(dataPath, "URL"))
    request.cls.driver = driver
    globals()["action"] = ActionChains(driver)
    ManagePages.InitWebPages()

    yield
    globals()["driver"].quit()


# Checks which browser is requested for execution
def GetWebDriver():
    browser = XML.ReadData(dataPath, "Browser")
    if browser.lower() == "chrome":
        driver = GetChrome()
    elif browser.lower() == "firefox":
        driver = GetFirefox()
    elif browser.lower() == "edge":
        driver = GetEdge()
    else:
        driver = None
        raise Exception("Wrong Input for browser, check configuration in data.xml file!")
    return driver


'''Initialize specific WebDriver'''


def GetChrome():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return chrome_driver


def GetFirefox():
    ff_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return ff_driver


def GetEdge():
    edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return edge_driver


########################################################################################################

'''Database connection'''


# MySQL
@pytest.fixture(scope="class")
def InitMySqlDBConnection(request):  # Open session
    db_connector = mysql.connector.connect(
        host=XML.ReadData(dataPath, "DbHost"),
        database=XML.ReadData(dataPath, "DbName"),
        user=XML.ReadData(dataPath, "DbUser"),
        password=XML.ReadData(dataPath, "DbPassword")
    )
    globals()["dbConnector"] = db_connector
    request.cls.dbConnector = db_connector

    yield
    db_connector.close()  # Close session


########################################################################################################


'''Catch Exceptions Errors and Screenshots'''


# This is exception for API test
# If it is None -> Screenshot will not be captured, because no browser is opened!
def pytest_exception_interact(node, call, report):  # TODO: see if remove node and call
    if report.failed:
        if globals()["driver"] is not None:
            d = datetime.now()
            image = XML.ReadData(dataPath, "ScreenshotPath") + "screenshot_" + str(
                d.strftime("%d.%m.%y %a %H-%M-%S")) + ".png"
            globals()["driver"].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

########################################################################################################
