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
# -- Description                              | Common Operations for entire Project
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------

import csv

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET
import CompanyPackage.TestCases.conftest as conftest
from Extensions.ExternalFiles.XmlExFiles import XML

'''Function to Explicitly Wait for elements'''
#
#
# def Wait(forElement, elem):
#     if forElement == "elementExists":
#         WebDriverWait(conftest.driver, int(XML.ReadData("WaitTime"))).until(
#             EC.presence_of_element_located((elem[0], elem[1])))
#     elif forElement == "elementDisplayed":
#         WebDriverWait(conftest.driver, int(XML.ReadData("WaitTime"))).until(
#             EC.visibility_of_element_located((elem[0], elem[1])))
#     '''Can be extended here '''
#
#
# '''Enums for different conditions'''
#
#
# # Enum For is for selecting displayed or exist element, my Wait method uses this enum
# class For:
#     elementExists = "elementExists"
#     elementDisplayed = "elementDisplayed"

############################################################################

# continue from here implementing as needed


############################################################################
