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
# -- Description                              | REST API Methods builder for easy
#                                                   use in Infrastructure
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------


import allure
import requests

'''Variables'''
header = {"Content-type": "application/json"}


class RestAPI:
    """GET Request"""

    # In params -> add "?"
    @staticmethod
    @allure.step("Get Request")
    def GetRequest(urlAPI: str, params: str):
        response = requests.get(urlAPI + params)
        return response

    # After response specify values to extract
    # Example : ExtractValueFromResponse(response)["data"][0]["first_name"])
    @staticmethod
    @allure.step("Extract value from response")
    def ExtractValueFromResponse(response):
        rJSON = response.json()
        return rJSON

    '''POST Request'''

    # First -> Create dict with payload
    @staticmethod
    @allure.step("Post Request")
    def PostRequest(path, payload):
        response = requests.post(path, json=payload, headers=header)
        return response.status_code

    '''PUT Request'''

    # First -> Create dict with payload
    @staticmethod
    @allure.step("Put Request")
    def PutRequest(path, payload):
        response = requests.put(path, json=payload, headers=header)
        return response.status_code

    '''PATCH Request'''

    # First -> Create dict with payload
    @staticmethod
    @allure.step("Patch Request")
    def PatchRequest(path, payload):
        response = requests.patch(path, payload)
        return response.status_code

    '''DELETE Request'''

    @staticmethod
    @allure.step("Delete Request")
    def DeleteRequest(path):
        response = requests.delete(path)
        return response.status_code

############################################################################

# continue from here implementing as needed

############################################################################
