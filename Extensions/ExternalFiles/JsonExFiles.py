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
# -- Description                              | Json External files
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------


import json
import allure


class JSON:

    @staticmethod
    @allure.step("Create JSON file")
    def Create(filePath: str, value: dict):
        with open(filePath, "w") as p:
            json.dump(value, p)


    '''Read existing Json file'''
    @staticmethod
    @allure.step("Read JSON file")
    def Read(filePath: str) -> dict:
        with open(filePath, "r") as reader:
            data = json.load(reader)
        return data


    '''Update values in Json file'''


    # The file must exist
    # before this function specify data values to be changed
    # Example :
    # data = JsonRead(path)
    # data["Salary"]["QA"] = "10000"
    # data["Salary"]["Dev"] = "10000"
    @staticmethod
    @allure.step("Change values in JSON file")
    def ChangeValue(filePath: str, dat):
        JSON.Create(filePath, dat)

############################################################################

# continue from here implementing as needed


############################################################################
