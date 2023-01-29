import sys
from Custom_Widgets.Widgets import *
import mysql.connector as sqltor
from ui_login import *
from main2 import *
from functions import *
import platform
settings = QSettings()
user="user"

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> GLOBALS
counter = 0

class MainAppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles = {
        "style2.json"
        })
        self.show() 
        QAppSettings.updateAppSettings(self)
        AppFunctions.main()
        AppFunctions.displayUsers(self, AppFunctions.getAllUsers())
        self.ui.addUserBtn.clicked.connect(lambda: AppFunctions.addUser(self))


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO Hash-It")

        # Change Texts
        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_description.setText("<strong>ESTABLISHING</strong> CONNECTION TO DATABASE"))
        QtCore.QTimer.singleShot(2200, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        QtCore.QTimer.singleShot(4300,lambda: self.ui.label_description.setText("<strong>CONNECTING</strong> TO THE REMOTE SERVER"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainAppWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Login_Window()
        self.ui.setupUi(self)
        loadJsonStyle(self,self.ui)
        self.ui.registerBtn.clicked.connect(self.signupfunction)
        self.ui.loginBtn.clicked.connect(self.loginfunction)
        # QAppSettings.updateAppSettings(self)
        
    #     self.menu = QtWidgets.QMenu()
    #     self.menu.addAction("Default-Dark", self.apply_dark_theme)
    #     self.menu.addAction("Default-Light", self.apply_light_theme)

    #     self.ui.themeBtn.setMenu(self.menu)

    # def apply_dark_theme(self):
    #     settings = QSettings()
    #     settings.setValue("THEME", "Default-Dark")
    #     QAppSettings.updateAppSettings(self)

    # def apply_light_theme(self):
    #     settings = QSettings()
    #     settings.setValue("THEME", "Default-Light")
    #     QAppSettings.updateAppSettings(self)
        
        
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
            self.ui.error_2.setText("Please input all fields")
        else:
            mycon=sqltor.connect(host="localhost",user="root",passwd="Hello1234@",database="login_details")
            cur=mycon.cursor()
            query='SELECT password FROM details WHERE email=\''+user+"\'"
            cur.execute(query)
            result_pass=cur.fetchone()[0]
            if (password==result_pass):
                print("Successfully logged In....","\n")
                self.MainWindow=SplashScreen()
                # self.MainWindow=MainAppWindow()
                self.MainWindow.show()
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
