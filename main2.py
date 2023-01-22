import os
import sys
from ui_main import *
from Custom_Widgets.Widgets import *
import mysql.connector as sqltar
from mysql.connector import Error 
from PySide2.QtWidgets import QTableWidgetItem
settings = QSettings()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show() 
        QAppSettings.updateAppSettings(self)
        
        l = QGridLayout()
        
        conn=AppFunctions.create_connection()
        rows=AppFunctions.getAllUsers(conn)

        AppFunctions.main(conn)
        AppFunctions.displayUsers(self,rows)
        # self.ui.addUserBtn.clicked.connect(AppFunctions.addUser(self,conn))

class AppFunctions():
    
    def create_connection():
        conn = None
        try:
            conn = sqltar.connect(host='localhost',database='login_details',user='root',password='Hello1234@')
            if conn.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(e)
        return conn
    
    def create_table(conn,create_table_sql):
        try:
            c=conn.cursor
            c.execute(create_table_sql)
        except:
            print("table cannot be made...")
            
    def main(conn):
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users (
                                            USER_ID INTEGER PRIMARY KEY ,
                                            USER_NAME TEXT,
                                            USER_EMAIL TEXT,
                                            USER_PHONE TEXT
                                         ); 
                                    """
        if conn is not None:
            AppFunctions.create_table(conn,create_user_table)
        else:
            print("Error cannot create the databse connection.")
    
    def getAllUsers(conn):
        get_all_users="""select * from users;"""
        try:
            c=conn.cursor
            c.execute(get_all_users)
            return c
        except:
            print("Data cannot be retreived")
    
    def addUser(self,conn):
        userName = self.ui.userName.text()
        email = self.ui.email.text()
        phoneNo = self.ui.phoneNo.text()

        # Create sql statement
        insert_person_data_sql = f"""INSERT INTO Users (USER_NAME, USER_EMAIL, USER_PHONE) VALUES ('{userName}', '{email}', '{phoneNo}');"""

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
            # AppFunctions.displayUsers(self, AppFunctions.getAllUsers(conn))
    
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
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 
