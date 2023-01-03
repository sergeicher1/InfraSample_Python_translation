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
# -- Description                              | CSV External files
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------


import csv
import allure


class CSV:

    @staticmethod
    @allure.step("CSV ReadAll")
    def ReadAll(filePath: str):
        result = []
        with open(filePath, mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                result.insert(len(result), lines)
            return result

    '''Write to CSV file'''
    @staticmethod
    @allure.step("CSV Write to file")
    def WriteTo(filePath: str, fields: list, rows: list):
        with open(filePath, 'w') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow(fields)
            csvWriter.writerows(rows)

############################################################################

# continue from here implementing as needed

############################################################################
