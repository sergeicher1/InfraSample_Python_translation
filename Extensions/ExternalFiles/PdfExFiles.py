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
# -- Description                              | PDF External files
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------


import PyPDF2
import allure

class PDF:

    @staticmethod
    @allure.step("Read PDF file")
    def Read(filePath: str):
        pdfFileObj = open(filePath, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # printing number of pages in pdf file
        print("Number of pages: ", pdfReader.numPages)
        pageObj = pdfReader.getPage(0)
        textFromPdf = pageObj.extractText()
        pdfFileObj.close()
        return textFromPdf

############################################################################

# continue from here implementing as needed


############################################################################
