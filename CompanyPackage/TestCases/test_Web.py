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
# -- Description                              | Test Cases clean -> Using other scripts as helpers
# Usage Example
# Use pytest.fixtures for the desired test configuration:
# @pytest.mark.usefixtures("InitWebDriver")  # Uncomment for UI testing with browser
# @pytest.mark.usefixtures("InitDBConnection")  # Uncomment for SQL
# In class "Test_...." :
# class Test_Web:
# Write your tests "test_...)
#     @allure.title("Test Case 01: Valid Login Flow")
#     @allure.description("This test verifies the login flow")
#     def test_TC01LoginFlow(self):
#         WebFlows.LoginFlow("Sergeicher87@gmail.com", "Qq1@34567890")
#         Verifications.VerifyEquals(actual=ManagePages.homePage.GetHeader().text,
#                                                   expected="Your Daily Summary1")
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# To execute first of all MAKE SURE all imports are from correct Directories
# change URL and SCREEN-PATH  in data.xml
# To RUN all available tests and save the allure report "up 2 folders" in main directory
# In terminal -> navigate to "TestCases" directory and RUN:
#                           pytest -s -v --alluredir ./../allure-results
# To generate local server with allure report
# In terminal -> navigate to main directory and RUN:
#                           allure serve allure-results
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------


import pytest
from CompanyPackage.WorkFlows.Webflows import *
from Extensions.ExternalFiles.CSVExFiles import CSV
from Extensions.ExternalFiles.XmlExFiles import XML
from Extensions.SqlMethods import *
from Extensions.Verifications import Verifications

'''Path to data.xml'''
dataPath = "D:\\pyCharm\\InfrastructureSample\\Configuration\\data.xml"

# list of data for data driven testing
data = CSV.ReadAll(XML.ReadData(dataPath, "CSVLocation"))
testData = []  # Generic testData -> rows and cols from csv file
for i in data:
    for j in i:
        testData.append(j)


@pytest.mark.usefixtures("InitWebDriver")  # Uncomment for UI testing with browser
# @pytest.mark.usefixtures("InitDBConnection")  # Uncomment for SQL
class Test_Web:

    # @pytest.mark.skip("Skipped to save time")
    @allure.title("Test Case 01: Valid Login Flow")
    @allure.description("This test verifies the login flow")
    def test_TC01LoginFlow(self):
        WebFlows.LoginFlow("Sergeicher87@gmail.com", "Qq1@34567890")
        Verifications.VerifyEquals(actual=ManagePages.homePage.GetHeader().text, expected="Your Daily Summary1")

    # @pytest.mark.skip("Skipped to save time")
    @allure.title("Test Case 02: Invalid Login Flow")
    @allure.description("This test verifies Invalid Login flows")
    def test_TC02InvalidLoginFlows(self):
        WebFlows.LoginFlow("ser.cher.com", "12313123")
        Verifications.VerifyEquals(actual=ManagePages.loginPage.GetIncorrectMsg().text,
                                   expected="Incorrect username or password. Please try again.")

    # @pytest.mark.skip("Skipped to save time")
    @allure.title("Test Case 03: Verify Elements in Navigation Bar and check them working")
    @allure.description("This test verifies presence of elements in Navigation Bar and if they work")
    def test_TC03NavBarChecking(self):
        WebFlows.VerifyNavBarElems()

    # @pytest.mark.skip("Skipped to save time")
    @allure.title("Test Case 04: Verify adding comments")
    @allure.description("This test adds comments and verifies them")
    @pytest.mark.parametrize("value", testData)
    def test_TC04AddCommentsAndVerify(self, value):
        WebFlows.AddCommentsAndVerify(value=value)