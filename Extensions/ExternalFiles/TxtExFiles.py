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
# -- Description                              | Plain text (.txt) External files
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------

import allure


class Text:

    @staticmethod
    @allure.step("Adds text to txt file, creates new if file doesn't exist")
    def Add(filePath: str, data: str):
        with open(filePath, "a") as file:
            file.writelines(data)
            file.write("\n")


    '''Read text file, File must exist'''

    @staticmethod
    @allure.step("Reads text file")
    def Read(filePath: str):
        with open(filePath, "r") as file:
            text = file.read()
        return text

############################################################################

# continue from here implementing as needed


############################################################################
