import sys
import os
from Custom_Widgets.Widgets import *
from ui_interface import *
import mysql.connector as sqltor

settings = QSettings()
    
    
# class WelcomeScreen(QDialog):
#     def __init__(self):
#         super(WelcomeScreen, self).__init__()
#         loadUi("welcomescreen.ui",self)
#         self.login.clicked.connect(self.gotologin)
#         self.create.clicked.connect(self.gotocreate)
#         self.setWindowIcon(QtGui.QIcon("placeholder.png"))

#     def gotologin(self):
#         login = LoginScreen()
#         widget.addWidget(login)
#         widget.setCurrentIndex(widget.currentIndex()+1)
        
#     def gotocreate(self):
#         create=CreateAccScreen()
#         widget.addWidget(create)
#         widget.setCurrentIndex(widget.currentIndex()+1)

# class CreateAccScreen(QDialog):
#     def __init__(self):
#         super(CreateAccScreen,self).__init__()
#         loadUi("createacc.ui",self)
#         self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.signup.clicked.connect(self.signupfunction)
#         self.setWindowIcon(QtGui.QIcon("placeholder.png"))
        
#     def signupfunction(self):
#         fillupprofile=FillProfileScreen()        
#         widget.addWidget(fillupprofile)
#         widget.setCurrentIndex(widget.currentIndex()+1)
        
#         username=self.usernamefield.text()
#         password=self.passwordfield.text()
#         confirm_password=self.confirmpasswordfield.text()
#         if(len(username)==0 or len(password)==0 or len(confirm_password)==0):
#             self.error.setText("Please input all fields")
            
#         elif(password!=confirm_password):
#             self.error.setText("Both the passwords are not same")
#         else:
#             mycon=sqltor.connect(host="localhost",username="root",passwd="Hello1234@",database="login_details")
#             cur=mycon.cursor() 
            
#             user_info=[username,password]
#             query="Insert into details(email,password) values('{}','{}')".format(username,password)
#             cur.execute(query)
            
#             mycon.commit()
#             mycon.close()
#             self.success.setText("Success")
#             fillupprofile=FillProfileScreen()
#             widget.addWidget(fillupprofile)
#             widget.setCurrentIndex(widget.currentIndex()+1)
            
        
# class FillProfileScreen(QDialog):
#     def __init__(self):
#         super(FillProfileScreen, self).__init__()
#         loadUi("fillprofile.ui",self)
#         self.image.setPixmap(QPixmap('placeholder.png'))
        

# class LoginScreen(QDialog):
#     def __init__(self):
#         super(LoginScreen, self).__init__()
#         loadUi("login.ui",self)
#         self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.login.clicked.connect(self.loginfunction)
#         self.setWindowIcon(QtGui.QIcon("placeholder.png"))
#     def loginfunction(self):
#         user=self.emailfield.text()
#         password=self.passwordfield.text()
        
#         if(len(user)==0 or len(password)==0):
#             self.error.setText("Please input all fields")
#         else:
#             mycon=sqltor.connect(host="localhost",user="root",passwd="Hello1234@",database="login_details")
#             cur=mycon.cursor()
#             query='SELECT password FROM details WHERE email=\''+user+"\'"
#             cur.execute(query)
#             result_pass=cur.fetchone()[0]
#             global User
#             User=user
#             if(result_pass==password):
#                 self.error.setText("Successfully Logged In")
#                 User=user
#                 print("Account has been successfully logged in...")
#                 mainscreen=MainScreen()
#                 widget.addWidget(mainscreen)
#                 widget.setCurrentIndex(widget.currentIndex()+1)
                
#             else:
#                 self.error.setText("Invalid Username or Password ")


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        loadJsonStyle(self,self.ui)
        self.show()

#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting....")


