#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 00:22:54 2018

@author: skaering
"""
import sys
#import QtGui

from PyQt5.QtWidgets import QTableWidget,QApplication,QMainWindow,QTableWidgetItem,QLineEdit,QCheckBox,QGridLayout#,pyqtSignal

from PyQt5 import QtCore

from PyQt5 import QtGui
class Mytable (QTableWidget):

    # def _init_(self,rows,columns):
    #     super().__init__(rows,columns)
    #     self.form_widget =Mytable(0,2)
    #     self.setCentralWidget(self.form_widget)
    #     self.show()
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.cellClicked.connect(self.handleCellClicked)

    def handleCellClicked(self, row, column):
        clickedCell = self.item(row, column)
        if (clickedCell.text() == ''):
            if clickedCell.checkState() == QtCore.Qt.Checked:
                self.disableLine(row)
            else:
                self.enableLine(row)
    def disableCell(self, row, col):
        cell = self.item(row, col)
        flags = cell.flags()
        flags = flags & ~QtCore.Qt.ItemIsSelectable
        flags = flags & ~QtCore.Qt.ItemIsEditable
        flags = flags & ~QtCore.Qt.ItemIsEnabled
        cell.setBackground(QtGui.QColor(135, 233, 144))
        cell.setFlags(flags)
        self.setItem(row, col, QTableWidgetItem(cell))
    def disableLine(self, row):
        for i in range(3):
            self.disableCell(row,i)
    def enableCell(self, row, col):
        cell = self.item(row, col)
        cell.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
        cell.setBackground(QtGui.QColor(255, 255, 255))
        self.setItem(row, col, QTableWidgetItem(cell))
    def enableLine(self, row):
        for i in range(3):
            self.enableCell(row, i)
    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        
    def c_current(self):
        row=self.clickedRow()
        col=self.currentColumn()
        value=self.item(row,col)
        value=value#.text()
        
    def setValue (self,ligne,colonne, value):
        val=QTableWidgetItem(value)
        self.setCurrentCell(ligne,colonne)
        self.setItem(ligne,colonne,QTableWidgetItem(val))
        
    def addRow (self):
        
        self.setRowCount(self.rowCount()+1)
    def setValue1 (self,ligne,value,value1,value2):
        val=QTableWidgetItem(value)
        self.setCurrentCell(ligne,0)
        self.setItem(ligne,0,QTableWidgetItem(val))
        self.setCurrentCell(ligne,1)
        val=QTableWidgetItem(value1)
        self.setItem(ligne,1,QTableWidgetItem(val))
        self.setCurrentCell(ligne,2)
        val=QTableWidgetItem(value2)
        self.setItem(ligne,2,QTableWidgetItem(val))
        
        ##############################
        # zone test checkbox
        ##############################
        valCheckBox=QTableWidgetItem()
        valCheckBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        valCheckBox.setCheckState(QtCore.Qt.Unchecked)
        self.setItem(ligne,3,valCheckBox)
       # wdg = QtGui.QWidget()
        ##############################
        # code de la checkbox
        ########################
       # box =QTableWidgetItem( QCheckBox)
        #box.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled )
        #box.setEnabled(True)
        #box.setFlags(QtCore.Qt.ItemIsEnabled)
        #box.setCheckState(QtCore.Qt.Unchecked)       
        #box.clicked.connect(self.handleItemClicked)
        #self.setCurrentCell(ligne,3)
        
       # self.setItem(ligne,3,box)
        
        #self.setCellWidget(ligne,3, box)
        #self.setCellWidget(ligne,3,box).setLayout(layout)
        #######################################
        ######################################
        #self.setRowCount(self.rowCount()+1)
        #form_widget
    def deleteLine (self,row):
        self.removeRow(self.clickedRow())
        
    def resetTable (self):
        lines = self.rowCount()
        print(lines)
        for i in range(lines):
            self.removeRow(i)
       
        
    #def handleItemClicked(box):
      #  if box.checkState()==QtCore.Qt.Checked:
         #   print('"%s"validated'%box.text())
            
#class Sheet(QMainWindow):
#    def _init_(self):
#        super().__init__()
#        self.form_widget=Mytable(100,3)
#        self.setCentralWidget(self.form_widget)
#        self.show()
#app= QApplication(sys.argv)
#table=Mytable(3,100)  
#sheet= Sheet()
#sys.exit(app.exec_())   
