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
# -- Description                              | SQL queries and builder for easy use
#                                                   in Infrastructure
# Usage Example
# Import this module and use these functions
# ------------------------------------------------------------------------------------------------


import allure
from CompanyPackage.TestCases import conftest


class SQL:
    """Query Builder"""

    @staticmethod
    @allure.step("Query Result Builder")
    def BuildQueryResult(item):
        dbCursor = conftest.dbConnector.cursor()
        dbCursor.execute(item)
        result = dbCursor.fetchall()
        return result

    @staticmethod
    @allure.step("Free Query Builder")
    def Query(value: str):
        return SQL.BuildQueryResult(value)

    '''SELECT Statement'''

    # Example :
    # SELECT *
    # FROM tableName
    @staticmethod
    @allure.step("Query builder -> Returns List of Tuples")
    def SelectAllFrom(table: str):
        query = "SELECT * FROM " + table
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT column1, column2, ...
    # FROM tableName
    @staticmethod
    @allure.step("Query builder -> Returns List of Tuples")
    def SelectColumns(columns: list, table: str):
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT DISTINCT column1, column2, ...
    # FROM tableName
    @staticmethod
    @allure.step("Query builder -> Returns DISTINCT List of Tuples")
    def SelectDistinctCols(columns: list, table: str):
        cols = ",".join(columns)
        query = "SELECT DISTINCT " + cols + " FROM " + table
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT  column1, column2, ...
    # FROM tableName WHERE condition(columnName = 'test') Text Fields
    # FROM tableName WHERE condition(columnName = 1) Numeric Fields
    @staticmethod
    @allure.step("Query builder -> Returns filtered List of Tuples")
    def SelectColsWhere(columns: list, table: str, condition: str):
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE " + condition
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT column1, column2, ...
    # FROM table_name
    # WHERE condition1 AND condition2
    @staticmethod
    @allure.step("Query builder -> Returns filtered List of Tuples")
    def SelectColsWhereAND(columns: list, table: str, condition1: str, condition2: str):
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE " + condition1 + " AND " + condition2
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT column1, column2, ...
    # FROM table_name
    # WHERE condition1 OR condition2
    @staticmethod
    @allure.step("Query builder -> Returns filtered List of Tuples")
    def SelectColsWhereOR(columns: list, table: str, condition1: str, condition2: str):
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE " + condition1 + " OR " + condition2
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT column1, column2, ...
    # FROM table_name
    # WHERE NOT condition
    @staticmethod
    @allure.step("Query builder -> Returns filtered List of Tuples")
    def SelectColsWhereNOT(columns: list, table: str, condition: str):
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE NOT " + condition
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT *
    # FROM table_name
    # ORDER BY column1, column2
    @staticmethod
    @allure.step("Query builder -> Returns filtered List of Tuples")
    def SelectAllOrderBy(table: str, columns: list):
        cols = ",".join(columns)
        query = "SELECT * FROM " + table + " ORDER BY " + cols
        return SQL.BuildQueryResult(query)

    '''INSERT INTO statement'''

    # Example :
    # INSERT INTO table_name (column1, column2, column3, ...)
    # VALUES (value1, value2, value3, ...)
    @staticmethod
    @allure.step("Query builder -> Insert new values to table")
    def InsertInto(table: str, columns: list, values: list):
        cols = ",".join(columns)
        values = "'" + "','".join(values) + "'"
        query = f"INSERT INTO {table} ({cols}) VALUES ({values})"
        return SQL.BuildQueryResult(query)

    '''MISC statements'''

    # Example :
    # UPDATE table_name
    # SET column1 = value1, column2 = value2, ... (column1 = 'text', column2 = 'text')
    # WHERE condition (column1 = 'text')
    @staticmethod
    @allure.step("Query builder -> Update values in table")
    def UpdateSetWhere(table: str, colNamesWithValues: str, condition: str):
        query = f"UPDATE {table} SET {colNamesWithValues} WHERE {condition}"
        return SQL.BuildQueryResult(query)

    # Example :
    # DELETE FROM table_name
    # WHERE condition (column1 = 'text') HERE can be extended with AND|OR
    @staticmethod
    @allure.step("Query builder -> Delete existing records in table")
    def DeleteWhere(table: str, condition: str):
        query = f"DELETE FROM {table} WHERE {condition}"
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT * FROM tableName
    # WHERE condition (column1 = 'text') HERE can be extended with AND|OR
    # LIMIT (num)
    @staticmethod
    @allure.step("Query builder -> Select Top to specify the number of records to return")
    def SelectTop(table: str, condition: str, nums: int):
        query = f"SELECT * FROM {table} WHERE {condition} LIMIT {nums}"
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT MIN(column)
    # FROM Products
    @staticmethod
    @allure.step("Query builder -> Select MIN in table")
    def SelectMin(column: str, table: str):
        query = f"SELECT MIN({column}) FROM {table}"
        return SQL.BuildQueryResult(query)

    # Example :
    # SELECT MAX(column)
    # FROM Products
    @staticmethod
    @allure.step("Query builder -> Select MAX in table")
    def SelectMax(column: str, table: str):
        query = f"SELECT MAX({column}) FROM {table}"
        return SQL.BuildQueryResult(query)
############################################################################

# continue from here implementing as needed

############################################################################
