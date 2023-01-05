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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import *

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

if __name__ == '__main__':
    pass
    # driver.get("https://www.google.co.il/")
    # driver.set_window_position(150, 100)
    # driver.set_window_size(1600, 900)
    # print(driver.title)
    # print(driver.page_source)
    # fileName = input("Please enter file name: \n")
    # first = input("Please enter first variable name: \n")
    # resF = input("Please enter value: \n")
    # second = input("Please enter second variable name: \n")
    # resS = input("Please enter value: \n")
    # res = input("Please enter third variable name: \n")
    # resR = input("Please specify the desired function: ")
    # with open(f"D:\\pyCharm\\InfrastructureSample\\{fileName}.py", "a") as test:
    #     test.writelines(
    #         f"{first} = {resF}\n" +
    #         f"{second} = {resS}\n" +
    #         f"{res} = {first} {resR} {second}\n" +
    #         f"print(\"The third variable is: \", res)")
