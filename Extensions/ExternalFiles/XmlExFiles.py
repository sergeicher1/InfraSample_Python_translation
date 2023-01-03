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
# -- Description                              | XML External files
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------

import allure
import xml.etree.ElementTree as ET


class XML:

    # Parameter   : Name of the attribute in xml file
    # Return value: String
    @staticmethod
    @allure.step("Read data from XML file")
    def ReadData(dataPath: str, name: str) -> str:
        root = ET.parse(dataPath).getroot()
        return root.find(".//" + name).text

############################################################################

# continue from here implementing as needed


############################################################################
