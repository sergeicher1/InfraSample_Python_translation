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
# -- Description                              | # Automatically sends CV #
# ------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import *
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)


def OpenAndSearch():
    driver.get("https://b.log-on.com/")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[text()='כל התחומים']").click()
    driver.find_element(By.XPATH, "//button[@data-parent='qa-automation']").click()
    driver.find_element(By.XPATH, "//span[text()='QA Mobile']").click()
    driver.find_element(By.XPATH, "//span[text()='QA SAP']").click()
    driver.find_element(By.XPATH, "//span[text()='QA desktop']").click()
    driver.find_element(By.XPATH, "//span[text()='אוטומציה']").click()
    driver.find_element(By.XPATH, "//span[text()='QA Web']").click()
    driver.find_element(By.XPATH, "//span[text()='QA BI']").click()
    driver.find_element(By.XPATH, "//span[text()='QA AS400']").click()
    driver.find_element(By.XPATH, "//button[text()='כל האיזורים']").click()
    driver.find_element(By.XPATH, "//span[text()='צפון']").click()
    driver.find_element(By.XPATH, "//span[text()='שרון']").click()
    driver.find_element(By.XPATH, "//span[text()='מרכז']").click()
    driver.find_element(By.XPATH, "//span[text()='עבודה מהבית']").click()
    driver.find_element(By.XPATH, "//button[@class='btn button-lo search-jobs-button']").click()


def ShowAllPositions():
    # After search - open all positions
    # Scrolling should be... to focus on the element
    # el1 = driver.find_element(By.XPATH, "//button[@rel='next']").location_once_scrolled_into_view
    action.move_to_element(driver.find_element(By.XPATH, "//button[@rel='next']")).perform()
    driver.find_element(By.XPATH, "//button[@rel='next']").click()
    print(len(driver.find_elements(By.TAG_NAME, "h2")))
    sleep(0.5)

    for i in range(4):
        # el2 = driver.find_element(By.XPATH, "//button[@rel='next']").location_once_scrolled_into_view
        action.move_to_element(driver.find_element(By.XPATH, "//button[@rel='next']")).perform()
        driver.find_element(By.XPATH, "//button[@rel='next']").click()
        sleep(1)
        print(len(driver.find_elements(By.TAG_NAME, "h2")))
    # get back to the top of the page
    driver.find_element(By.XPATH, "//i[@class='fa fa-arrow-up']").click()


def SendFirstPosition():
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH,
                                                                       "//div[@class='job']/div[3]/div/button"))
    SendCV()
    sleep(3)


def SendCV():
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("סרגיי טשרניחובסקי")
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("sergeicher87@gmail.com")
    action.move_to_element(driver.find_element(By.XPATH, "//input[@type='file']")).perform()
    upload = driver.find_element(By.XPATH, "//input[@type='file']")
    upload.send_keys(
        "C:\\Users\\serge\\OneDrive\\Desktop\\סרגיי טשרניחובסקי - בודק תוכנה .pdf")
    if driver.page_source.find("סרגיי טשרניחובסקי - בודק תוכנה .pdf"):
        driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Testing flow of logon send CV automation
if __name__ == '__main__':
    OpenAndSearch()
    SendFirstPosition()
    assert "קורות החיים התקבלו בהצלחה!" in driver.page_source
    print("CV sent status: Successful")

    # region
    # ShowAllPositions()
    # TODO: After send CV to the first position, add loop in range len(of expanded positions) for others too
    #############################################################################################
    # First button with other XPATH

    # other_buttons = driver.find_elements(By.XPATH,
    #                                      "//div[@class='alm-reveal']/div/div/div/button[text()='שלח/י קו\"ח']")
    # print("length of other buttons: ", len(other_buttons))
    # driver.execute_script("arguments[0].click();", other_buttons[49])
    # sleep(1)
    #
    ##########################################################################################
    # other_buttons[3].click()
    ##########################################################################################################
    # action.move_to_element(other_buttons[3]).perform()
    # li = driver.find_elements(By.TAG_NAME, "h2")
    # for i in li:
    #     with open("C:\\Users\\serge\\OneDrive\\Desktop\\headers.txt", "a", encoding="utf-8") as header:
    #         header.write(i.text + "\n")

    # buttons = driver.find_elements(By.XPATH, "//button[@class='button-lo send-your-cv']")
    #############################################################################################
    # sleep(3)
    # '''Upload CV'''
    # send_list = driver.find_elements(By.XPATH,
    #                             "//button[@type='button' and @class='button-lo send-your-cv']//ancestor::button[1]")
    # send_list[0].click()
    # driver.find_element(By.XPATH,
    #                     "//button[@type='button' and @class='button-lo send-your-cv']//ancestor::button[1]").click()
    #
    # driver.find_element(By.XPATH, "//input[@type='text']").send_keys("סרגיי טשרניחובסקי")
    # driver.find_element(By.XPATH, "//input[@type='email']").send_keys("sergeicher87@gmail.com")
    # action = ActionChains(driver)
    # action.move_to_element(driver.find_element(By.XPATH, "//input[@type='file']")).perform()
    # upload = driver.find_element(By.XPATH, "//input[@type='file']")
    # upload.send_keys(
    #     "C:\\Users\\serge\\OneDrive\\Desktop\\סרגיי טשרניחובסקי - בודק תוכנה .pdf")
    # if driver.page_source.find("סרגיי טשרניחובסקי - בודק תוכנה .pdf"):
    #     driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # endregion
