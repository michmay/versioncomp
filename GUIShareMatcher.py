# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from modShareMatcher import *
import sharescraper
import pandas as pd
import numpy as np
import datetime
import os
import sys
import time
from commentImporter import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(211, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tabClients = QtWidgets.QWidget()
        self.tabClients.setObjectName("tabClients")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabClients)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tabClients)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.listWidget = QtWidgets.QListWidget(self.tabClients)
        self.listWidget.setObjectName("listWidget")
        """
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        """
        self.verticalLayout_4.addWidget(self.listWidget)
        self.lineEdit.raise_()
        self.listWidget.raise_()
        self.tabWidget.addTab(self.tabClients, "")
        self.tabShares = QtWidgets.QWidget()
        self.tabShares.setObjectName("tabShares")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabShares)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tabShares)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.tabShares)
        self.listWidget_2.setObjectName("listWidget_2")

        """
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        """
        
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.tabWidget.addTab(self.tabShares, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.display_data)
    
        self.inst = shareComments('AAA PORTFOLIOVALUE-2016-08-16_2016-08-16.xlsx')
        
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(23)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")

        
        
        self.pushButton.clicked.connect(self.save_file)

        #self.saveAction = QtWidgets.QAction(MainWindow)
        #self.saveAction.setShortcut("Ctrl+S")
        #self.saveAction.clicked.connect(save_file)

        
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionUpdate)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionUpdate.triggered.connect(self.update_data)

        msg = QtWidgets.QMessageBox.question(MainWindow,'Message',
            "Use live ASX data?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
##        msg.setText("Use live share data?")
##        msg.setWindowTitle("Live")
##        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if msg == QtWidgets.QMessageBox.Yes:
            self.liveData = True
        if msg == QtWidgets.QMessageBox.No:
            self.liveData = False

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        allclients()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        clientlist = allclients()
        for i in range(len(clientlist)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            item = self.listWidget.item(i)
            item.setText(_translate("MainWindow",str(clientlist[i])))
        """
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "one"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "two"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "three"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "four"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "five"))"""
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabClients), _translate("MainWindow", "Clients"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)

        allsharelist = allshares()
        for i in range(len(allsharelist)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget_2.addItem(item)
            
            item = self.listWidget_2.item(i)
            item.setText(_translate("MainWindow",str(allsharelist[i])))
        """
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "one"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "two"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "three"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "four"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "five"))

        """

        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.listWidget_2.sortItems()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabShares), _translate("MainWindow", "Shares"))
        self.pushButton_2.setText(_translate("MainWindow", ">>"))

        """
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row")) """
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Share"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "$ Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Role in Portf"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Maximum Exposure"))
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        
        

        self.rewrite_table()

        """
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "one"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "two"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "threee"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "threagain"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "five"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "six"))
        """
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        #self.actionUpdate.triggered.connect(self.update_data)

        
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        print(self.tableWidget.rowCount())

    def rewrite_table(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "one"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "two"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "threee"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "threagain"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "five"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "six"))

        print(self.tableWidget.horizontalHeaderItem(1).text())
        print(self.tableWidget.columnCount())
        print(self.tableWidget.item(2,0).text())

        
    
        

    def update_data(self,direc):


        
        import modBatchImport

        founf = modBatchImport.imp_data()

        msg = QtWidgets.QMessageBox()
        msg.setText("Updated!")
        msg.setWindowTitle("Update!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()

        
        
    def display_data(self):
        _translate = QtCore.QCoreApplication.translate
        print("tab test")
        if self.tabWidget.currentIndex()==0:
            print(self.tableWidget.horizontalHeaderItem(1).text())
            self.displayingClients = True
            #throw a clients shares to table
            print('currently on client tab')
            print(self.listWidget.currentItem().text())

            while (self.tableWidget.rowCount() > 0) :   #clear table
                    self.tableWidget.removeRow(0)

            client = self.listWidget.currentItem().text()

            share_list = portfolio(client)
            print(len(share_list))
            
            self.progbar = QtWidgets.QProgressBar()
            
            self.progbar.setMinimum(0)
            self.progbar.setMaximum(len(share_list)-1)
            self.progbar.setGeometry(200, 80, 250, 20)
            
            self.progbar.show()
            
            for i in range(len(share_list)):
                
                
        
                if self.tableWidget.rowCount() < len(share_list):
                    self.tableWidget.insertRow(i)

                item = QtWidgets.QTableWidgetItem(client)
                self.tableWidget.setItem(i, 0, item)   

                item = QtWidgets.QTableWidgetItem(share_list[i])
                self.tableWidget.setItem(i, 1, item)

                if self.liveData :
                    try:
                        curprice = sharescraper.shareprice(share_list[i])
                        price = '$'+str(curprice)

                        pass
                    except:
                        price = 999
                        pass

                    item = QtWidgets.QTableWidgetItem(str(price))
                    self.tableWidget.setItem(i, 2, item)

                try:
                    item = QtWidgets.QTableWidgetItem(self.inst.comm(share_list[i].upper()))
                    self.tableWidget.setItem(i, 3, item)
                except Exception as e:
                    print(str(e))
                    self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem('error'))

                QtWidgets.QApplication.processEvents()
                self.progbar.setValue(i)
                if i == len(share_list)-1:
                    self.progbar.hide()
                
        elif self.tabWidget.currentIndex() == 1:
            self.displayingClients = False
            #throw owners of ticker to table
            print('currently on share tab')
            print(self.listWidget_2.currentItem().text())

            ticker = self.listWidget_2.currentItem().text()
            

            if self.liveData :
                try:
                    curprice = sharescraper.shareprice(ticker)
                    price = '$'+str(curprice)
                    pass
                except:
                    price = 999
                    pass

            owns_share = inshares(ticker)

            owns_share.sort()
        
            while (self.tableWidget.rowCount() > 0) :
                    self.tableWidget.removeRow(0)


            self.progbar = QtWidgets.QProgressBar()
            
            self.progbar.setMinimum(0)
            self.progbar.setMaximum(len(owns_share)-1)
            self.progbar.setGeometry(200, 80, 250, 20)
            
            self.progbar.show()
            
            for i in range(len(owns_share)):
                
                                    
                if self.tableWidget.rowCount() < len(owns_share):
                    self.tableWidget.insertRow(i)
                    

                item = QtWidgets.QTableWidgetItem(owns_share[i])
                self.tableWidget.setItem(i, 0, item)

                item = QtWidgets.QTableWidgetItem(ticker)
                self.tableWidget.setItem(i, 1, item)
                if self.liveData:
                    item = QtWidgets.QTableWidgetItem(str(price))
                    self.tableWidget.setItem(i, 2, item)
                try:
                    item = QtWidgets.QTableWidgetItem(self.inst.comm(owns_share[i].upper()))
                    self.tableWidget.setItem(i, 3, item)
                except:
                    self.tableWidget.setItem(i, 3,QtWidgets.QTableWidgetItem('error'))
                """ insert share comment here"""
        
                #item = inst.comm(ticker.upper())
                                
                    
                QtWidgets.QApplication.processEvents()
                self.progbar.setValue(i)
                if i == len(owns_share)-1:
                    self.progbar.hide()
                            
    def save_file(self):
        tabledata = [[] for i in range(self.tableWidget.rowCount())]
        

        for j in range(self.tableWidget.columnCount()):
            #print('j = '+str(j))
            
            for i in range(self.tableWidget.rowCount()):
                #print('i = '+str(i))
                try:
                    tabledata[i].append(self.tableWidget.item(i,j).text())
                except:
                    tabledata[i].append("")

        #print(tabledata)
                    
        df = pd.DataFrame(tabledata,columns = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())])
        
        if self.displayingClients:
            name = self.tableWidget.item(0,0).text() +'_'+ str(datetime.date.today())
            
            print(name)
        elif not self.displayingClients:
            name = self.tableWidget.item(0,1).text()+'_'+ str(datetime.date.today())
            
            print(name)
        else:
            name = str(datetime.date.today())
            print(name)
 
        saveCsvName = QtWidgets.QFileDialog.getSaveFileName(MainWindow,"Save Table", name,"CSV (*.csv)") #mainwindow was the needed expression, not self

        print(saveCsvName)

        
        if saveCsvName[1] is not '':

            paths = os.path.split(saveCsvName[0])

            df.to_csv(saveCsvName[0],index=False)
            msg = QtWidgets.QMessageBox()
            msg.setText("Saved to:\n "+saveCsvName[0])
            msg.setWindowTitle("Saved!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            
        if saveCsvName[1] == '':
            
            msg = QtWidgets.QMessageBox()
            msg.setText("Not saved")
            msg.setWindowTitle("Cancelled!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
        
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

