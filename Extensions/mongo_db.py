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
# -- Description                              | MongoDB queries and builder
#                                                   for easy use in Infrastructure
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------

import allure
import pymongo


class MongoDB:
    """Build DB Object"""

    @staticmethod
    @allure.step("Build DB Object")
    def BuildDBObject(DatabaseURLWithPass: str, dbName: str, colName: str):
        client = pymongo.MongoClient(DatabaseURLWithPass)
        db = client[dbName]
        col = db[colName]
        return col

    '''Create and Insert ONE Value'''

    # To create a collection in MongoDB, use database object and specify
    # the name of the collection you want to create.
    # MongoDB will create the collection if it does not exist.
    # Without data the collection and database will NOT be created!
    # Example:
    # dataPath = "D:\\pyCharm\\InfrastructureSample\\Configuration\\data.xml"
    # databaseURL = XmlReadData(dataPath, "DbURLwithPass")
    # dbName = XmlReadData(dataPath, "MonDbName")
    # colName = XmlReadData(dataPath, "colName")
    # values = {
    #   "_id": 1,
    #   "name": "Steven"
    #  }
    @staticmethod
    @allure.step("Add DB Document to collection")
    def AddDocument(DatabaseURLWithPass: str, dbName: str, colName: str, value: dict):
        MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).insert_one(value)

    '''Create and Insert MULTIPLE Values'''

    # If you do not want MongoDB to assign unique ids for you document,
    # you can specify the _id field when you insert the document(s).
    # Remember that the values has to be unique. Two documents cannot have the same _id.
    @staticmethod
    @allure.step("Add DB Documents to collection")
    def AddDocuments(DatabaseURLWithPass: str, dbName: str, colName: str, values: list):
        MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).insert_many(values)

    '''Find All'''

    # The find() method returns all occurrences in the selection.
    @staticmethod
    @allure.step("Find all DB Documents in collection")
    def FindAll(DatabaseURLWithPass: str, dbName: str, colName: str) -> list:
        li = []
        for i in MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).find():
            li.append(i)
        return li

    '''Find Specific value/s'''

    # The second parameter of the find() method is an object describing which fields
    # to include in the result.
    # This parameter is optional, and if omitted, all fields will be included in the result.

    # Example:
    # val = { "_id": 0, "name": 1, "address": 1 }
    # You are not allowed to specify both 0 and 1 values in the same object (except if one
    # of the fields is the _id field). If you specify a field with the value 0,
    # all other fields get the value 1
    @staticmethod
    @allure.step("Find specific DB Document in collection")
    def FindSpecificDocument(DatabaseURLWithPass: str, dbName: str, colName: str, valuesToFind: dict) -> list:
        li = []
        for i in MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).find({}, valuesToFind):
            li.append(i)
        return li

    '''Filter the Result'''

    # Example:
    # val = {"address": "New York 23"}
    # To make advanced queries you can use modifiers as values in the query object.
    # E.g. to find the documents where the "address" field starts with the letter "S"
    # or higher (alphabetically), use the greater than modifier: {"$gt": "S"}
    # Example:
    # val = { "address": { "$gt": "S" } }
    # Regular expressions. To find only the documents where the "address"
    # field starts with the letter "S", use the regular expression {"$regex": "^S"}
    # Example:
    # val = { "address": { "$regex": "^S" } }
    @staticmethod
    @allure.step("Filter DB Documents")
    def Filter(DatabaseURLWithPass: str, dbName: str, colName: str, valuesToFind: dict) -> list:
        li = []
        docs = MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).find(valuesToFind)
        for i in docs:
            li.append(i)
        return li

    '''Limit the result to specified number'''

    @staticmethod
    @allure.step("Limit the result")
    def FilterWithLimit(DatabaseURLWithPass: str, dbName: str, colName: str, valueToFind: dict, number: int) -> list:
        li = []
        res = MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).find(valueToFind).limit(number)
        for i in res:
            li.append(i)
        return li

    '''Sort the result'''

    # Example:
    # direction = 1 -> ascending
    # direction = -1 -> descending
    @staticmethod
    @allure.step("Sort ascending / descending DB search results")
    def Sort(DatabaseURLWithPass: str, dbName: str, colName: str, value: str, direction: int) -> list:
        li = []
        docs = MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).find().sort(value, direction)
        for i in docs:
            li.append(i)
        return li

    '''Delete one document in DB'''

    @staticmethod
    @allure.step("Delete document in DB collection")
    def DeleteDocument(DatabaseURLWithPass: str, dbName: str, colName: str, value: dict):
        MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).delete_one(value)

    '''Delete many document in DB'''

    @staticmethod
    @allure.step("Delete Documents in DB collection")
    def DeleteDocuments(DatabaseURLWithPass: str, dbName: str, colName: str, value: dict):
        MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).delete_many(value)

    '''Delete ALL documents in collection'''

    @staticmethod
    @allure.step("Delete all documents in DB collection")
    def DeleteAllDocuments(DatabaseURLWithPass: str, dbName: str, colName: str):
        MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).delete_many({})

    '''Drop collection in database'''

    @staticmethod
    @allure.step("Drop collection in database")
    def DropCollection(DatabaseURLWithPass: str, dbName: str, colName: str):
        MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).drop()

    '''Update one document in collection'''

    @staticmethod
    @allure.step("Update document in collection")
    def UpdateDocument(DatabaseURLWithPass: str, dbName: str, colName: str, record: dict, newRecord: dict):
        MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).update_one(record, newRecord)

    '''Update many documents in collection'''

    @staticmethod
    @allure.step("Update documents in collection")
    def UpdateDocuments(DatabaseURLWithPass: str, dbName: str, colName: str, record: dict, newRecord: dict):
        MongoDB.BuildDBObject(DatabaseURLWithPass, dbName, colName).update_many(record, newRecord)

############################################################################


# continue from here implementing as needed


############################################################################
