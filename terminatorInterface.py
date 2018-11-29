# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Terminator_Interface_05.03.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import csv
import datetime
#import Main1103
from MyTable import Mytable
from fonctions_terminator import pseudo_main
#from Import_script import opening
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QHeaderView, QWidget, QLabel, QApplication, QWidget, QPushButton, QMessageBox

class Ui_MainWindow(object):
    app = QtWidgets.QApplication(sys.argv)
    buffer= []
    listBuffer=[]
    def addTriad(self):
        self.tableViewResultExecute.addRow()
##############################################################################
            ###Saving method 
    def creationFichier (self):
        D=datetime.date.today()
        X=D.strftime('%Y_%m_%d')
        nomFichier="Terminator_" + X + ".txt"
        obj = open(nomFichier, 'w') ## Opening the file in writting
       ## adding of label informations in the file
        obj.write("                             TERMINATOR                          ")
        obj.write("\n\n\n")
        obj.write(X)
        obj.write("\n\n\n")
        obj.write("Ref N°:")
        obj.write(self.lineEditRefNum.text())
        obj.write("\n\n")
        obj.write("Specie Number:")
        obj.write(self.lineEditSpeciesNum.text())
        obj.write("\n\n")
        obj.write("Rec N°:")
        obj.write(self.labelRecNum.text())
        obj.write("\n\n")
        obj.write("Genus:")
        obj.write(self.labelGenus.text())
        obj.write("\n\n")
        obj.write("Specie Name:")
        obj.write(self.lineEditSpecies.text())
        obj.write("\n\n")
        obj.write("Population:")
        obj.write(self.lineEditPopulation.text())
        obj.write("\n\n")
        obj.write("Stage:")
        obj.write(self.lineEditAge.text())
        obj.write("\n\n")
        obj.write("Sex:")
        obj.write(self.lineEditSex.text())
        obj.write("\n\n\n")
        obj.write("Locality:")
        obj.write(self.lineEditLocality.text())
        obj.write("\n\n\n")
        obj.write("Host:")
        obj.write(self.lineEditHost.text())
        obj.write("\n\n\n")
        obj.write(self.textEditPublishedDescription.toPlainText()) ## Adding  of the original text into the file
        ## adding of the triads
        obj.write("\n\n\n")
        obj.write("Triades Generated:")
        obj.write("\n\n\n")
        for i in range(self.tableViewResultExecute.rowCount()):
            
            triad=[]
            triad.append("           ")
            triad.append( self.tableViewResultExecute.item(i,0).text())
            c=0
            for c in range(len(self.tableViewResultExecute.item(i,0).text())):
                c+=1
            for z in range (60-c):
                triad.append(" ")
            triad.append(self.tableViewResultExecute.item(i,1).text())
            c=0
            for c in range (len(self.tableViewResultExecute.item(i,1).text())):
                c+=1
            for e in range (60-c):
                triad.append(" ")
            triad.append(self.tableViewResultExecute.item(i,2).text())
            stringTampon="".join(triad)
            obj.write(stringTampon)
            obj.write("\n")
            triad=[]
        obj.close()

################################################################################
   ###########################################################
   #méthode pour le bouton undo a corriger 
   ############################################################
    def undo1(self):
        self.tableViewResultExecute.addRow()
        buffer1=self.listBuffer[len(self.listBuffer)-1]
        i=self.tableViewResultExecute.rowCount()
        print("i:")
        print(i)
        
        organ=buffer1[0]
        properti=buffer1[1]
        value=buffer1[2]
        self.tableViewResultExecute.setValue1((i-1),organ,properti,value)
        self.tableViewResultExecute.update()
        del self.listBuffer[-1]
    
    ##################################################
    #méthode bouton delete ok 
    #################################################
    def deleteTriad(self):
        self.buffer.append(self.tableViewResultExecute.item(self.tableViewResultExecute.row(self.tableViewResultExecute.currentItem()),0).text())
        print("Buffer après premier ajout"+self.buffer[0])
        self.buffer.append(self.tableViewResultExecute.item(self.tableViewResultExecute.row(self.tableViewResultExecute.currentItem()),1).text())
        print("Buffer après seond ajout"+self.buffer[1])
        self.buffer.append(self.tableViewResultExecute.item(self.tableViewResultExecute.row(self.tableViewResultExecute.currentItem()),2).text())
        print("Buffer après troisieme ajout"+self.buffer[2])
        
        self.listBuffer.append(self.buffer)
        print("liste buffer après ajout")
        print(self.listBuffer)
        self.buffer=[]
        self.tableViewResultExecute.deleteLine(self.tableViewResultExecute.row((self.tableViewResultExecute.currentItem())));
    #############################################
    # méthode bouton next ok 
    ############################################
    def boutonNext(self):
        #On ne peut pas cliquer sur next si Published description est vide
        if(self.textEditPublishedDescription.toPlainText() != ""):
            self.tab.setCurrentIndex(2)
            self.processImport()
            self.labelEmptyField.setText("")
        else: self.labelEmptyField.setText("The field Published Description cannot be empty.")
        
    # dégrise le bouton next
    def enableNextButton(self):
        self.pushButtonNext.setEnabled(True);

