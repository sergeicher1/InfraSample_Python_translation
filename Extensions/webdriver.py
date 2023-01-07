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
# -- Description                              | Selenium Object Methods for easy use in Infrastructure
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------


import allure
from time import sleep
from typing import Dict
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from CompanyPackage.TestCases import conftest
from Extensions.ui_actions import UiActions


class WebDriver:
    """Browser Interactions"""

    # You can read the current page title from the browser
    @staticmethod
    @allure.step("Get title of the page")
    def GetTitle() -> str:
        return conftest.driver.title

    # you can read the current URL from the browser’s address bar
    @staticmethod
    @allure.step("Get current url")
    def GetURL() -> str:
        return conftest.driver.current_url

    # return the page source
    @staticmethod
    @allure.step("Get Page source")
    def GetPageSource() -> str:
        return conftest.driver.page_source

    '''Browser Navigation'''

    @staticmethod
    @allure.step("Navigation to specific page")
    def NavigateToPage(path: str):
        conftest.driver.get(path)

    # Pressing the browser’s back button
    @staticmethod
    @allure.step("Browser Back")
    def Back():
        conftest.driver.back()

    # Pressing the browser’s forward button
    @staticmethod
    @allure.step("Browser Forward")
    def Forward():
        conftest.driver.forward()

    # Refresh the current page
    @staticmethod
    @allure.step("Browser Refresh")
    def Refresh():
        conftest.driver.refresh()

    '''JavaScript alerts, prompts and confirmations'''

    # Scroll To specific position in browser
    @staticmethod
    @allure.step("Execute ScrollDown JS Script")
    def ScrollDown(value1: int, value2: int):
        conftest.driver.execute_script(f"window.scrollTo({value1},{value2})")

    # The simplest of these is referred to as an alert, which shows a custom message,
    # and a single button which dismisses the alert, labelled in most browsers as OK
    @staticmethod
    @allure.step("Accept Alert")
    def AcceptAlert(elem: WebElement):  # Element that opens an ALERT
        UiActions.Click(elem)
        WebDriverWait(conftest.driver, 10).until(ec.alert_is_present())
        alert = conftest.driver.switch_to.alert
        alert.accept()

    # A confirmation box is similar to an alert, except the user can also choose to cancel the message
    @staticmethod
    @allure.step("Confirm Alert -> Dismiss")
    def ConfirmAlert(elem: WebElement):  # Element that opens an ALERT
        UiActions.Click(elem)
        WebDriverWait(conftest.driver, 10).until(ec.alert_is_present())
        alert = conftest.driver.switch_to.alert
        alert.dismiss()

    # TODO: See why id does not send text to Alert
    # Prompts are similar to confirm boxes, except they also include a text input.
    @staticmethod
    @allure.step("Prompt Alert -> Include text input")
    def PromptAlert(elem: WebElement, text: str):  # Element that opens an ALERT, text to enter
        UiActions.Click(elem)
        WebDriverWait(conftest.driver, 10).until(ec.alert_is_present())
        alert = conftest.driver.switch_to.alert
        alert.send_keys(text)
        sleep(3)
        alert.accept()

    '''Upload file'''

    @staticmethod
    @allure.step("Upload File -> the input element is of type -> FILE")
    def UploadFile(elem1: WebElement, filePathName: str, elem2: WebElement):
        UiActions.UpdateText(elem1, filePathName)
        elem2.submit()

    '''Information about web elements'''

    # This method is used to check if the connected Element is displayed on a webpage.
    # Returns a Boolean value, True if the connected element is displayed
    # in the current browsing context else returns false.
    @staticmethod
    @allure.step("Check if element is_displayed")
    def IsDisplayed(elem: WebElement):
        return elem.is_displayed()

    # This method is used to check if the connected Element is enabled
    # or disabled on a webpage. Returns a boolean value, True if the connected element
    # is enabled in the current browsing context else returns false.
    @staticmethod
    @allure.step("Check if element is_enabled")
    def IsEnabled(elem: WebElement):
        return elem.is_enabled()

    # This method determines if the referenced Element is Selected or not.
    # This method is widely used on Check boxes, radio buttons, input elements,
    # and option elements. Returns a boolean value,
    # True if referenced element is selected in the current
    # browsing context else returns false.
    @staticmethod
    @allure.step("Check if element is_selected")
    def IsSelected(elem: WebElement):
        return elem.is_selected()

    # It is used to fetch the TagName of the referenced Element
    # which has the focus in the current browsing context.
    @staticmethod
    @allure.step("Return Tag Name of element")
    def TagName(elem: WebElement):
        return elem.tag_name

    # It is used to fetch the dimensions and coordinates of the referenced element.
    @staticmethod
    @allure.step("The fetched data body contain the following details:"
                 "X-axis position from the top-left corner of the element"
                 "y-axis position from the top-left corner of the element"
                 "Height of the element"
                 "Width of the element ")
    def SizeAndPosition(elem: WebElement):
        return elem.rect

    # Retrieves the value of specified computed style
    # property of an element in the current browsing context.
    @staticmethod
    @allure.step("Get CSS Value of element")
    def CssValue(elem: WebElement, cssValue: str):
        return elem.value_of_css_property(cssValue)

    # Retrieves the rendered text of the specified element.
    @staticmethod
    @allure.step("Get Text Content")
    def Text(elem: WebElement):
        return elem.text

    # Fetches the run time value associated with a DOM attribute.
    # It returns the data associated with the DOM attribute or property of the element.
    @staticmethod
    @allure.step("Fetch Attribute")
    def Attribute(elem: WebElement, value: str):
        return elem.get_attribute(value)

    # Fetches the run time value associated with a DOM attribute.
    # It returns the data associated with the DOM attribute or property of the element.
    @staticmethod
    @allure.step("Fetch DOM Attribute")
    def DOMAttribute(elem: WebElement, value: str):
        return elem.get_dom_attribute(value)

    # Fetches the run time value associated with a DOM attribute.
    # It returns the data associated with the DOM attribute or property of the element.
    @staticmethod
    @allure.step("Fetch Property")
    def AttributeProperty(elem: WebElement, value: str):
        return elem.get_property(value)

    '''Working with cookies'''

    # It is used to add a cookie to the current browsing context.
    # Add Cookie only accepts a set of defined serializable JSON object
    # Here is the link to the list of accepted JSON key values: https://www.w3.org/TR/webdriver1/#cookies
    @staticmethod
    @allure.step("Add Cookie")
    def AddCookie(item: Dict):
        conftest.driver.add_cookie(item)

    # It returns the serialized cookie data matching with the cookie name
    # among all associated cookies.
    @staticmethod
    @allure.step("Get Named Cookie")
    def GetCookie(value: str):
        return conftest.driver.get_cookie(value)

    # It returns a ‘successful serialized cookie data’ for current browsing context.
    # If browser is no longer available it returns error
    @staticmethod
    @allure.step("Get All Cookies")
    def GetCookies():
        return conftest.driver.get_cookies()

    # It deletes the cookie data matching with the provided cookie name.
    @staticmethod
    @allure.step("Delete Cookie")
    def DeleteCookie(value: str):
        conftest.driver.delete_cookie(value)

    # It deletes all the cookies of the current browsing context.
    @staticmethod
    @allure.step("Delete All Cookies")
    def DeleteCookies():
        conftest.driver.delete_all_cookies()

    '''Working with iFrames and frames'''

    # You can find the frame using your preferred selector and switch to it.
    @staticmethod
    @allure.step("Using a WebElement")
    def SwitchToIframe(elem: WebElement):
        conftest.driver.switch_to.frame(elem)

    # To leave an iframe or frame set, switch back to the default content
    @staticmethod
    @allure.step("Leaving a frame")
    def LeaveIframe():
        conftest.driver.switch_to.default_content()

    '''Working with windows and tabs'''

    # BEFORE switching -> Store the ID of the original window in variable
    @staticmethod
    @allure.step("Store original window handle")
    def StoreOriginalWindow():
        return conftest.driver.current_window_handle

    # When you are finished with a window or tab, and it is not the last window or tab
    # open in your browser, you should close it and switch back to the window you
    # were using previously
    @staticmethod
    def SwitchToOriginalWindow(elem):
        conftest.driver.switch_to.window(elem)

    # Opens a new tab and switches to new tab
    @staticmethod
    @allure.step("Switch to new tab")
    def SwitchToNewTab():
        conftest.driver.switch_to.new_window("tab")

    # Opens a new window and switches to new window
    @staticmethod
    @allure.step("Switch to new window")
    def SwitchToNewWindow():
        conftest.driver.switch_to.new_window('window')

    # Close the current tab
    @staticmethod
    @allure.step("Close tab")
    def CloseTab():
        conftest.driver.close()

    '''Taking screenshots'''

    # Used to capture screenshot for current browsing context.
    @staticmethod
    @allure.step("Taking screenshot")
    def TakeScreenshot(filePathName: str):
        conftest.driver.save_screenshot(f"{filePathName}.png")

    # Used to capture screenshot of an element for current browsing context.
    @staticmethod
    @allure.step("Taking element screenshot")
    def TakeElementScreenshot(elem: WebElement, filePathName: str):
        elem.screenshot(f"{filePathName}.png")

############################################################################

# continue from here implementing as needed


############################################################################
