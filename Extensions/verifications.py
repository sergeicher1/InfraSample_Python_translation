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
# -- Description                              |  Different Verifications(assertions) for entire Project
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------

import allure
from selenium.webdriver.remote.webelement import WebElement
from colorama import Fore
from colorama import Style
from smart_assertions import *


class Verifications:

    @staticmethod
    @allure.step("Equality Verification")  # Fore to print in different colors
    def VerifyEquals(actual, expected):
        assert actual == expected, f"{Fore.RED} Equality Verification FAILED, {Style.RESET_ALL}actual: " + str(
            actual) + f"{Fore.RED} is not Equals to {Style.RESET_ALL}expected: " + str(expected)

    @staticmethod
    @allure.step("Verify if element is displayed on page")
    def VerifyIsDisplayed(elem: WebElement):
        assert elem.is_displayed(), f"{Fore.RED}Verification is FAILED, {Style.RESET_ALL}Element: " + elem.text + f" {Fore.RED}is not displayed!"

    '''Method to append FAILED assertion to list, and check only in the end of test case'''

    @staticmethod
    @allure.step("Soft Assert(Verification) using soft_assert")
    def SmartAssert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step("Verification of amount of elements in table")
    def VerifyAmountOfElements(elems, expectedSize):
        assert len(elems) == expectedSize, "Number of elements in list: " + str(
            len(elems)) + f" {Fore.RED}doesn't match expected size: " + str(expectedSize)

############################################################################

# continue from here implementing as needed


############################################################################
