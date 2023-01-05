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

from CompanyPackage.PageObjects.home_page import HomePage
from CompanyPackage.PageObjects.login_page import LoginPage
from CompanyPackage.PageObjects.main_page import MainPage
from CompanyPackage.TestCases import conftest

'''Web Objects'''
main_page = None
login_page = None
home_page = None


# upperMenuBar = None


class ManagePages:

    # Initialization of web objects
    @staticmethod
    def InitWebPages():
        globals()["main_page"] = MainPage(conftest.driver)
        globals()["login_page"] = LoginPage(conftest.driver)
        globals()["home_page"] = HomePage(conftest.driver)
