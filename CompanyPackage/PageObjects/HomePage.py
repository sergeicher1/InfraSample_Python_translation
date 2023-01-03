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
# -- Description                              | Page Objects that are located on Home Page
# Usage Example
# In the Elements on page section, define variables with tuple structure:
# header = (By.XPATH, "//div/h1")
# In class of the page section, define initialization of the new object of that class:
# class HomePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
# Then define method that returns object of that variable:
#     def GetHeader(self):
#         return self.driver.find_element(header[0], header[1])
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

'''Elements on page'''
header = (By.XPATH, "//div/h1")
navBarElems = (By.XPATH, "//ul[@id='nav']/li")
home = (By.XPATH, "//a[text()='My Home']")
food = (By.XPATH, "//a[text()='Food']")
exercise = (By.XPATH, "//a[text()='Exercise']")
reports = (By.XPATH, "//a[text()='Reports']")
apps = (By.XPATH, "//a[text()='Apps']")
community = (By.XPATH, "//a[text()='Community']")
blog = (By.XPATH, "//a[text()='Blog']")
premium = (By.XPATH, "//a[text()='Premium']")
newsInput = (By.XPATH, "//textarea[@name='status-update']")
shareBtn = (By.XPATH, "//button[text()='Share']")
lastComment = (By.XPATH, "//p[@data-testid='post-text']")


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def GetHeader(self):
        return self.driver.find_element(header[0], header[1])

    def GetNavBarElems(self):
        return self.driver.find_elements(navBarElems[0], navBarElems[1])

    def GetHome(self):
        return self.driver.find_element(home[0], home[1])

    def GetFood(self):
        return self.driver.find_element(food[0], food[1])

    def GetExercise(self):
        return self.driver.find_element(exercise[0], exercise[1])

    def GetReports(self):
        return self.driver.find_element(reports[0], reports[1])

    def GetApps(self):
        return self.driver.find_element(apps[0], apps[1])

    def GetCommunity(self):
        return self.driver.find_element(community[0], community[1])

    def GetBlog(self):
        return self.driver.find_element(blog[0], blog[1])

    def GetPremium(self):
        return self.driver.find_element(premium[0], premium[1])

    def GetNewsInput(self):
        return self.driver.find_element(newsInput[0], newsInput[1])

    def GetShareBtn(self):
        return self.driver.find_element(shareBtn[0], shareBtn[1])

    def GetLastComment(self):
        return self.driver.find_element(lastComment[0], lastComment[1])
