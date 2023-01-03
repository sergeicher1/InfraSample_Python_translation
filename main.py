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
# -- Description                              | # This is a sample Python script for testing #
# Usage Example
# For fast testing features before implementing a complex usage in infrastructure
# ------------------------------------------------------------------------------------------------

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from Extensions.ExternalFiles.CSVExFiles import CSV
from Extensions.ExternalFiles.TxtExFiles import Text
from Extensions.ExternalFiles.DocxExFiles import Docx
from Extensions.ExternalFiles.PdfExFiles import PDF
from Extensions.ExternalFiles.XlExFiles import Excel
from Extensions.MongoDBMethods import MongoDB
from Extensions.SqlMethods import SQL
from Extensions.WebDriverMethods import WD

if __name__ == '__main__':
    pass
