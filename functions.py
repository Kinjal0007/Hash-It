import os
import sys
from mysql.connector import Error
import mysql.connector as sqltor
# Import QTableWidgetItem(For creating new table cells)
from PySide2.QtWidgets import QTableWidgetItem

# Functions class
class AppFunctions():
    """docstring for AppFunctions"""
    def __init__(self, arg):
        super(AppFunctions, self).__init__()
        self.arg = arg

    def create_connection():
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn =sqltor.connect(host="localhost",username="root",passwd="Hello1234@",database="login_details")
        except Error as e:
            print(e)

        # Return connection
        return conn

    ########################################################################
    ## A function to Create table
    ########################################################################
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    ########################################################################
    ## Main function
    ########################################################################
    def main():
        # Create table if it does not exist
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users (
                                            USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            USER_NAME TEXT,
                                            USER_EMAIL TEXT,
                                            USER_PHONE TEXT
                                        ); 
                                    """
        # Create db connection
        conn = AppFunctions.create_connection()

        # create tables
        if conn is not None:
            # create user table
            AppFunctions.create_table(conn, create_user_table)

        else:
            print("Error! cannot create the database connection.")

    ########################################################################
    ## Get all users from database
    ########################################################################
    def getAllUsers():
        # Create db connection
        conn = AppFunctions.create_connection()

        get_all_users = """
                            SELECT * FROM Users;
                        """
        try:
            c = conn.cursor()
            c.execute(get_all_users)
            # Return all table rows
            return c
        except Error as e:
            print(e)

    ########################################################################
    ## Add a user to db
    ########################################################################
    def addUser(self):
        # Create db connection
        conn = AppFunctions.create_connection()

        # Get form values
        userName = self.ui.userName.text()
        email = self.ui.email.text()
        phoneNo = self.ui.phoneNo.text()

        # Create sql statement
        insert_person_data_sql = f"""
        INSERT INTO Users (USER_NAME, USER_EMAIL, USER_PHONE) VALUES ('{userName}', '{email}', '{phoneNo}');
        """

        # Execute sql statement
        if not conn.cursor().execute(insert_person_data_sql):
            print("Could not insert person data")
        else:
            conn.commit()
            # Clear form input
            self.ui.userName.setText("")
            self.ui.email.setText("")
            self.ui.phoneNo.setText("")

            # Load new user from DB to table view
            AppFunctions.displayUsers(self, AppFunctions.getAllUsers())

    ########################################################################
    ## Display users
    ########################################################################
    def displayUsers(self, rows):
        # Loop through all rows
        for row in rows:
            # Get number of rows
            rowPosition = self.ui.tableWidget.rowCount()

            # Skip rows that have already been loaded to table
            if rowPosition+1 > row[0]:
                continue

            itemCount = 0
            # Create new table row
            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            # Add items to row
            for item in row:
                self.qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.ui.tableWidget.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))


                itemCount = itemCount+1

            rowPosition = rowPosition+1


