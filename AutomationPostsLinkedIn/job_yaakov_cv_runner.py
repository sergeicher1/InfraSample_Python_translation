# TODO:  make automation on CV runner: https://www.jobkarov.com/CV/Send-Resume/
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
# -- Description                              | # Automatically sends CV by cv_runner #
# ------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import *
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)
driver.implicitly_wait(10)

# Testing flow of logon send CV automation
if __name__ == '__main__':
    # Login Flow
    driver.get("https://www.jobkarov.com/")
    driver.find_element(By.XPATH, "//span[@class='Link icon-login']").click()
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sergeicher87@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qq1@3456")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    driver.find_element(By.LINK_TEXT, "הפצת קו\"ח").click()
    driver.execute_script("scrollTo(0,1000);")

    # Update common information text Flow
    for i in range(30):
        driver.find_element(By.XPATH, "//input[@name='fname']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@name='fname']").send_keys("Sergei")

    for i in range(30):
        driver.find_element(By.XPATH, "//input[@name='lname']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@name='lname']").send_keys("Chernyahovsky")

    for i in range(30):
        driver.find_element(By.XPATH, "//input[@name='phone']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("0535270505")

    for i in range(30):
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sergeicher87@gmail.com")

    for i in range(30):
        driver.find_element(By.XPATH, "//input[@name='address']").send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//input[@name='address']").send_keys("Haifa")
    driver.find_element(By.XPATH, "//input[@name='address']").send_keys(Keys.ENTER)

    # Update field and jobs flow - change every time
    # el1 = driver.find_element(By.XPATH, "//span[text()=' בחר תפקיד ']").location_once_scrolled_into_view
    action.move_to_element(driver.find_element(By.XPATH, "//span[text()=' בחר תפקיד ']")).perform()
    driver.find_element(By.XPATH, "//span[text()=' בחר תפקיד ']").click()
    driver.find_element(By.XPATH, "//div[@id='WinSelect']/input[@type='text']").send_keys("QA")
    action.move_to_element(driver.find_element(By.XPATH, "//input[@value='2936']")).perform()
    driver.find_element(By.XPATH, "//input[@value='2936']").click()
    driver.find_element(By.XPATH, "//input[@value='2188']").click()
    driver.find_element(By.XPATH, "//input[@value='3806']").click()
    driver.find_element(By.XPATH, "//input[@value='2190']").click()
    driver.find_element(By.XPATH, "//input[@value='2191']").click()
    action.move_to_element(driver.find_element(By.XPATH, "//span[text()='סגור']")).perform()
    driver.find_element(By.XPATH, "//span[text()='סגור']").click()
    sleep(5)
