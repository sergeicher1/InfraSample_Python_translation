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


from Extensions.WebDriverMethods import *
from Extensions.UIActioins import UiActions
from Extensions.Verifications import Verifications
from Utilities import ManagePages
from Utilities.CommonOps import *


class WebFlows:

    # Specific AUT functions
    @staticmethod
    @allure.step("Accept cookies")
    def AcceptCookies():
        iFrame = ManagePages.mainPage.GetIFrame()
        conftest.driver.switch_to.frame(iFrame)
        UiActions.Click(ManagePages.mainPage.GetAcceptBtn())
        conftest.driver.switch_to.default_content()

    # Business Flows

    @staticmethod
    @allure.step("Login flow")
    def LoginFlow(email: str, password: str):
        WD.NavigateToPage("https://www.myfitnesspal.com/")
        WebFlows.AcceptCookies()
        UiActions.Click(ManagePages.mainPage.GetLoginLink())
        UiActions.Clear(ManagePages.loginPage.GetEmailField())
        UiActions.UpdateText(ManagePages.loginPage.GetEmailField(), email)
        UiActions.Clear(ManagePages.loginPage.GetPasswordField())
        UiActions.UpdateText(ManagePages.loginPage.GetPasswordField(), password)
        UiActions.Click(ManagePages.loginPage.GetLoginBtn())
        sleep(10)

    @staticmethod
    @allure.step("Verify Navigation Bar Elements")
    def VerifyNavBarElems():
        Verifications.SmartAssert(ManagePages.homePage.GetNavBarElems())

    @staticmethod
    @allure.step("Verify adding comments - Data Driven Test")
    def AddCommentsAndVerify(value: str):
        # ScrollDown(0, 400) # Use if there will be a problem with ads showing
        UiActions.Clear(ManagePages.homePage.GetNewsInput())
        UiActions.UpdateText(ManagePages.homePage.GetNewsInput(), value)
        UiActions.Click(ManagePages.homePage.GetShareBtn())
        sleep(0.5)
        actual = ManagePages.homePage.GetLastComment().text
        expected = str(value)
        Verifications.VerifyEquals(actual=actual, expected=expected)
