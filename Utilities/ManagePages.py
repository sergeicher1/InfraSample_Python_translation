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
# -- Description                              | Managing pages with their Page Objects
# Usage Example
# In Web Objects section, define global objects:
# mainPage = None
# In class ManagePages, initialize web objects:
# class ManagePages:
#     Initialization of web objects
#     @staticmethod
#     def InitWebPages():
#         globals()["mainPage"] = MainPage(conftest.driver)
# ------------------------------------------------------------------------------------------------

from CompanyPackage.PageObjects.HomePage import HomePage
from CompanyPackage.PageObjects.LoginPage import LoginPage
from CompanyPackage.PageObjects.MainPage import MainPage
from CompanyPackage.TestCases import conftest

'''Web Objects'''
mainPage = None
loginPage = None
homePage = None


# upperMenuBar = None


class ManagePages:

    # Initialization of web objects
    @staticmethod
    def InitWebPages():
        globals()["mainPage"] = MainPage(conftest.driver)
        globals()["loginPage"] = LoginPage(conftest.driver)
        globals()["homePage"] = HomePage(conftest.driver)