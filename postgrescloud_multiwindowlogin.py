#using the input data from the pyqt5 to login into the system with the client login app to checking with the database 
import os 
import sys 
import csv
import json 
import requests
import socket
import getpass 
import psycopg2 # Login for the client side on the app machine 
import pandas as pd 
import subprocess # Getting the subprocess 
from PyQt5 import QtCore, QtWidgets, uic,Qt,QtGui 
from PyQt5.QtWidgets import QApplication,QTreeView,QDirModel,QFileSystemModel,QVBoxLayout, QTreeWidget,QStyledItemDelegate, QTreeWidgetItem,QLabel,QGridLayout,QLineEdit,QDial,QComboBox,QTextEdit,QTabWidget,QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QIcon,QImage,QPalette,QBrush
from pyqtgraph.Qt import QtCore, QtGui   #PyQt graph to control the model grphic loaded  
import pyqtgraph.opengl as gl
#Now using this postgresql-opaque-57490 #heroku cloud postgresql roboreactoruser https://roboreactoruser.herokuapp.com/ | https://git.heroku.com/roboreactoruser.git
#postgresql-rigid-15553  #heroku cloud postgresql robouserdb https://robouserdb.herokuapp.com/ | https://git.heroku.com/robouserdb.git
#postgresql-amorphous-76096 as DATABASE_URL https://robotuserinterface.herokuapp.com/
DATABASE_URL = "postgres://xvbxxuaqpujgue:5c062c3b3fe5ed0568ac106245866ba273ff816b3eaaed847a0a9bfb71742318@ec2-44-198-236-169.compute-1.amazonaws.com:5432/d381tss8v44rv3"
Host = "ec2-44-198-236-169.compute-1.amazonaws.com"
Database = "d381tss8v44rv3",
Password = "5c062c3b3fe5ed0568ac106245866ba273ff816b3eaaed847a0a9bfb71742318"
Port = "5432"
username = getpass.getuser()
print(username)


class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()

        #Load the UI Page
        uic.loadUi('Roboticfirmwaregenerator.ui', self)
        self.setWindowTitle('Roboreactor firmware generator  User:'+"\t"+username)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkGray)
        self.setPalette(p)
        #Adding the roboreactor firmware generator function right here 

    
class MainWindow(QtWidgets.QMainWindow):
   
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('Loginpage.ui', self)
        self.setWindowTitle('Welcome to roboreactor User:'+"\t"+username)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkGray)
        self.setPalette(p)
        oImage = QImage("kobuki_new.jpg")
        oImage.scaled(300,200)
        #sImage = oImage.scaled(QSize(300,200))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)
        self.pushButton.clicked.connect(self.Login) #button login 
        self.text = self.findChild(QTextEdit,"textEdit") #Getting the text edit input the username on the system
        self.text2 = self.findChild(QLineEdit,"lineEdit") #Getting the password input
        self.label.setStyleSheet("color:white")
        self.label_2.setStyleSheet("color:white")
        self.label_3.setStyleSheet("color:white")
        query()
        #submit
    def Login(self):
            print("Logging into the database......")
            usernamedata = self.text.toPlainText()
            passworddata = self.text2.text() # This is the QLineEdit for the text hiding password data 
            print(usernamedata,passworddata) #Getting the username and password
            #reading the cloud database and activate the new window 
            print(update())
            self.w = MainWindow2()
            self.w.show() 
            self.hide() 
def query():
      #Getting the host url https://dashboard.heroku.com/apps 
      #DATABASE_URL = os.environ['DATABASE_URL']
      #conn = psycopg2.connect(DATABASE_URL, sslmode='require') 
      conn = psycopg2.connect(
               DATABASE_URL,
               #host = Host,
               #database = Database,
               #password = Password,
               #port = Port,
               sslmode='require',
      )
      c = conn.cursor()
      c.execute('''CREATE TABLE IF NOT EXISTS customers
      (first_name Text,
      last_name Text,
      e_mail Text,
      password Text,
      payment_status Text,
      Cardholder Text,
      schedule Text,
      Recharge Text);
      ''')
      conn.commit()
      c.close()
      
# This submit will be on the server side to register the customer from the website only
def submit():
      #DATABASE_URL = os.environ['DATABASE_URL']
      #conn = psycopg2.connect(DATABASE_URL, sslmode='require') 
      conn = psycopg2.connect(
        
               host = Host,
               database = Database,
               password = Password,
               port = Port,
               sslmode='require',
      )
      c = conn.cursor()
      c.execute('''CREATE TABLE IF NOT EXIST customers
      (first_name Text,
      last_name Text,
      e_mail Text,
      password Text,
      payment_status Text,
      cardholder Text,
      schedule Text,
      recharge Text);''')
      # Create a cursor
      c = conn.cursor()
      # Insert data into table 
      C1 = "Chanapai"
      C2 = "Chuadchum" 
      C3 = "kornbot380@hotmail.com"
      C4 = "Rkl3548123#"
      C5 = "Pending"  
      C6 = "ChanapaiChuadchum" 
      C7 = "10/12/2021" 
      C8 = recharge.get()
      c.execute('''INSERT INTO customers (first_name,last_name,e_mail,password,payment_status,cardholder,schedule,recharge)
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''',(C1,C2,C3,C4,C5,C6,C7,C8)
      )
      conn.commit()
      conn.close() 
      update()
# using the update function to fetch the login data 
def update():
      #DATABASE_URL = os.environ['DATABASE_URL']
      #conn = psycopg2.connect(DATABASE_URL, sslmode='require') 
      conn = psycopg2.connect(
               host = Host,
               database = Database,
               password = Password,
               port = Port,
               sslmode='require',
      )
      c = conn.cursor()
      c.execute('''CREATE TABLE IF NOT EXIST customers
      (first_name Text,
      last_name Text,
      e_mail Text,
      password Text,
      payment_status Text,
      cardholder Text,
      schedule Text,
      recharge Text);''')
      # Create a cursor
      c = conn.cursor()
      #Grab stuff from online database 
      c.execute("SELECT*FROM customers")
      records = c.fetchall() 
      output = '' 
      for records in records:
             print(records[records]) #Getting the records data 
      conn.close()        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

    
if __name__ == '__main__':         
    main()