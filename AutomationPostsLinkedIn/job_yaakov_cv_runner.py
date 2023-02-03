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
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from time import *

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)
driver.implicitly_wait(10)
driver.delete_all_cookies()


def StartBrowser():
    # Login Flow
    driver.get("https://www.jobkarov.com/")
    driver.find_element(By.XPATH, "//span[@class='Link icon-login']").click()
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sergeicher87@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qq1@3456")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    driver.find_element(By.LINK_TEXT, "הפצת קו\"ח").click()
    driver.execute_script("scrollTo(0,1000);")


def CloseBrowser():
    global driver
    driver.quit()


def UpdateInfo():
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


def UpdateJobs():
    # Update jobs flow
    action.move_to_element(
        driver.find_element(By.XPATH, "//*[@id='CVEditor']/form/div[2]/div/p[1]/button/span")).perform()
    driver.find_element(By.XPATH, "//*[@id='CVEditor']/form/div[2]/div/p[1]/button/span").click()
    driver.find_element(By.XPATH, "//div[@id='WinSelect']/input[@type='text']").send_keys("QA")
    # action.move_to_element(driver.find_element(By.XPATH, "//input[@value='2936']")).click().perform()
    driver.find_element(By.XPATH, "//input[@value='2936']").click()
    driver.find_element(By.XPATH, "//input[@value='2188']").click()
    driver.find_element(By.XPATH, "//input[@value='3806']").click()
    driver.find_element(By.XPATH, "//input[@value='2190']").click()
    driver.find_element(By.XPATH, "//input[@value='2191']").click()
    action.move_to_element(driver.find_element(By.XPATH, "//span[text()='סגור']")).click().perform()


def OpenFields():
    # Open fields
    action.move_to_element(
        driver.find_element(By.XPATH, "//*[@id='CVEditor']/form/div[2]/div/p[2]/button/span")).perform()
    driver.find_element(By.XPATH, "//*[@id='CVEditor']/form/div[2]/div/p[2]/button/span").click()


def CloseFields():
    # Close fields
    action.move_to_element(driver.find_element(By.XPATH, "//span[text()='סגור']")).click().perform()
    driver.execute_script("scrollTo(0,500);")


def FirstFields():
    # First run
    driver.find_element(By.XPATH, "//input[@value='15']").click()
    driver.find_element(By.XPATH, "//input[@value='16']").click()
    driver.find_element(By.XPATH, "//input[@value='17']").click()
    driver.find_element(By.XPATH, "//input[@value='18']").click()
    driver.find_element(By.XPATH, "//input[@value='19']").click()
    driver.find_element(By.XPATH, "//input[@value='20']").click()


def SecondFields():
    # Second run
    driver.find_element(By.XPATH, "//input[@value='31']").click()
    driver.find_element(By.XPATH, "//input[@value='32']").click()
    driver.find_element(By.XPATH, "//input[@value='33']").click()
    driver.find_element(By.XPATH, "//input[@value='34']").click()
    driver.find_element(By.XPATH, "//input[@value='35']").click()
    driver.find_element(By.XPATH, "//input[@value='36']").click()


def ThirdFields():
    # Third run
    driver.find_element(By.XPATH, "//input[@value='37']").click()
    driver.find_element(By.XPATH, "//input[@value='51']").click()
    driver.find_element(By.XPATH, "//input[@value='53']").click()
    driver.find_element(By.XPATH, "//input[@value='54']").click()
    driver.find_element(By.XPATH, "//input[@value='55']").click()
    driver.find_element(By.XPATH, "//input[@value='56']").click()


def FourthFields():
    # Fourth run
    driver.find_element(By.XPATH, "//input[@value='80']").click()
    driver.find_element(By.XPATH, "//input[@value='82']").click()
    driver.find_element(By.XPATH, "//input[@value='93']").click()
    driver.find_element(By.XPATH, "//input[@value='54']").click()
    driver.find_element(By.XPATH, "//input[@value='55']").click()
    driver.find_element(By.XPATH, "//input[@value='56']").click()


def ChooseJobTime():
    # Job time
    action.move_to_element(
        driver.find_element(By.XPATH, "//*[@id='CVEditor']/form/div[2]/div/p[3]/button/span")).perform()
    driver.find_element(By.XPATH, "//*[@id='CVEditor']/form/div[2]/div/p[3]/button/span").click()
    driver.find_element(By.XPATH, "//input[@value='3']").click()
    driver.find_element(By.XPATH, "//input[@value='2']").click()
    driver.find_element(By.XPATH, "//input[@value='30']").click()
    driver.find_element(By.XPATH, "//input[@value='10']").click()
    driver.find_element(By.XPATH, "//input[@value='26']").click()
    driver.find_element(By.XPATH, "//input[@value='11']").click()
    action.move_to_element(driver.find_element(By.XPATH, "//span[text()='סגור']")).click().perform()


def ChooseCV():
    # choose CV
    action.move_to_element(
        driver.find_element(By.XPATH, "//*[@id='CVEditor']/form/div[3]/div[1]/div[1]/div/input")).click().perform()

    driver.execute_script("scrollTo(0,500);")


def ClickSendButton():
    # Click on the send button
    action.move_to_element(driver.find_element(By.XPATH, "//button[text()='שלח']")).click().perform()


def FirstExecution():
    UpdateInfo()
    UpdateJobs()
    OpenFields()
    FirstFields()
    CloseFields()
    ChooseJobTime()
    ChooseCV()
    ClickSendButton()
    sleep(5)


def SecondExecution():
    action.move_to_element(driver.find_element(By.XPATH, "//*[@id='divTop']/div[1]/span/a[2]")).click().perform()

    # driver.find_element(By.XPATH, "//*[@id='divTop']/div[1]/span/a[2]").click()
    UpdateInfo()
    UpdateJobs()
    OpenFields()
    SecondFields()
    CloseFields()
    ChooseJobTime()
    ChooseCV()
    ClickSendButton()
    sleep(5)


def ThirdExecution():
    action.move_to_element(driver.find_element(By.XPATH, "//*[@id='divTop']/div[1]/span/a[2]")).click().perform()

    UpdateInfo()
    UpdateJobs()
    OpenFields()
    ThirdFields()
    CloseFields()
    ChooseJobTime()
    ChooseCV()
    ClickSendButton()
    sleep(5)


def FourthExecution():
    action.move_to_element(driver.find_element(By.XPATH, "//*[@id='divTop']/div[1]/span/a[2]")).click().perform()

    UpdateInfo()
    UpdateJobs()
    OpenFields()
    FourthFields()
    CloseFields()
    ChooseJobTime()
    ChooseCV()
    ClickSendButton()
    sleep(5)


#  flow of send CV automation
if __name__ == '__main__':
    # TODO: Check what is wrong
    StartBrowser()
    FirstExecution()
    SecondExecution()
    ThirdExecution()
    FourthExecution()
    CloseBrowser()
