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
# -- Description                              | Page Objects that are located on Main Page
# Usage Example
# In the Elements on page section, define variables with tuple structure:
# iFrame = (By.ID, "sp_message_iframe_742832")
# In class of the page section, define initialization of the new object of that class:
# class MainPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
# Then define method that returns object of that variable:
#     def GetIFrame(self):
#         return self.driver.find_element(iFrame[0], iFrame[1])
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

'''Elements on page'''
loginLink = (
    By.XPATH, "//a[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineNone css-aj6lj0']")
iFrame = (By.ID, "sp_message_iframe_742832")
acceptBtn = (By.XPATH, "//button[@title='ACCEPT']")


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def GetLoginLink(self):
        return self.driver.find_element(loginLink[0], loginLink[1])

    def GetIFrame(self):
        return self.driver.find_element(iFrame[0], iFrame[1])

    def GetAcceptBtn(self):
        return self.driver.find_element(acceptBtn[0], acceptBtn[1])
