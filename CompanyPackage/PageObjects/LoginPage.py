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
# -- Description                              | Page Objects that are located on Login Page
# Usage Example
# In the Elements on page section, define variables with tuple structure:
# emailField = (By.ID, "email")
# In class of the page section, define initialization of the new object of that class:
# class LoginPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
# Then define method that returns object of that variable:
#     def GetEmailField(self):
#         return self.driver.find_element(emailField[0], emailField[1])
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

'''Elements on page'''
emailField = (By.ID, "email")
passwordField = (By.ID, "password")
loginButton = (By.XPATH, "//button[@type='submit']")
incorrectMsg = (By.XPATH, "//div[@class='MuiAlert-message css-1xsto0d']")


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def GetEmailField(self):
        return self.driver.find_element(emailField[0], emailField[1])

    def GetPasswordField(self):
        return self.driver.find_element(passwordField[0], passwordField[1])

    def GetLoginBtn(self):
        return self.driver.find_element(loginButton[0], loginButton[1])

    def GetIncorrectMsg(self):
        return self.driver.find_element(incorrectMsg[0], incorrectMsg[1])
