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
# -- Description                              | WEB flows (dirty work) for TestCases
# Usage Example
# In class WebFlows, define static methods that contain all the "dirty" work for TestCases:
# Business Flows
#     @staticmethod
#     @allure.step("Login flow")
#     def LoginFlow(email: str, password: str):
#         NavigateToPage("https://www.myfitnesspal.com/")
#         WebFlows.AcceptCookies()
#         UiActions.Click(ManagePages.mainPage.GetLoginLink())
#         UiActions.Clear(ManagePages.loginPage.GetEmailField())
#         UiActions.UpdateText(ManagePages.loginPage.GetEmailField(), email)
#         UiActions.Clear(ManagePages.loginPage.GetPasswordField())
#         UiActions.UpdateText(ManagePages.loginPage.GetPasswordField(), password)
#         UiActions.Click(ManagePages.loginPage.GetLoginBtn())
# ------------------------------------------------------------------------------------------------


from Extensions.webdriver import *
from Extensions.ui_actions import UiActions
from Extensions.verifications import Verifications
from Utilities import manage_pages


# from Utilities.CommonOps import *


class WebFlows:

    # Specific AUT functions
    @staticmethod
    @allure.step("Accept cookies")
    def AcceptCookies():
        i_frame = manage_pages.main_page.GetIFrame()
        conftest.driver.switch_to.frame(i_frame)
        UiActions.Click(manage_pages.main_page.GetAcceptBtn())
        conftest.driver.switch_to.default_content()

    # Business Flows

    @staticmethod
    @allure.step("Login flow")
    def LoginFlow(email: str, password: str):
        WebDriver.NavigateToPage("https://www.myfitnesspal.com/")
        WebFlows.AcceptCookies()
        UiActions.Click(manage_pages.main_page.GetLoginLink())
        UiActions.Clear(manage_pages.login_page.GetEmailField())
        UiActions.UpdateText(manage_pages.login_page.GetEmailField(), email)
        UiActions.Clear(manage_pages.login_page.GetPasswordField())
        UiActions.UpdateText(manage_pages.login_page.GetPasswordField(), password)
        UiActions.Click(manage_pages.login_page.GetLoginBtn())
        sleep(10)

    @staticmethod
    @allure.step("Verify Navigation Bar Elements")
    def VerifyNavBarElements():
        Verifications.SmartAssert(manage_pages.home_page.GetNavBarElems())

    @staticmethod
    @allure.step("Verify adding comments - Data Driven Test")
    def AddCommentsAndVerify(value: str):
        WebDriver.ScrollDown(0, 400)  # Use if there will be a problem with ads showing
        UiActions.Clear(manage_pages.home_page.GetNewsInput())
        UiActions.UpdateText(manage_pages.home_page.GetNewsInput(), value)
        UiActions.Click(manage_pages.home_page.GetShareBtn())
        sleep(0.5)
        actual = manage_pages.home_page.GetLastComment().text
        expected = str(value)
        Verifications.VerifyEquals(actual=actual, expected=expected)
