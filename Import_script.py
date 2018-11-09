# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:35:11 2018

@author: clemence
"""

import xlrd
import pickle
from xlwt import Workbook

###############################################################################
##################### Import of excel files in dictionnaries ##################
###############################################################################

# Be careful on the format of the excel sheet : only two columns, without title
# This script needs to be in the same repertory that the dictionnaries and the excel file

def import_dico(nomDoc,nomSheet):
    # Need to write the title of the file with '' + xlsx extension
    # Write the name of the sheet like this : u'nameSheet' !!

    # Loading of the Excel sheets
    wb = xlrd.open_workbook(nomDoc)
    # Reading sheets of the doc
    sh = wb.sheet_by_name(nomSheet)
    
    synonyms = []
    dico = {}
    
    for rownum in range (0,sh.nrows): 
    # reading one line after the other, starting at line 0
        synonyms.append(sh.row_values(rownum))    
        # add the document words in a list, created line by line
        for key, value in synonyms: # read the list
            key = key.lower()
            value = value.lower() # the value is set in lower case before adding it
            if key not in dico:
                if value == '':
                    dico[key]=[]
                else:
                    dico[key] = [value]
            # if the key does not exit in the dictionnary, create it with the corresponding value
            else:
                if not value in dico[key] and value != '': 
                    # if the value is not already part of the values associated to the key (avoid duplication)
                    dico[key].append(value)
                    # otherwise we add the value in the list of the values corresponding to the key
    
    return(dico)

###############################################################################
###### Creation of a global list containing the words and their synonyms ######
###############################################################################

def list_organs(nomDoc,nomSheet):
        # Loading of the Excel sheets
    wb = xlrd.open_workbook(nomDoc)
    # Reading sheets of the doc
    sh = wb.sheet_by_name(nomSheet)
    
    synonyms = []
    
    for rownum in range (0,sh.nrows): 
    # read the lines one after the other, starting at line 0
        synonyms.extend(sh.row_values(rownum))    
        # add the words in the list
    return(synonyms)
    
###############################################################################
########## Saving and loading of the file containing the dictionnary ##########
###############################################################################
    
def register(dico,fileName):
    # record the dictionnary in a file
    with open(fileName,'wb') as theFile: 
        myPickler = pickle.Pickler(theFile) # indicate in which file we will work 
        myPickler.dump(dico) # write in the dictionnary
        
def opening(fileName):
    # open the file and read it
    with open(fileName,'rb') as theFile:
        myDepickler = pickle.Unpickler(theFile)
        dictionnary = myDepickler.load()
    return(dictionnary)

def saveData(dico,filename):
    with open(filename, "wb") as pickleFile:
        pickle.dump(dico, pickleFile)

###############################################################################
#################### Adding a new item in the dictionnary #####################
###############################################################################
        
def add_Item():
    print("Adding a new word in the dictionnary : \n")
    ajoute = False
    word = input("What word do you want to add to the dictionnary ? \n")
    word = word.lower() # word in lower case
    

    ######################## DICTIONNARY'S CHOICE ########################

    print("In which dictionnary ? \n")
    print("1) Organs/Synonyms dictionnary \n")
    print("2) Properties/Values dictionnary \n")
    print("3) Name extensions dictionnary \n")
    
    c = input("Your choice ? 1,2 or 3 ? \n")
    if c == '1': 
        file = 'organsList' # define the file we are working in
        dico = opening('organsList') # load the dictionnary
        print("You chose Organs/Synonyms dictionnary. \n")
    elif c == '2': 
        file = 'valuesDico' # define the file we are working in
        dico = opening('valuesDico') # load the dictionnary
        print("You chose Properties/Values dictionnary. \n")
    elif c == '3': 
        dico = opening('relativeProp') # define the file we are working in
        file = 'relativeProp' # load the dictionnary
        print("You chose Name extensions dictionnary. \n")
    else: # if the user enters something else
        print("Error")
        
    ####################################################################
    
    syno = input("Is this word the synonym for another one ? y/n \n")
    
    if syno == 'y' or syno == 'Y': # if the word is synonym of another one
        newsyno = input("Which one ? \n")
        newsyno = newsyno.lower() # new synonym in lower case
        
        for key in dico: # look in the entire dictionnary
            if newsyno in dico.keys(): # if newsyno is a key in the dictionnary
                dico[newsyno].append(word) # add word in the values of the newsyno key
                with open(file,'wb') as newdico: # open the file containing the dico (with 'write' argument)
                    pickle.dump(dico,newdico) # modify the file containing the dico
                    newdico.close() # close the file
                print("The word is now in the dictionnary. \n")
                ajoute = True
                break # exit the loop
            else: # if newsyno is not a key in the dictionnary
                for i in dico.values(): # we look in the values of the dictionnary
                    if newsyno in i: # if newsyno is in the values of the dictionnary
                        i.append(word) # we add it in the list of the corresponding values
                        with open(file,'wb') as newdico: # open the file containing the dico (with 'write' argument)
                            pickle.dump(dico,newdico) # modify and save the file
                            newdico.close() # close the file 
                        print("The word is now in the dictionnary. \n")
                        ajoute = True
                break # exit the loop
        if ajoute == False: 
            print("This word is not in the dictionnary. \n")
    
    elif syno == 'n' or syno == 'N': # if word is not a synonym of another word
        dico[word] = [] # add the word as a key in the dictionnary
        with open(file,'wb') as newdico: # open the file containing the dico (with 'write' argument)
            pickle.dump(dico,newdico) # modify and save the file
            newdico.close() # close the file
            print("The word is now in the dictionnary. \n")
            ajoute = True
        if ajoute == False: 
            print("This word is not in the dictionnary. \n")
    else: # if the user enters something else
        print("Error")
    
    
###############################################################################
################### Deleting an item from the dictionnary #####################
###############################################################################

def supp_item():
    values = [] # intermediary list : used to store the values of the dictionnary    
    trouve = False
    print("Deleting of a word in the dictionnary. \n")
    
    ######################## CHOIX DU DICTIONNAIRE #####################

    print("In which dictionnary do you want to work ? \n")
    print("1) Organs/Synonyms dictionnary \n")
    print("2) Properties/Values dictionnary \n")
    print("3) Name extensions dictionnary \n")
    
    c = input("Your choice ? 1,2 or 3 ? \n")
    if c == '1': 
        file = 'organsList' # define the file we are working in
        dico = opening('organsList') # load the dictionnary
        print("You chose Organs/Synonyms dictionnary. \n")
    elif c == '2': 
        file = 'valuesDico' # define the file we are working in
        dico = opening('valuesDico') # load the dictionnary
        print("You chose Properties/Values dictionnary. \n")
    elif c == '3': 
        dico = opening('relativeProp') # define the file we are working in
        file = 'relativeProp' # load the dictionnary
        print("You chose Name extensions dictionnary. \n")
    else: # if the user enters something else
        print("Error")
        
    ####################################################################
     
    word = input("What word do you want to delete from the dictionnary ? \n")
    word = word.lower() # word in lower case
        
    for key in dico: 
        if word in dico.keys():
            trouve = True
            choice = input("This word has synonyms. Do you want to delete them all ? y/n \n")
            if choice == "y" or choice == "Y": 
                del dico[word] # delete the key + all the associated values
                with open(file,'wb') as newdico: # open the file containing the dico (with 'write' argument)
                    pickle.dump(dico,newdico) # modify and save the file
                    newdico.close() # close the file   
                print("The word has been deleted from the dictionnary. \n")
            elif choice == "n" or choice == "N": 
                # delete the key but keep the values : the first one become the key
                values = dico[word] # save the values associated to word
                del dico[word] # delete the key and the associated values
                dico[values[0]] = [] # first value become the key 
                dico[values[0]].extend(values[1:]) # add the values
                with open(file,'wb') as newdico: # open the file containing the dico (with 'write' argument)
                    pickle.dump(dico,newdico) # modify and save the file
                    newdico.close() # close the file 
                print("The word has been deleted from the dictionnary. \n")
        else: 
            for i in dico.values(): # loop in the lists of values of the dictionnary
                if word in i: # if word is a value in the dictionnary
                    i.remove(word) # remove the word in the list of value
                    trouve = True
                    with open(file,'wb') as newdico: # open the file containing the dico (with 'write' argument)
                        pickle.dump(dico,newdico) # modify and save the file
                        newdico.close() # close the file
                    print("The word has been deleted from the dictionnary. \n")
                    break
    if trouve == False: 
        print("This word is not in the dictionnary. \n")

###############################################################################
################ Export of the triads list into an Excel file #################
###############################################################################

def export(listeTriades): 
    
    # creation of the workbook
    book = Workbook()
    
    # creation of the first sheet
    sheet1 = book.add_sheet('Results')
    
    # adding the headers
    sheet1.write(0,0,'Organ')
    sheet1.write(0,1,'Property')
    sheet1.write(0,2,'Value')
    
    x = 1
    #filling the table
    for triades in listeTriades:
        sheet1.write(x,0,triades[0])
        sheet1.write(x,1,triades[1])
        sheet1.write(x,2,triades[2])
        x += 1 # allow to right in the line below the previous one
    
    # material creation of the existing file
    book.save('FinalResults.xls')
    
###############################################################################
###############################################################################
         
#---------- Creation of the file / Testing of the functions -------------------#
        
dico_relativeprop = import_dico('Fichier_Dictionnaire.xlsx',u'relativeProp')
register(dico_relativeprop,'relativeProp')
#test2 = opening('relativeProp')
#print(test2)

dico_values = import_dico('Fichier_Dictionnaire.xlsx',u'Standards_vals')
register(dico_values, 'valuesDico')
#test1 = opening('valuesDico')
#print(test1)

dico = import_dico('Fichier_Dictionnaire.xlsx',u'Organes')
register(dico,'organsList')
#test = opening('organsList')
#print(test)
        