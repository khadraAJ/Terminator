#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 00:22:54 2018

@author: skaering
"""
import sys
#import QtGui
from fonctions_terminator import loadings
from PyQt5.QtWidgets import QTableWidget,QApplication,QMainWindow,QTableWidgetItem,QLineEdit,QCheckBox,QGridLayout,QComboBox,QItemDelegate#,pyqtSignal

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
        #loads all the values of organs, properties, values, modifiers and relatives
        self.listsForCombobox()

    #the line is enable/disable if the validated checkbox statut changes
    def handleCellClicked(self, row, column):
        clickedCell = self.item(row, column)
        if (clickedCell.text() == '' and column == 5):
            if clickedCell.checkState() == QtCore.Qt.Checked:
                self.disableLine(row)
            else:
                self.enableLine(row)

    #disables a cell and colors it in green                
    def disableCell(self, row, col):
        self.cellWidget(row,col).setStyleSheet(("QComboBox { background-color: rgb(124, 252, 0)}"))
        self.cellWidget(row,col).setEnabled(False)
#        cell = self.item(row, col)
#        flags = cell.flags()
#        flags = flags & ~QtCore.Qt.ItemIsSelectable
#        flags = flags & ~QtCore.Qt.ItemIsEditable
#        flags = flags & ~QtCore.Qt.ItemIsEnabled
#        cell.setBackground(QtGui.QColor(135, 233, 144))
#        cell.setFlags(flags)
#        self.setItem(row, col, QTableWidgetItem(cell))

    #disables a line and colors it in green        
    def disableLine(self, row):
        for i in range(1,5):
            self.disableCell(row,i)

    #enables a cell and colors it in white             
    def enableCell(self, row, col):
        self.cellWidget(row,col).setStyleSheet(("QComboBox { background-color: rgb(255, 255, 255)}"))
        self.cellWidget(row,col).setEnabled(True)
#        cell = self.item(row, col)
#        cell.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
#        cell.setBackground(QtGui.QColor(255, 255, 255))
#        self.setItem(row, col, QTableWidgetItem(cell))
        
    #enables a line and colors it in white        
    def enableLine(self, row):
        for i in range(1,5):
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

    #displays the triads in the table when the user clicks on Next in Execute 
    #WARNING changer la valeur de la cellule actuelle lorsque l'on clique sur une
#combobox sinon lors de la suppression de ligne, la mauvaise sera supprimée  
    #WARNING chaque fois que l'on clique sur une checkbox la cellule selectionée change
    def setValue1 (self,ligne,value,value1,value2,value3):
        #defined actions 
        slotOrgans = lambda: self.handleCombo(ligne,1)
        slotProperties = lambda: self.handleCombo(ligne,2)
        slotValues = lambda: self.handleCombo(ligne,3)
        slotModifiers = lambda: self.handleCombo(ligne,4)
        
        selectCheckBox=QTableWidgetItem()
        selectCheckBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        selectCheckBox.setCheckState(QtCore.Qt.Unchecked)
        self.setItem(ligne,0,selectCheckBox)
        
        #comboboxes creation
        comboOrgans = QComboBox()
        comboOrgans.addItems(self.organs)
        comboOrgans.setCurrentIndex(self.findIndex(1,value))
        comboOrgans.currentIndexChanged.connect(slotOrgans)
        self.setCellWidget(ligne,1,comboOrgans)
        
        comboProperties = QComboBox()
        comboProperties.addItems(self.properties)
        comboProperties.setCurrentIndex(self.findIndex(2,value1))
        comboProperties.currentIndexChanged.connect(slotProperties)
        self.setCellWidget(ligne,2,comboProperties)
        
        comboValues = QComboBox()
        comboValues.addItems(self.values)
        comboValues.setCurrentIndex(self.findIndex(3,value2))
        comboValues.currentIndexChanged.connect(slotValues)
        self.setCellWidget(ligne,3,comboValues)
        
        
        comboModifiers = QComboBox()
        comboModifiers.addItems(self.modifiers)
        comboModifiers.setCurrentIndex(self.findIndex(4,value3))
        comboModifiers.currentIndexChanged.connect(slotModifiers)
        self.setCellWidget(ligne,4,comboModifiers)
        
        

            
        val=QTableWidgetItem(value)
        self.setCurrentCell(ligne,1)
        self.setItem(ligne,1,QTableWidgetItem(val))
        self.setCurrentCell(ligne,2)
        val=QTableWidgetItem(value1)
        self.setItem(ligne,2,QTableWidgetItem(val))
        self.setCurrentCell(ligne,3)
        val=QTableWidgetItem(value2)
        self.setItem(ligne,3,QTableWidgetItem(val))
        self.setCurrentCell(ligne,4)
        val=QTableWidgetItem(value3)
        self.setItem(ligne,4,QTableWidgetItem(val))
        valCheckBox=QTableWidgetItem()
        valCheckBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        valCheckBox.setCheckState(QtCore.Qt.Unchecked)
        self.setItem(ligne,5,valCheckBox)
        

    
    #removes all the selected rows 
    def deleteLines (self):
        deletion = False
        for i in reversed(range (self.rowCount())):
            clickedCell = self.item(i, 0)
            if clickedCell.checkState() == QtCore.Qt.Checked:
                self.removeRow(i)
                deletion = True
        return deletion
    
    #removes all the rows in the table except the head of the table
    def resetTable (self):
        lines = self.rowCount()
        for i in reversed(range(lines)):
            self.removeRow(i)
       

    def dropdownList (self):
        alist = QComboBox()
        alist.insertItem(0,"coucou")
        cell = QTableWidgetItem(alist)
        if not self.parent().indexWidget(1):
            self.parent().setIndexWidget(1,alist)
        return cell

    @QtCore.pyqtSlot()      
    def handleCombo(self, row, column):
        print("Vous venez de changer la liste de la case ({},{})".format(row,column))
        print("Nouvelle valeur : "+self.cellWidget(row,column).currentText())
        
    def listsForCombobox(self):
        self.modifiers, organsDico, propertiesAndValues, self.relatives = loadings()
        self.modifiers.insert(0,"none")
        
        self.organs = []
        for i in organsDico.keys():
            self.organs.append(i)
        self.organs.insert(0,"none")
        
        self.properties = []
        for i in propertiesAndValues.keys():
            self.properties.append(i)
        self.properties.insert(0,"none")
        
        self.values = []
        for i in propertiesAndValues.values():
            for j in i:
                self.values.append(j) 
        self.values.insert(0,"none")
        print (self.values)

    def findIndex(self, row, val):
         if(row == 1):
             for i in self.organs:
                 if(i == val):
                     return self.organs.index(val)
             return 0
         else:
             if (row == 2):
                 for i in self.properties:
                     if(i == val):
                         return self.properties.index(val)
                 return 0
             else:
                 if (row == 3):
                     for i in self.values:
                         if(i == val):
                             return self.values.index(val)
                     return 0
                 else:
                     if (row == 4):
                         for i in self.modifiers:
                             if(i == val):
                                 return self.modifiers.index(val)
                         return 0
        
        
        
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
