# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasycricketmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from newteamname import Ui_Form

from openteam import Ui_Form as open

from Eval_screen import Ui_Evaluate_Window as Eval_class

# importing module to calculate points

from points_earned import calc_points as player_scores

import sqlite3
mygame=sqlite3.connect('fantasycricket.db')
curgame=mygame.cursor()

class Ui_Fantasy_Cricket(object):

    def __init__(self):

        self.Form=QtWidgets.QWidget()
        self.newteamname = Ui_Form()
        self.newteamname.setupUi(self.Form)

        self.openscreen=QtWidgets.QWidget()
        self.openteam=open()
        self.openteam.setupUi(self.openscreen)

        self.evalscreen=QtWidgets.QMainWindow()
        self.eval_object=Eval_class()
        self.eval_object.setupUi(self.evalscreen)
        
        self.totalplayers=0
        self.batsmancount=0
        self.bowlerscount=0
        self.arcount=0
        self.wkcount=0
        self.newteam_name=None
        self.points_available=1000
        self.points_used=0
        self.items=[]

        self.error_screen=QtWidgets.QErrorMessage()

    def setupUi(self, Fantasy_Cricket):
        Fantasy_Cricket.setObjectName("Fantasy_Cricket")
        Fantasy_Cricket.resize(951, 681)
        self.centralwidget = QtWidgets.QWidget(Fantasy_Cricket)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setObjectName("t1")
        self.horizontalLayout_3.addWidget(self.t1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setObjectName("t2")
        self.horizontalLayout_3.addWidget(self.t2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        self.t3.setObjectName("t3")
        self.horizontalLayout_3.addWidget(self.t3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        self.t4.setObjectName("t4")
        self.horizontalLayout_3.addWidget(self.t4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.b1 = QtWidgets.QRadioButton(self.centralwidget)
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)

        self.b2 = QtWidgets.QRadioButton(self.centralwidget)
        self.b2.setObjectName("b2")
        self.horizontalLayout.addWidget(self.b2)

        self.b3 = QtWidgets.QRadioButton(self.centralwidget)
        self.b3.setObjectName("b3")
        self.horizontalLayout.addWidget(self.b3)

        self.b4 = QtWidgets.QRadioButton(self.centralwidget)
        self.b4.setObjectName("b4")
        self.horizontalLayout.addWidget(self.b4)

        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        self.t5.setObjectName("t5")
        self.horizontalLayout_2.addWidget(self.t5)
        spacerItem4 = QtWidgets.QSpacerItem(265, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.t6 = QtWidgets.QLineEdit(self.centralwidget)
        self.t6.setObjectName("t6")
        self.horizontalLayout_2.addWidget(self.t6)
        spacerItem6 = QtWidgets.QSpacerItem(165, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 5, 0, 1, 1)
        self.l2 = QtWidgets.QListWidget(self.centralwidget)
        self.l2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.l2.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.l2.setObjectName("l2")
        self.gridLayout.addWidget(self.l2, 7, 2, 1, 1)
        self.l1 = QtWidgets.QListWidget(self.centralwidget)
        self.l1.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.l1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 3, 0, 1, 1)
        Fantasy_Cricket.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(Fantasy_Cricket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        self.menuManage_Team.setObjectName("menuManage_Team")
        Fantasy_Cricket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fantasy_Cricket)
        self.statusbar.setObjectName("statusbar")
        Fantasy_Cricket.setStatusBar(self.statusbar)

        #New

        self.actionNew_Team = QtWidgets.QAction(Fantasy_Cricket)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionNew_Team.setShortcut("Ctrl+N")
        self.actionNew_Team.triggered.connect(self.newteam)
        self.newteamname.btn.clicked.connect(self.new_team_name)

        #Open

        self.actionOpen_Team = QtWidgets.QAction(Fantasy_Cricket)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionOpen_Team.setShortcut("Ctrl+O")
        self.actionOpen_Team.triggered.connect(self.open_team)
        self.openteam.btn.clicked.connect(self.openteamname)

        #Save

        self.actionSave_Team = QtWidgets.QAction(Fantasy_Cricket)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionSave_Team.setShortcut("Ctrl+S")
        self.actionSave_Team.triggered.connect(self.save_file)

        #Evaluate

        self.actionEvaluate_team = QtWidgets.QAction(Fantasy_Cricket)
        self.actionEvaluate_team.setObjectName("actionEvaluate_team")
        self.actionEvaluate_team.setShortcut("ctrl+E")
        self.actionEvaluate_team.triggered.connect(self.eval_screen)
        self.eval_object.cb_2.currentTextChanged.connect(self.combobox1)
        self.eval_object.pushButton.clicked.connect(self.closeevalscreen)


        
        self.menuManage_Team.addAction(self.actionNew_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionOpen_Team)
        self.menuManage_Team.addAction(self.actionSave_Team)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionEvaluate_team)
        self.menuManage_Team.addSeparator()
        self.menubar.addAction(self.menuManage_Team.menuAction())


        #select/remove signal/slot

        self.l1.itemDoubleClicked.connect(self.rlist1)
        self.l2.itemDoubleClicked.connect(self.rlist2)

        
        self.retranslateUi(Fantasy_Cricket)
        QtCore.QMetaObject.connectSlotsByName(Fantasy_Cricket)

    def retranslateUi(self, Fantasy_Cricket):
        _translate = QtCore.QCoreApplication.translate
        Fantasy_Cricket.setWindowTitle(_translate("Fantasy_Cricket", "MainWindow"))
        self.label_5.setText(_translate("Fantasy_Cricket", "Batsman (BAT)"))
        self.label_6.setText(_translate("Fantasy_Cricket", "       Bowlers (BWL)"))
        self.label_4.setText(_translate("Fantasy_Cricket", "      All Rounders (AR)"))
        self.label_3.setText(_translate("Fantasy_Cricket", "       Wicket Keeper (WK)"))   
        self.b1.setText(_translate("Fantasy_Cricket", "BAT"))
        self.b2.setText(_translate("Fantasy_Cricket", "BWL"))
        self.b3.setText(_translate("Fantasy_Cricket", "AR"))
        self.b4.setText(_translate("Fantasy_Cricket", "WK"))
        self.label.setText(_translate("Fantasy_Cricket", "Points Available :"))
        self.label_2.setText(_translate("Fantasy_Cricket", "Points Used :"))
        self.label_7.setText(_translate("Fantasy_Cricket", "Your Selections  :"))
        self.label_8.setText(_translate("Fantasy_Cricket", "         >         "))
        self.menuManage_Team.setTitle(_translate("Fantasy_Cricket", "Manage Team"))
        self.actionNew_Team.setText(_translate("Fantasy_Cricket", "New Team"))
        self.actionOpen_Team.setText(_translate("Fantasy_Cricket", "Open Team"))
        self.actionSave_Team.setText(_translate("Fantasy_Cricket", "Save Team"))
        self.actionEvaluate_team.setText(_translate("Fantasy_Cricket", "Evaluate Team"))
   

#New team      

    def newteam(self):
        self.Form.show()
    
    def new_team_name(self):
        self.newteam_name=self.newteamname.l.text()
        self.Form.hide()
        self.l1.clear()
        self.l2.clear()
        
        self.b1.clicked.connect(self.batsman)
        self.b2.clicked.connect(self.bowlers)
        self.b3.clicked.connect(self.allrounders)
        self.b4.clicked.connect(self.wktkeepers)
        self.t5.setText(str(1000))
        self.t6.setText(str(0))
        

#Opening Specified team

    def open_team(self):
        self.openscreen.show()

    def openteamname(self):
        self.l1.clear()
        self.l2.clear()
        self.points_available=1000
        self.points_used=0
        self.txt=self.openteam.l.text()
        self.newteam_name=self.openteam.l.text()

        sql="SELECT Players from Teams WHERE Name='"+self.txt+"';"
        try:
            curgame.execute(sql)
            self.result=curgame.fetchall()
            print(self.result)
            if self.result==[]:
                self.error_screen.showMessage('!! No Team with this name')
                self.error_screen.exec_()
                self.openscreen.show();
            mygame.commit()
            for i in range(len(self.result)):
                item=QtWidgets.QListWidgetItem(self.result[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.l2.addItem(item)
            self.openscreen.hide()
            self.flag=0
            for i in range(self.l2.count()):
                self.cal_points(self.l2.item(i).text())
            
            self.b1.clicked.connect(self.batsman)
            self.b2.clicked.connect(self.bowlers)
            self.b3.clicked.connect(self.allrounders)
            self.b4.clicked.connect(self.wktkeepers)

        except:
            self.error_screen.showMessage('!! Operation unsuccessfull')
            self.error_screen.exec_()
            mygame.rollback()

        
#Players list        

    def batsman(self,selected):
        sql="SELECT Player from Stats WHERE category='BAT';"
        if selected:
            try:
                curgame.execute(sql)
                self.l1.clear()
                batsman=curgame.fetchall()
                mygame.commit()
                for i in range(len(batsman)):
                    item=QtWidgets.QListWidgetItem(batsman[i][0])
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    self.l1.addItem(item)

            except:
                self.error_screen.showMessage('!! Operation unsuccessfull')
                self.error_screen.exec_()
                mygame.rollback()

    def bowlers(self,selected):
        sql="SELECT Player from Stats WHERE category='BWL';"
        if selected:
            try:
                curgame.execute(sql)
                self.l1.clear()
                bowlers=curgame.fetchall()
                mygame.commit()
                for i in range(len(bowlers)):
                    item=QtWidgets.QListWidgetItem(bowlers[i][0])
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    self.l1.addItem(item)

            except:
                self.error_screen.showMessage('!! Operation unsuccessfull')
                self.error_screen.exec_()
                mygame.rollback()

    def allrounders(self,selected):
        sql="SELECT Player from Stats WHERE category='AR';"
        if selected:
            try:
                curgame.execute(sql)
                self.l1.clear()
                ar=curgame.fetchall()
                mygame.commit()
                for i in range(len(ar)):
                    item=QtWidgets.QListWidgetItem(ar[i][0])
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    self.l1.addItem(item)

            except:
                self.error_screen.showMessage('!! Operation unsuccessfull')
                self.error_screen.exec_()
                mygame.rollback()

    def wktkeepers(self,selected):
        sql="SELECT Player from Stats WHERE category='WK';"
        if selected:
            try:
                curgame.execute(sql)
                self.l1.clear()
                wk=curgame.fetchall()
                mygame.commit()
                for i in range(len(wk)):
                    item=QtWidgets.QListWidgetItem(wk[i][0])
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    self.l1.addItem(item)

            except:
                self.error_screen.showMessage('!! Operation unsuccessfull')
                self.error_screen.exec_()
                mygame.rollback()
    
        
#select and drop players

    def rlist1(self,item):
        self.flag=0
        self.l1.takeItem(self.l1.row(item))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.l2.addItem(item)
        self.totalplayers=self.l2.count()
        self.cal_points(item.text())
        if self.b1.isChecked()==True:
            self.batsmancount+=1
            self.error()
            self.t1.setText(str(self.batsmancount))
        if self.b2.isChecked()==True:
            self.bowlerscount+=1
            self.error()
            self.t2.setText(str(self.bowlerscount))
        if self.b3.isChecked()==True:
            self.arcount+=1
            self.error()
            self.t3.setText(str(self.arcount))
        if self.b4.isChecked()==True:
            self.wkcount+=1
            self.error()
            self.t4.setText(str(self.wkcount))
                
    def rlist2(self,item):
        self.flag=1
        self.l2.takeItem(self.l2.row(item))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.l1.addItem(item)
        self.totalplayers=self.l2.count()
        self.cal_points(item.text())
        if self.b1.isChecked()==True:
            self.batsmancount-=1
            self.error()
            self.t1.setText(str(self.batsmancount))
        if self.b2.isChecked()==True:
            self.bowlerscount-=1
            self.error()
            self.t2.setText(str(self.bowlerscount))
        if self.b3.isChecked()==True:
            self.arcount-=1
            self.error()
            self.t3.setText(str(self.arcount))
        if self.b4.isChecked()==True:
            self.wkcount-=1
            self.error()
            self.t4.setText(str(self.wkcount))

#Calculating points

    def cal_points(self,item):
        sql="SELECT Value from Stats WHERE Player='"+str(item)+"';"
        
        try:
            curgame.execute(sql)
            record=curgame.fetchone()
            mygame.commit()
            if self.flag==0:
                self.points_available-=int(record[0])
                self.points_used+=int(record[0])
            elif self.flag==1:
                self.points_available+=int(record[0])
                self.points_used-=int(record[0])
            self.t5.setText(str(self.points_available))
            self.t6.setText(str(self.points_used))

        except:
                self.error_screen.showMessage('!! Operation unsuccessfull')
                self.error_screen.exec_()
                mygame.rollback()

#Saving file

    def save_file(self):
        for i in range(self.l2.count()):
            self.items.append(str(self.l2.item(i).text()))
        player_score=[]
        try:
            for player in self.items:
                curgame.execute("SELECT * from Match WHERE Player='"+player+"';")
                self.record=curgame.fetchone()
                mygame.commit()
                player_score.append(player_scores(self.record))
                
            for i in range(len(self.items)):
                curgame.execute("INSERT INTO Teams('Name','Players','Value') VALUES ('%s','%s','%d');"%(self.newteam_name,self.items[i],player_score[i]))
                mygame.commit()

        except:
          self.error_screen.showMessage('!! Operation unsuccessfull')
          self.error_screen.exec_()
          mygame.rollback()

#Evaluate action

    def eval_screen(self):
        self.evalscreen.show()

    def combobox1(self):
        self.eval_object.cb1.currentTextChanged.connect(self.combobox2)

    def combobox2(self):
        team=self.eval_object.cb_2.currentText()

        self.eval_object.listWidget.clear()
        self.eval_object.listWidget_2.clear()
        try:
            curgame.execute("SELECT Players from Teams WHERE Name='"+team+"';")
            record=curgame.fetchall()
            mygame.commit()
            for i in range(len(record)):
                item= QtWidgets.QListWidgetItem(record[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.eval_object.listWidget.addItem(item)
            
            curgame.execute("SELECT Value from Teams WHERE Name='"+team+"';")
            record=curgame.fetchall()
            mygame.commit()
            self.totalscore=[]
            for i in range(len(record)):
                self.totalscore.append(record[i][0])
                item= QtWidgets.QListWidgetItem(str(record[i][0]))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.eval_object.listWidget_2.addItem(item)
                
            self.eval_object.label_2.setText(str(sum(self.totalscore)))
            

        except:
          self.error_screen.showMessage('!! Operation unsuccessfull')
          self.error_screen.exec_()
          mygame.rollback()
        

    def closeevalscreen(self):
        self.evalscreen.close()
        
        
#Errors

    def error(self):

        if self.batsmancount>=0 and self.batsmancount<6:
            pass
        else:
            self.error_screen.showMessage('!!Only five batsman are allowed in one team')
            self.error_screen.exec_()

        if self.bowlerscount>=0 and self.bowlerscount<6:
            pass
        else:
            self.error_screen.showMessage('!!Only five bowlers are allowed in one team')
            self.error_screen.exec_()

        if self.wkcount>=0 and self.wkcount<2:
            pass
        else:
            self.error_screen.showMessage('!!You should have atleast one wicket keeper in your team')
            self.error_screen.exec_()

        if self.arcount>=0 and self.arcount<3:
            pass
        else:
            self.error_screen.showMessage('!! Only two all rounders are allowed')
            self.error_screen.exec_()
            
        if self.totalplayers>=0 and self.totalplayers<12:
            pass
        else:
            self.error_screen.showMessage('!!Team requirments not fullfilled')
            self.error_screen.exec_()

        if self.points_available>=0 and self.points_used<=1000:
            pass
        else:
            self.error_screen.showMessage('!! You have only 1000 points')
            self.error_screen.exec_()

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fantasy_Cricket = QtWidgets.QMainWindow()
    ui = Ui_Fantasy_Cricket()
    ui.setupUi(Fantasy_Cricket)
    Fantasy_Cricket.show()
    sys.exit(app.exec_())
