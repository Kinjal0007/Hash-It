import sys
from Custom_Widgets.Widgets import *
from ui_login import *
import mysql.connector as sqltor

settings = QSettings()
user="user"

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self,self.ui)
        self.ui.registerBtn.clicked.connect(self.signupfunction)
        self.ui.loginBtn.clicked.connect(self.loginfunction)
        
    def signupfunction(self):
        username1=self.ui.username.text()
        password2=self.ui.password.text()
        confirm_password1=self.ui.confirm_password.text()
        if(len(username1)==0 or len(password2)==0 or len(confirm_password1)==0):
            self.ui.error.setText("Please input all fields")

        elif(password2!=confirm_password1):
            self.ui.error.setText("Both the passwords are not same")
            
        else:
            mycon=sqltor.connect(host="localhost",username="root",passwd="Hello1234@",database="login_details")
            cur=mycon.cursor()
            
            user_info=[username1,password2] 
            query="Insert into details(email,password) values('{}','{}')".format(username1,password2)
            cur.execute(query)
            
            print("username =",username1,"added to database")
            mycon.commit()
            mycon.close()

    def loginfunction(self):
        global user
        user=self.ui.emailfield.text()
        password=self.ui.passwordfield.text()
    
        if(len(user)==0 or len(password)==0):
            self.ui.error.setText("Please input all fields")
        else:
            mycon=sqltor.connect(host="localhost",user="root",passwd="Hello1234@",database="login_details")
            cur=mycon.cursor()
            query='SELECT password FROM details WHERE email=\''+user+"\'"
            cur.execute(query)
            result_pass=cur.fetchone()[0]
            mycon.close()
            
    

#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting....")