############################################################
    def open_dialog(self):
        dialog = QtWidgets.QDialog()
        # dialog.ui = Form()
        # dialog.ui.setupUi(dialog)
        # dialog.exec_()
        dialog.show()

    def processImport(self):
        dicotampon = pseudo_main(self.textEditPublishedDescription.toPlainText())
        # dicoOrgans = opening('organsList') # on charge le dictionnaire contenant les organes et leurs synonymes
        # valuesDico = opening('valuesDico') # on charge le dico contenant les valeurs et leurs synonymes
        tampon = self.textEditPublishedDescription.toPlainText()
        self.textEditPublishedDescriptionExecutePage.clear()
        # self.textEditPublishedDescriptionExecutePage.insertPlainText(tampon)
        i = 0

        for key, value in dicotampon.items():
            print(key)
            self.textEditPublishedDescriptionExecutePage.insertPlainText(key)
            if (value):
                for j in range(len(value)):
                    self.tableViewResultExecute.addRow()
                    # self.tableViewResultExecute.setRowCount(self.tableViewResultExecute.rowCount()+1)
                    x = value[j]
                    organ = x[0]
                    prop = x[1]
                    val = x[2]
                    self.tableViewResultExecute.setValue1(i, organ, prop, val)
                    i += 1


    def setupUi(self, MainWindow):
        ## setting of the window and the home page 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 676)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setToolTipDuration(-5)
        self.tab.setObjectName("tab")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.home_page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layoutHome = QtWidgets.QVBoxLayout()
        self.layoutHome.setObjectName("layoutHome")
        self.labelHome1 = QtWidgets.QLabel(self.home_page)
        self.labelHome1.setObjectName("labelHome1")
        self.layoutHome.addWidget(self.labelHome1)
        self.labelHome2 = QtWidgets.QLabel(self.home_page)
        self.labelHome2.setObjectName("labelHome2")
        self.layoutHome.addWidget(self.labelHome2)
        self.horizontalLayout.addLayout(self.layoutHome)
        self.tab.addTab(self.home_page, "")
        self.importText_page = QtWidgets.QWidget()
        self.importText_page.setToolTip("")
        
        ## import text part 
        self.importText_page.setObjectName("importText_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.importText_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layoutImportText1 = QtWidgets.QVBoxLayout()
        self.layoutImportText1.setObjectName("layoutImportText1")
        self.layoutImportText2 = QtWidgets.QFormLayout()
        self.layoutImportText2.setObjectName("layoutImportText2")
        
        
        self.layoutImportText3 = QtWidgets.QFormLayout()
        self.layoutImportText3.setObjectName("layoutImportText3")
        self.labelRefNum = QtWidgets.QLabel(self.importText_page)
        

        ##ref num
        self.labelRefNum.setObjectName("labelRefNum")
        self.layoutImportText3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelRefNum)
        self.lineEditRefNum = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditRefNum.setObjectName("lineEditRefNum")
        self.layoutImportText3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditRefNum)
       
        ## specie num
        self.labelSpeciesNum = QtWidgets.QLabel(self.importText_page)
        self.labelSpeciesNum.setObjectName("labelSpeciesNum")
        self.layoutImportText3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelSpeciesNum)
        self.lineEditSpeciesNum = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditSpeciesNum.setObjectName("lineEditSpeciesNum")
        self.layoutImportText3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditSpeciesNum)
       
        ## rec num 
        self.labelRecNum = QtWidgets.QLabel(self.importText_page)     
        self.labelRecNum.setObjectName("labelRecNum")
        self.layoutImportText3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelRecNum)
        self.lineEditRecNum = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditRecNum.setObjectName("lineEditRecNum")
        self.layoutImportText3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditRecNum)
        
        ##genus
        self.labelGenus = QtWidgets.QLabel(self.importText_page)     
        self.labelGenus.setObjectName("labelGenus")
        self.layoutImportText3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelGenus)
        self.lineEditGenus = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditGenus.setObjectName("lineEditGenus")
        self.layoutImportText3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditGenus)
        
        #specie 
        self.labelSpecies = QtWidgets.QLabel(self.importText_page)
        self.labelSpecies.setObjectName("labelSpecies")
        self.layoutImportText3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelSpecies)
        self.lineEditSpecies = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditSpecies.setObjectName("lineEditSpecies")
        self.layoutImportText3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditSpecies)
        
        #population
        self.labelPopulation = QtWidgets.QLabel(self.importText_page)
        self.labelPopulation.setObjectName("labelPopulation")
        self.layoutImportText3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelPopulation)
        self.lineEditPopulation = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditPopulation.setObjectName("lineEditPopulation")
        self.layoutImportText3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEditPopulation)
        
        #sexe
        self.labelSex = QtWidgets.QLabel(self.importText_page)
        self.labelSex.setObjectName("labelSex")
        self.layoutImportText3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelSex)
        self.lineEditSex = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditSex.setObjectName("lineEditSex")
        self.layoutImportText3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEditSex)
        
        #stage
        self.labelAge = QtWidgets.QLabel(self.importText_page)
        self.labelAge.setObjectName("labelAge")
        self.layoutImportText3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.labelAge)
        self.lineEditAge = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditAge.setObjectName("lineEditAge")
        self.layoutImportText3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEditAge)

        #Locality
        self.labelLocality = QtWidgets.QLabel(self.importText_page)
        self.labelLocality.setObjectName("labelLocality")
        self.layoutImportText3.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.labelLocality)
        self.lineEditLocality = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditLocality.setObjectName("lineEditLocality")
        self.layoutImportText3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEditLocality)
        
        #Host
        self.labelHost = QtWidgets.QLabel(self.importText_page)
        self.labelHost.setObjectName("labelHost")
        self.layoutImportText3.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.labelHost)
        self.lineEditHost = QtWidgets.QLineEdit(self.importText_page)
        self.lineEditHost.setObjectName("lineEditHost")
        self.layoutImportText3.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEditHost)
        
        #espace entre age et published description
        spacerItem = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutImportText3.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        
        # zone de texte
        self.layoutImportText2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.layoutImportText3)
        self.layoutDescription = QtWidgets.QVBoxLayout()
        self.layoutDescription.setObjectName("layoutDescription")
        self.labelPublishedDescription = QtWidgets.QLabel(self.importText_page)
        self.labelPublishedDescription.setObjectName("labelPublishedDescription")
        self.layoutDescription.addWidget(self.labelPublishedDescription)
        
        #espace entre la zone de texte et les boutons
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutDescription.addItem(spacerItem1)
        
        
        self.textEditPublishedDescription = QtWidgets.QTextEdit(self.importText_page)
        self.textEditPublishedDescription.setObjectName("textEditPublishedDescription")
        self.layoutDescription.addWidget(self.textEditPublishedDescription)
        
        ##bouton next et import file:
        
        self.layoutImpotFileAndnextButtons = QtWidgets.QHBoxLayout()
        self.layoutImpotFileAndnextButtons.setObjectName("layoutImpotFileAndnextButtons")
        
        #import file bouton
        self.pushButtonImportFile = QtWidgets.QPushButton(self.importText_page)
        self.pushButtonImportFile.setObjectName("pushButtonImportFile")
        self.layoutImpotFileAndnextButtons.addWidget(self.pushButtonImportFile)
        
        #next bouton
        self.pushButtonNext = QtWidgets.QPushButton(self.importText_page)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.layoutImpotFileAndnextButtons.addWidget(self.pushButtonNext)
        
        ##link of the action to the button 
        self.pushButtonNext.clicked.connect(self.boutonNext)
        
        #Message quand Published description est vide
        self.labelEmptyField = QtWidgets.QLabel(self.importText_page)
        self.labelEmptyField.setObjectName("labelEmptyField")
        self.layoutImportText2.setWidget(30, QtWidgets.QFormLayout.LabelRole, self.labelEmptyField)

    
                       
        self.layoutDescription.addLayout(self.layoutImpotFileAndnextButtons)
        self.layoutImportText2.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.layoutDescription)
        self.layoutImportText1.addLayout(self.layoutImportText2)
        self.verticalLayout_2.addLayout(self.layoutImportText1)
        self.tab.addTab(self.importText_page, "")
        
        
        #execute_page
        self.execute_page = QtWidgets.QWidget()
        self.execute_page.setObjectName("execute_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.execute_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.layoutExecute1 = QtWidgets.QVBoxLayout()
        self.layoutExecute1.setObjectName("layoutExecute1")
        self.groupBoxExecute1 = QtWidgets.QGroupBox(self.execute_page)
        self.groupBoxExecute1.setObjectName("groupBoxExecute1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBoxExecute1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.layoutExecute2 = QtWidgets.QVBoxLayout()
        self.layoutExecute2.setObjectName("layoutExecute2")
        
        
        #################
        self.textEditPublishedDescriptionExecutePage = QtWidgets.QTextEdit(self.groupBoxExecute1)
        self.textEditPublishedDescriptionExecutePage.setObjectName("textEditPublishedDescriptionExecutePage")
        self.layoutExecute2.addWidget(self.textEditPublishedDescriptionExecutePage)
        self.layoutExecute3 = QtWidgets.QHBoxLayout()
        self.textEditPublishedDescriptionExecutePage.setDisabled(True);
        ###################
        
        
        self.layoutExecute3.setObjectName("layoutExecute3")
        self.layoutExecute2.addLayout(self.layoutExecute3)
        self.verticalLayout_13.addLayout(self.layoutExecute2)
        self.groupBoxExecute2 = QtWidgets.QGroupBox(self.groupBoxExecute1)
        self.groupBoxExecute2.setObjectName("groupBoxExecute2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBoxExecute2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.layoutExecute4 = QtWidgets.QVBoxLayout()
        self.layoutExecute4.setObjectName("layoutExecute4")
        
        
        
        ###########################
        # table of results
        self.tableViewResultExecute = Mytable(0,4)#QtWidgets.QTableView(self.groupBoxExecute2)
        colonne_header=["Organ","Property","Value","Validated"]#,"Validated:"
        self.tableViewResultExecute.setHorizontalHeaderLabels(colonne_header)
        header= self.tableViewResultExecute.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableViewResultExecute.setObjectName("tableViewResultExecute")
        self.layoutExecute4.addWidget(self.tableViewResultExecute)
       
        
        
        
       #############################
        self.layoutExecute5 = QtWidgets.QHBoxLayout()
        self.layoutExecute5.setObjectName("layoutExecute5")
        
            ################################
        # button delete
        ################################
        self.pushButtonDelete=QtWidgets.QPushButton(self.groupBoxExecute2)
        self.pushButtonDelete.setText("Delete Triad")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonDelete.clicked.connect(self.deleteTriad)
        self.layoutExecute5.addWidget(self.pushButtonDelete)
#        
        
        ################################
        # button add
        ################################
        self.pushButtonAdd=QtWidgets.QPushButton(self.groupBoxExecute2)
        self.pushButtonAdd.setText("Add Triad")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonAdd.clicked.connect(self.addTriad)
        self.layoutExecute5.addWidget(self.pushButtonAdd)

#        
       
        #button next
        self.pushButtonNext2=QtWidgets.QPushButton(self.groupBoxExecute2)
        self.pushButtonNext2.setText("Next")
        self.pushButtonNext2.setObjectName("pushButtonNext2")
        #self.pushButtonNext2.clicked.connect(self.addTriad) # nextTriad should be a function ?
        self.layoutExecute5.addWidget(self.pushButtonNext2)
        
        
        #button save
        self.pushButtonSaveExecute = QtWidgets.QPushButton(self.groupBoxExecute2)
        self.pushButtonSaveExecute.setObjectName("pushButtonSaveExecute")
        self.layoutExecute5.addWidget(self.pushButtonSaveExecute)
        self.layoutExecute4.addLayout(self.layoutExecute5)
        self.pushButtonSaveExecute.clicked.connect(self.creationFichier)
        
        
        self.horizontalLayout_14.addLayout(self.layoutExecute4)
        self.verticalLayout_13.addWidget(self.groupBoxExecute2)
        self.layoutExecute1.addWidget(self.groupBoxExecute1)
        self.verticalLayout_5.addLayout(self.layoutExecute1)
        self.tab.addTab(self.execute_page, "")
        
        ## page schema
        self.schema_page = QtWidgets.QWidget()
        self.schema_page.setObjectName("schema_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.schema_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.layoutSchema1 = QtWidgets.QVBoxLayout()
        self.layoutSchema1.setObjectName("layoutSchema1")
        self.groupBoxSchema1 = QtWidgets.QGroupBox(self.schema_page)
        self.groupBoxSchema1.setObjectName("groupBoxSchema1")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.groupBoxSchema1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.layoutSchema2 = QtWidgets.QVBoxLayout()
        self.layoutSchema2.setObjectName("layoutSchema2")
        self.tableViewSchema = QtWidgets.QTableView(self.groupBoxSchema1)
        self.tableViewSchema.setObjectName("tableViewSchema")
        self.layoutSchema2.addWidget(self.tableViewSchema)
        self.layoutSchema3 = QtWidgets.QHBoxLayout()
        self.layoutSchema3.setObjectName("layoutSchema3")
        
        ## bouton add schema
        self.pushButtonAddSchema = QtWidgets.QPushButton(self.groupBoxSchema1)
        self.pushButtonAddSchema.setObjectName("pushButtonAddSchema")
        self.layoutSchema3.addWidget(self.pushButtonAddSchema)
        
        ##bouton modify schema
        self.pushButtoModifySchema = QtWidgets.QPushButton(self.groupBoxSchema1)
        self.pushButtoModifySchema.setObjectName("pushButtoModifySchema")
        self.layoutSchema3.addWidget(self.pushButtoModifySchema)
        
        ## bouton modifier un schema
        self.pushButtonDeleteSchema = QtWidgets.QPushButton(self.groupBoxSchema1)
        self.pushButtonDeleteSchema.setObjectName("pushButtonDeleteSchema")
        self.layoutSchema3.addWidget(self.pushButtonDeleteSchema)
        self.layoutSchema2.addLayout(self.layoutSchema3)
        self.horizontalLayout_16.addLayout(self.layoutSchema2)
        self.layoutSchema1.addWidget(self.groupBoxSchema1)
        self.verticalLayout_7.addLayout(self.layoutSchema1)
        self.tab.addTab(self.schema_page, "")
        self.verticalLayout_17.addWidget(self.tab)
        
        ## Partie export
        self.export_page = QtWidgets.QWidget()
        self.export_page.setObjectName("export_page")
        self.verticalLayout_77 = QtWidgets.QVBoxLayout(self.export_page)
        self.verticalLayout_77.setObjectName("verticalLayout_77")
        self.layoutSchema11 = QtWidgets.QVBoxLayout()
        self.layoutSchema11.setObjectName("layoutSchema11")
        self.groupBoxSchema11 = QtWidgets.QGroupBox(self.export_page)
        self.groupBoxSchema11.setObjectName("groupBoxSchema11")
        self.horizontalLayout_166 = QtWidgets.QHBoxLayout(self.groupBoxSchema11)
        self.horizontalLayout_166.setObjectName("horizontalLayout_166")
        self.layoutSchema22 = QtWidgets.QVBoxLayout()
        self.layoutSchema22.setObjectName("layoutSchema22")
        self.tableViewSchema = QtWidgets.QTableView(self.groupBoxSchema11)
        self.tableViewSchema.setObjectName("tableViewSchema")
        self.layoutSchema22.addWidget(self.tableViewSchema)
        self.layoutSchema33 = QtWidgets.QHBoxLayout()
        self.layoutSchema33.setObjectName("layoutSchema33")
        #
        self.layoutSchema22.addLayout(self.layoutSchema33)
        self.horizontalLayout_166.addLayout(self.layoutSchema22)
        self.layoutSchema11.addWidget(self.groupBoxSchema11)
        self.verticalLayout_77.addLayout(self.layoutSchema11)
        self.tab.addTab(self.export_page, "")
        
        ## partie help
        self.help_page = QtWidgets.QWidget()
        self.help_page.setObjectName("help_page")
        self.verticalLayout_77 = QtWidgets.QVBoxLayout(self.help_page)
        self.verticalLayout_77.setObjectName("verticalLayout_77")
        self.layoutSchema11 = QtWidgets.QVBoxLayout()
        self.layoutSchema11.setObjectName("layoutSchema11")
        self.groupBoxSchema11 = QtWidgets.QGroupBox(self.help_page)
        self.groupBoxSchema11.setObjectName("groupBoxSchema11")
        self.horizontalLayout_166 = QtWidgets.QHBoxLayout(self.groupBoxSchema11)
        self.horizontalLayout_166.setObjectName("horizontalLayout_166")
        self.layoutSchema22 = QtWidgets.QVBoxLayout()
        self.layoutSchema22.setObjectName("layoutSchema22")
        self.tableViewSchema = QtWidgets.QTableView(self.groupBoxSchema11)
        self.tableViewSchema.setObjectName("tableViewSchema")
        self.layoutSchema22.addWidget(self.tableViewSchema)
        self.layoutSchema33 = QtWidgets.QHBoxLayout()
        self.layoutSchema33.setObjectName("layoutSchema33")
        #
        self.layoutSchema22.addLayout(self.layoutSchema33)
        self.horizontalLayout_166.addLayout(self.layoutSchema22)
        self.layoutSchema11.addWidget(self.groupBoxSchema11)
        self.verticalLayout_77.addLayout(self.layoutSchema11)
        self.tab.addTab(self.help_page, "")
        
        ## ?? 
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Terminator 2.0"))
        self.labelHome1.setText(_translate("MainWindow", "Terminator 2.0\n"
"Author: Name and email\n"
"Contributors: …\n"
""))
        self.labelHome2.setText(_translate("MainWindow", "Link of the previous versions of Terminator:\n"
"Le Terminator 1.0 = Diederich, J., Fortuner, R. & Milton, J. 1999a.\n"
"Computer-assisted data extraction from the taxonomical literature.\n"
"http://genisys.prd.fr/Diederich_etal_1999b.html>Vi\n"
"\n"
"Link which describes the terminator schema:\n"
"Diederich, J., Fortuner, R. & Milton, J. 1997. Construction and\n"
"integration of large character sets for nematode morpho-anatomical data\n"
"http://genisys.prd.fr/Diederich_etal_1997.html>. \n"
"Diederich, J., Fortuner, R. & Milton, J. 2000b. A uniform representation\n"
"for the plan of organization of nematodes of the order Tylenchida\n"
"http://genisys.prd.fr/Diederich_etal_2000b.html\n"
""))
        #page d'accueil
        self.tab.setTabText(self.tab.indexOf(self.home_page), _translate("MainWindow", "Home"))
        #table import text  partie description de lespèce
        self.labelRefNum.setText(_translate("MainWindow", "REF_N°"))
        self.labelSpeciesNum.setText(_translate("MainWindow", "SPECIES_N°"))
        self.labelRecNum.setText(_translate("MainWindow", "REC_N°"))
        self.labelGenus.setText(_translate("MainWindow", "Genus"))
        self.labelSpecies.setText(_translate("MainWindow", "Species"))
        self.labelPopulation.setText(_translate("MainWindow", "Population"))
        self.labelSex.setText(_translate("MainWindow", "Sex"))
        self.labelAge.setText(_translate("MainWindow", "Stage"))
        self.labelLocality.setText(_translate("MainWindow", "Locality"))
        self.labelHost.setText(_translate("MainWindow", "Host"))
        self.labelEmptyField.setText(_translate("MainWindow", ""))
        
        # import text 
        self.labelPublishedDescription.setText(_translate("MainWindow", "Published description"))
        self.pushButtonImportFile.setText(_translate("MainWindow", "Import file"))
        self.pushButtonNext.setText(_translate("MainWindow", "Next"))
        self.tab.setTabText(self.tab.indexOf(self.importText_page), _translate("MainWindow", "Import text"))
        #partie resultat
        self.groupBoxExecute1.setTitle(_translate("MainWindow", "Published description"))
        self.groupBoxExecute2.setTitle(_translate("MainWindow", "Result :"))
        self.pushButtonSaveExecute.setText(_translate("MainWindow", "Save"))
        # partie schema 
        self.tab.setTabText(self.tab.indexOf(self.execute_page), _translate("MainWindow", "Execute"))
        self.groupBoxSchema1.setTitle(_translate("MainWindow", "Schema of the organs and their associated properties"))
        self.pushButtonAddSchema.setText(_translate("MainWindow", "Add"))
        self.pushButtoModifySchema.setText(_translate("MainWindow", "Modify"))
        self.pushButtonDeleteSchema.setText(_translate("MainWindow", "Delete"))
        self.tab.setTabText(self.tab.indexOf(self.schema_page), _translate("MainWindow", "Schema"))
        # partie export
        self.tab.setTabText(self.tab.indexOf(self.export_page), _translate("MainWindow", "Export results"))
        # partie help
        self.tab.setTabText(self.tab.indexOf(self.help_page), _translate("MainWindow", "Help"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #MainWindow.destroy()
    sys.exit(app.exec_())
  #  os.close(Python 3.6)
    #sys.exit(0)
    

