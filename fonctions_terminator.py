# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:11:56 2018

@author: cleme
"""

from Import_script import opening
from Import_script import export
import re
import pickle

###############################################################################
# ------------------------------ Pseudo Main -------------------------------- #
###############################################################################

#source = "Measurements: Topotypes (10 females): L = 0.59-0.79 mm; a = 27-35; b = 5.8-6.9; b' = 4.4-5.9; c = 35-49; c' = 0.8-1.2; V = 60-65; spear = 25-28 µm; m = 46-50; O = 37-46. Female: Body usually in spiral shape. Lip region hemispherical, 4 or 5 often indistinct annules. Spear knobs with indented anterior surfaces. Excretory pore at level of anterior end of esophageal glands. Hemizonid just anterior to excretory pore. Hemizonion usually not visible. Spermatheca usually conspicuous, offset without sperm. Phasmids 5 to 11 annules anterior to level of anus. Tail more curved dorsally, usually with slight ventral projection, 6 to 12 annules."
#source = "Holotype (female in hard glycerin jelly): L (length including neck and head) = 446; width = 182; neck length = 124; stylet length = 24.4; DGO (distance from dorsal gland orifice to base of stylet) = 2.0; excretory pore from anterior end = 114; vulva-anus distance (lateral view) = 33.2; vulva length = 12.4; thickness of cuticle = 6.1; a (length/width) = 2.5; m (length of stylet cone/total stylet length) = 4.6; O (DGO/stylet length) = 0.1; excretory pore (excretory pore to head end/L %) = 26."
#source = "Cactodera salinas J. G. BALDWIN, M. MUNDO-OCAMPO & M. A. McCLURE, 1997. Cactodera salina n. sp. from the Estuary Plant, Salicornia bigelovii, in Sonora, Mexico. Journal of Nematology 29(4):465-473. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2619802/pdf/465.pdf Label REF_NO 5361SPECIES_NO 3976REC_NO 7067Species Cactodera salina Population  holotype Sex  Female Stage  Adult Description Holotype (female in hard glycerin jelly): L (length including neck and head) = 446; width = 182; neck length = 124; stylet length = 24.4; DGO (distance from dorsal gland orifice to base of stylet) = 2.0; excretory pore from anterior end = 114; vulva-anus distance (lateral view) = 33.2; vulva length = 12.4; thickness of cuticle = 6.1; a (length/width) = 2.5; m (length of stylet cone/total stylet length) = 4.6; O (DGO/stylet length) = 0.1; excretory pore (excretory pore to head end/L %) = 26. Label REF_NO 5361SPECIES_NO 3976REC_NO 7067Species Cactodera salina Population  paratypes Sex  Female Stage  Adult Females (n = 6): L (including "neck") = 336-515 (mean 447, standard error, 28.3); width = 149-272 (194.7, 19.7); neck length = 95-178 (128.7, 12.1); stylet length = 23.5- 24.4 (23.8, 0.2); DGO = 1.0-2.0 (1.6, 0.16); excretory pore from anterior end = 84-101 (92.6, 3.2); vulva-anus distance (lateral view) = 27.5-40.8 (36.9, 2.6); vulva length (n = 6 from cone mounts) = 10-12.7 (11.2, 0.5); thickness of cuticle --6.6-9.2 (8.2, 0.5); a = 1.9-3.4 (2.4, 0.23); O = 4.3-8.7 (6.8, 0.7).  Body asymmetrical and dorsally curved with no cone in younger individuals, oval or nearly spherical with a minute posterior protuberance in large specimens (Figs. 1B,C;3B). Neck set off and usually reflexed ventrally. Young females pearly white, becoming increasingly opaque with age and following fixation. Cuticle with a pattern of deep zigzag folds; anterior to the excretory pore a gradual transition to wavy striations and finally a relatively smooth head region. Anterior to the excretory pore, a dense material covering the head and neck region. Excretory pore slightly posterior to level of median bulb and esophageal gland region elongate. Stylet slightly curved dorsally (Fig. 1A). Ovaries paired. Subcrystalline layer not observed."
source = "Males (n = 15): L = 906-1118 (1001, 21); width = 27- 31 (28.7, 0.37); stylet = 24-28 (25.8, 0.35); DGO = 2.0- 3.1 (2.48, 0.18) esophagus length = 142-179 (161.2, 7.09); excretory pore from anterior end = 108-133 (117.8, 2.68); testis length = 415-565 (489, 29.8); spicule length (n = 1) = 40.8; gubernaculum length (n = 1) -- 13.3; a = 31.7-37.8 (34.9, 0.7); b = 4.7-11.2 (8.0, 0.9); b' = 5.5- 7.1 (6.3, 0.28); O = 7.7-12.5 (9.9, 0.8); T (testis length/L) % = 39.9-55.5 (48.6, 2.84) ; excretory pore % = 10.5-13.2 (11.8, 0.28).  Body vermiform with little anterior or posterior tapering; posterior end of heat-killed specimens with a nearly 90 ° twist. Head region slightly set off with about 4-7 discontinuous annulations (Figs. 2A,5B). Labial disc elevated; in SEM, lip sectors and labial disc together forming a square; lip sectors highly irregular in pattern among individuals but generally lateral lips fused with adjacent submedial sectors (Fig. 5B). Lateral sectors much smaller than submedial sectors. Lateral field with four incisures, outer ridges often areolated anteriorly, pattern of lines distorted posteriorly (Figs. 2B,5E). Hemizonid about one annule anterior to excretory pore; cephalids not observed. Stylet knobs robust and slightly flattened anteriorly (Fig. 2A). Spicules distinctly bifid; inconspicuous, elongate gubernaculum present. Phasmid openings not observed (Figs. 2B;5E,F)."

def pseudo_main(source):
    # creation or loading of the dictionnaries
    listModifiers = ["usually", "often", "rarely", "almost"]
    dicoOrgans = opening('organsList') 
    valuesDico = opening('valuesDico')
    dicoRelativeProp = opening('relativeProp')
    
    finalDicoText = {}
    finalListTriad = []
    
    # split of the text 
    source = source.lower() # source in lower case
    split = splitLine(source)
    previousOrgan = '' 
    
    for j in range(len(split)):
        
        # initialization of all the lists
        list_org_found = []
        list_prop_found = []
        list_val_found = []
        list_triads = []
        
        list_pos_org = []
        list_pos_prop = []
        list_pos_val = []
        
        # modifiers search 
        theModifiers = modifiersDetect(split[j], listModifiers)
        
        # organ search
        org = findOrgans(split[j], dicoOrgans)
        list_org_found = org[0]
        list_pos_org = org[1]
        
        # search of explicit qualitative properties and values 
        valQual = findQualitativeValues(split[j], valuesDico)
    
        list_prop_found = valQual[0][0]
        list_val_found = valQual[1][0]
        
        list_pos_prop = valQual[0][1]
        list_pos_val = valQual[1][1]
    
        # deleting of the duplications
        deleteDouble3(list_val_found, list_pos_val)
        deleteDouble3(list_prop_found, list_pos_prop)
        deleteDouble3(list_org_found, list_pos_org)

        # detection of a triads in a measurement triads context
        m = findMeasurement(split[j])#, findRegex(split[j]))
        
        #####
        #Here we test if the sentence might be a measurement sentence
        #If it is so the measurement triads related functions are perform
        if m[2] != 0:
            if m[2] > 1:                                                        ###Check if there is more than 1 "=" in the sentence
                m2Equal = measurementWith2Equals(split[j])                      #If so we change the value of resVal with measurementWith2Equals
                c = createTriadMeasurement1(m[0], m2Equal, list_triads)         #Perform createTriadMeasurement1
                if c == False:                                                  #If createTriadMeasurements does not found anything then
                    createTriadMeasurement2(m2Equal, org[0], valQual[0][0], m[0], list_triads)    #Perform createTriadMeasurements2
            else:                                                               ###If there is only 1 "="
                c = createTriadMeasurement1(m[0], m[1], list_triads)
                if c == False:
                    createTriadMeasurement2(m[1], org[0], valQual[0][0], m[0], list_triads)
        
        #####
        #If the sentence is not a measuremet triads then the explicite and implicite deduction triads function are perform
        else:  
            # deduction of implicit properties 
            newNumberProp(split[j], list_org_found, list_pos_org, list_triads)
            newTriad(list_org_found, list_prop_found, list_val_found, list_pos_val, list_triads, theModifiers[0], theModifiers[1])
            newTriadDeduc(list_org_found, list_pos_org, list_prop_found, list_val_found, list_pos_val, valuesDico, list_triads, theModifiers[0], theModifiers[1], previousOrgan) 
            # relative properties search 
            rel_values = detectionRelativeProp(split[j], dicoRelativeProp)
            add_rel_prop = addRelativeProp(rel_values[0], rel_values[1], list_org_found, org[1], list_prop_found, dicoRelativeProp, list_triads)
            list_org_found = add_rel_prop[0]
            # inserting results in the three lists
            list_pos_org = add_rel_prop[1]
            list_pos_prop = list_pos_prop + valQual[0][1]
            list_pos_val = list_pos_val + valQual[1][1]
            
    
        finalDicoText = createDicoText(finalDicoText,split[j],list_triads)
        finalListTriad = createTotalListTriad(finalListTriad,list_triads)
            
#    print(finalListTriad)
        
#    for i in finalDicoText:
#        print("Sentence: " + i)
#        print("The triad : ", finalDicoText[i])
#        print("*")
    return(finalDicoText)
    
###############################################################################
# ---------- Research functions (organs, properties, values) ---------------- #
###############################################################################

# This function allow to detect some numerical value and it units , range

def findRegex(source):
# search numerical values in the text using a regex    
    pattern=re.compile(r"""
                       (([[]?[0-9]+(\s?[.,]\s?\d+)?\s?(-|to|or)\s?[0-9]+(\s?[.,]\s?\d+)?[]]?)# intervalle
    |
    ([0-9]+(\s?[.,]\s?\d+)?))
    ([ ]*(µg|cm|g|mg|µm|mm|cg|m))?
    """, re.VERBOSE)
    result = pattern.finditer(source)
    listofresult=[] #record the result in a dictionnary
    for m in result:
        listofresult.append(m.group());
    return listofresult

# --------------------------------------------------------------------------- #
 
# function allowing to split a source text into lines by splitting by '.' or ';'
# uses a regex
def splitLine(source):
    result = re.split('(?<!\d)[;.]|[;.](?!\d)', source)
    return(result)

# --------------------------------------------------------------------------- #
    
#function of research of organs present in the source
#searching from the dictionary of organs containing the main name as key and the synonyms as values
def findOrgans(source, dicoOrgans):
    resFinal = [] # initialization of an empty list for the the found organs
    pos = [] #initialization of the list of the positions
    source = source.lower()
    if dicoOrgans!={}:
        for key in dicoOrgans: # for each key in the dictionary
            pattern = re.compile(key) 
            #use of a regex to match pattern of the values in the dictionary with the words of the source
            for org in pattern.finditer(source):
                org_pos = [org.start(), org.end()]
#.finditer allows to match strings and get back the start and end positions of the match in the source
                resFinal.append(key) #we keep the key
                pos.append(org_pos) # we keep the positions
            l_aux = dicoOrgans[key] 
            # creation of an auxiliary list, composed of the synonyms of themain organ (key)
            for i in range(len(l_aux)):
                pattern_syn = re.compile(l_aux[i])
                for syn in pattern_syn.finditer(source):
                    #we perform another research on the synonym values
                    syn_pos = [syn.start(), syn.end()]
                    resFinal.append(key) 
                    #if found, we take the name of the main organ to replace it directly in the result
                    pos.append(syn_pos)
    a = triBulle2(resFinal, pos) # sorting of the lists
    return(a) #return two lists, one with the organs, one with their positions (both are sorted)

#----------- IMPORTANT NOTE--------------------------------------------------------
#CAREFUL this function findOrgans alone takes the organs with their order from the dictionary
#needs to be sorted to get back the positions in the text
#CAREFUL the function manages directly the synonymy of the organs
    
# the other research functions are built on the same principle
    
# --------------------------------------------------------------------------- #

#this function researches qualitative values and properties the same way as findOrgans   
#we search form the dictionary of the basic properties  
def findQualitativeValues(source, dicoProp):
    source = source.lower()
    resProp, resVal = [], []
    posProp, posVal = [], []
    if dicoProp!={}:
        for key in dicoProp:
            pattern = re.compile(key) # we search the properties in the source
            for prop in pattern.finditer(source):
                prop_pos = [prop.start(), prop.end()]
                
                resProp.append(key) #we take the property name
                posProp.append(prop_pos) #we store their positions

            l_aux = dicoProp[key] #corresponds to the possible values for a property (key)
            for i in range(len(l_aux)): #for each value
                pattern_val = re.compile(l_aux[i]) 
                for val in pattern_val.finditer(source): #we search for a match according to the pattern
                    val_pos = [val.start(), val.end()]
                    
                    resVal.append(l_aux[i]) #we get the associate value to a property
                    posVal.append(val_pos)
    #sorting of the lists
    list_prop_exp = triBulle2(resProp, posProp) 
    list_val_qual = triBulle2(resVal, posVal)
    return(list_prop_exp, list_val_qual)
    #we get the properties and th evalues if existing
    
# --------------------------------------------------------------------------- #

#this function allows to deduce properties from values
def property_deduction2(value, prop_dico):
    #from a value we can do a deduction of its possible property
    l_found = [] #list of the found propeties for the value
    if prop_dico!={}:
        for key in prop_dico: #for each key from the dictionary of the properties
            l_aux = prop_dico[key]
            for i in range(len(l_aux)): #we search for the values
                if l_aux[i]==value: #if the value is found in the dictionary
                    l_found.append(key) #we get the associate property

    return(l_found) #we obtain a list containing the different possible properties for a value
    
# --------------------------------------------------------------------------- #

#research of numerical values in a text 
def findPropValNum(source, regle):
    # the 'regle' can be written in the main program
    pattern=re.compile(regle)

    result = pattern.finditer(source)
    listofresult=[] #record the result in a dictionnary
    for m in result:
        listofresult.append(m.group());
    return listofresult
    
# --------------------------------------------------------------------------- #

#this function recognizes relative values such as 'anterior to' for exemple
#the method of research is the same than for the precedent functions
def detectionRelativeProp(source, dicoRelativeProp):
    listRelVal = []
    posRelVal = []
    if dicoRelativeProp!={}:
        for key in dicoRelativeProp:
            #we search in the dictionary of the relative properties (and their values)
            l_aux = dicoRelativeProp[key]
            for i in range(len(l_aux)):
                pattern = re.compile(l_aux[i])
                for rel in pattern.finditer(source): #if we find values
                    pos = [rel.start(), rel.end()]

                    listRelVal.append(l_aux[i]) #we store them in list
                    posRelVal.append(pos)
    return(triBulle2(listRelVal, posRelVal))
    #returns the sorted lists of the relative values found and their positions in the source
    #here we only have the values, we need to find the property 
    #CAREFUL see the addRelativeProp function which is related to this function
    
# --------------------------------------------------------------------------- #

    # same principle of detection as usual
    # storage of the 'modifiers' found in the source
def modifiersDetect(source, listModifiers):

    modifiersFound = []
    pos = []
    source = source.lower()
    for i in listModifiers: #search in the list of possible modifiers
        pattern = re.compile(i)

        for modifiers in pattern.finditer(source): #if we find modifiers in the source
            mod_pos = [modifiers.start(), modifiers.end()]
            modifiersFound.append(i) #we keep them
            pos.append(mod_pos) #and we keep their positions
            
    return(triBulle2(modifiersFound, pos))
    #CAREFUL see the addModifiers function which is related to this function
    
# --------------------------------------------------------------------------- #
        
#This function is made to detec the measurement sentence
#The parameter are the sentence of the souce text and the regex find in those sentence with the findRegex() function
#The returned results are a list and a sting, a properties list and a values stirng (You may ask why... It is easier for the traitement with the other function)
#This function also return an integer which correspond to the number of "=" found in the sentence
        #The function begin by the "=" detection which are significative (most of the time) of a measurement sentence
        #I wanted to make a double check that the sentence if a measurement sentence by also detecting the numeric values (with findRegex)
        #Infortunatly that didn't work (as you can see the commented code below in the function)
        #But it is not so disturbing for the detection. I let it that way in order to focus on that point later
def findMeasurement(source):#, rgx):
    src = source.split(" ") #Split de la phrase en liste de mots
    resVal = "" 
    listProp = []
    posEqual = 0
    equalCpt = 0
    for i, word in enumerate(src): 
        if word == '=':                             #if the word is "="
            posEqual = i                            #I record its position in the word list
            equalCpt = equalCpt + 1
#            reg = source.find(r)                   #After checking that the sentence contain a "=" I check that there is a numerous value (findRegex())
#            if reg != -1:                          # If there is a numerous values there is high chance that it's a measurement sentence
            for i, word in enumerate(src): 
                if posEqual < i:                    #If the word is after the "="
                    resVal = resVal + src[i] + " "  #I make sting of whatever is afeter the "" -> It is likely to be the values
                if posEqual > i:                    #For whatever is before the ="
                    if src[i] != "":                #Sometime the function was returning me en empty element in the first place of the list. This allow to avoid it.
                        listProp.append(src[i])     #I a list of word -> It is likely to be the properties
    return(listProp, resVal, equalCpt)

###############################################################################
# ----------------- Functions of triad management --------------------------- #
###############################################################################

# --------------------------------------------------------------------------- #

#creation of a triad from three arguments, no matter their form   
def createTriad(org, prop, val):
    triad = []
    triad.append(org)
    triad.append(prop)
    triad.append(val)
    #each element is added to the list to create the triad
    return(triad) 
    
# --------------------------------------------------------------------------- #
    
#This function performs a triad construction according to the findMeasurement() results
#It is simple and it works well for the measurement sentence such as " a = 100 ", the easy measurement sentences (It is really standardized)
#It takes the listProp and resVal returned by findMeasurement() as parameter
#The function firstly analyse the words in ListProp, if a particular word is detected then the function record a triad according to that word 
#This function use addListTriads to record the triad in the final dictionnary
def createTriadMeasurement1(listProp, resVal, listTriads):
    createTriadMeasurementMade = False
    for i, word in enumerate(listProp):
        if word == "l" or word == "a" or word == "b" or word == "b'" or word == "v":
            if word == "l":
                tr1=createTriad("body", "length", resVal)
                addListTriads(listTriads, tr1)
            else:
                tr2=createTriad("body", "ratio " + word, resVal)
                addListTriads(listTriads, tr2)
            createTriadMeasurementMade = True
        if word == "width":
            tr3=createTriad("body", "width", resVal)
            addListTriads(listTriads, tr3)
            createTriadMeasurementMade = True
        if word == "c" or word  == "c'":
            tr4=createTriad("tail", "ratio " + word, resVal)
            addListTriads(listTriads, tr4)
            createTriadMeasurementMade = True
        if  word == "spear" or word == "m":
            if word == "spear":
                tr5=createTriad("stylet", "length", resVal)
                addListTriads(listTriads, tr5)
            else:
                tr5=createTriad("stylet", "ratio " + word, resVal)
                addListTriads(listTriads, tr5)
            createTriadMeasurementMade = True
        if  word == "o":
            tr6=createTriad("dorsal gland opening", "ratio " + word, resVal)
            addListTriads(listTriads, tr6)
            createTriadMeasurementMade = True
        if word == "dgo":
            tr7=createTriad("dorsal gland opening", "distance", resVal)
            addListTriads(listTriads, tr7)
            createTriadMeasurementMade = True
    return(createTriadMeasurementMade)

# --------------------------------------------------------------------------- #

#This second function allows to return a triad from a measurement sentence
#This function takes as parameters :
    #The values list returned form findMeasurement (which is to mendatory used to build the final result)
    #The organ list from findOrgan
    #The property list from findQualitativeValues
#I've try to use the result of findPropValNum() which detect everything before the "=" with no success (but it coulf be a good idea to use it in the future)
#This function record most of the time some approximation (At the level of the added Organ and Property). It definitly lake another funtion to be improved. For now, the user would have to decide if it is wrong or right 
def createTriadMeasurement2(resVal, listOrg, listP, listPropFromFindMeasurement, listTriads):
    org = ""
    prop = ""
    ###Organ Deduction
    if listOrg != []:
        org = " ".join(listOrg) #I join all the organ because it is too hard to know which one is the object of the sentence. In the reality it may works most of the time. The findOrgans function may detect two words (two differents organs) which actually consitute one only organ. However it also is the first source of approximation.
        for i, word in enumerate(listPropFromFindMeasurement): #This loop is only here to detect if there is the words "lateral view" to found
            if word == "(lateral" or word == "lateral": # it is "(lateral" because it is how the algo cut the sentence in word and to the word is like that
                if listPropFromFindMeasurement[i+1] == "view)" or listPropFromFindMeasurement[i+1] == "view":
                    org = org + " (lateral view)"
        ePFAE = " ".join(listPropFromFindMeasurement) #here we detect specifically if the organ is "excretory pore from anterior end" (epfae)
        if ePFAE == "excretory pore from anterior end": #it can be contained in the "if listOrg != []:" condition because "excretory pore" and "anterior end" are founnd and are contained in listOrgan
            org = ePFAE
    else:
        org = ("Organ not found") #If findOrgan doesn't find anything         
    ###Property deduction
    if listP != []: #Algorithmly speaking it is the same process than for the organ deduction part in this function
        prop = " ".join(listP) #Same strategy than for the organ 12 lignes above.
    elif listP == []: 
        for i, word in enumerate(listPropFromFindMeasurement): #New loop on the list from findMeasurement
            if word == "from" or word == "distance": #if there is the word "from" the property is likely to be Distance, same thing if there is the word distance (which is not in the dictionary and should/must be added by the way)
                prop = "Distance"
            else:
                prop = "Property not found" #If findQualitativeValues doesn't find anything and the property is not distance related
    tr=createTriad(org, prop, resVal)
    addListTriads(listTriads, tr)

# --------------------------------------------------------------------------- #

#This function allow to handel the measurement sentence with two "="
#It takes the source as parameter and return a new value of resVal
#The aim of this function is to only consider the values after the second "=" in the sentence as the real values to record (which is true most of the time)
#It works well for sentence such as "males (n = 15): l = 906-1118 (1001, 21)" however it doesn't word at all for a sentence which contain two measurements triad to found (which apparently must never happen because it is not how it should be written in the source text)
def measurementWith2Equals(source):
    src = source.split(" ")
    posEqual = 0
    resVal = ""
    #the first loop allows to record the list position of the last "=" of the sentence
    for i, word in enumerate(src):
        if word == "=":
            if posEqual < i:
                posEqual = i
    #This loop allows to record everything after the second "=" and then transformed the resVal 
    for i, word in enumerate(src):
        if posEqual < i:
            resVal = resVal + src[i] + " "      
    return(resVal)

# --------------------------------------------------------------------------- #


#this simple function allows to concatenate every new triad into the existing list of triad
#allows a more easy display of all the triads of a line or a source
def addListTriads(listTriads, newList):
    listTriads.append(newList)
    return(listTriads)
    
# --------------------------------------------------------------------------- #

# creation of a very simple triad for simple cases
#where the number of organs, properties and values are the same
def newTriad(listOrg,listProp,listVal, posVal, listTriads, listModifiers, posModifiers):
    
    l = len(listOrg)
    m = len(listProp)
    n = len(listVal)
    if (l == m and m == n): 
    #if each list has the same length
    #then we suppose that items are related one with others
        for i in range(l):
            mod = addModifiers(listVal, posVal, listModifiers, posModifiers)
            #we check for possible modifiers in the source and replace the values in the listVal if necessary
            tr = createTriad(listOrg[i], listProp[i], mod[i])
            #creation of the triad directly
            addListTriads(listTriads, tr)
            #adding of the triad in the general list of triad
        #cleaning of the lists not to associate them a second time with others functions
        del listOrg
        del listProp
        del listVal
        return(listTriads)

# --------------------------------------------------------------------------- #
        
#this function allows to guess properties from values and create the associate properties directly
def newTriadDeduc(listOrg, posOrg, listProp,listVal, posVal, valuesDico, listTriads, listModifiers, posModifiers, previousOrgan):
    org = ''
    add = None
    if listVal!=[]: #if qualitative values are found
        for i in listVal:
            ind_val = listVal.index(i) 
            #we store the index number of the position of this information in the list with .index()
            v = property_deduction2(i, valuesDico) #list containing the possible properties for this value
            if len(v)==1:  #if there is only one property possible then this is the good one
                if len(listOrg)==1: #if there is only one organ, it should be the good one
                    mod = addModifiers(listVal, posVal, listModifiers, posModifiers) #we search for modifiers
                    tr = createTriad(listOrg[0], v[0], mod[ind_val])
                    if ind_val==(len(listVal)-1): 
                        #if we have searched for all the values we can delete the organ which is no more needed
                        del listOrg[0]
                        del posOrg[0]
                elif listOrg==[]: #if there is no organ found in the source
                    mod = addModifiers(listVal, posVal, listModifiers, posModifiers)
                    tr= createTriad(previousOrgan, v[0], mod[ind_val])
                    
                    #we create the triad with an organ found from the previous sentence (previousOrgan)
                    
                else: #if there are several organs in the source
                    for j in posOrg:
                        ind_org = posOrg.index(j)
                        if j[0]<posVal[ind_val][0]: 
                            #if the value is located after the organ name
                            #then this organ should be the good one
                            org = listOrg[ind_org]
                            mod = addModifiers(listVal, posVal, listModifiers, posModifiers)
                            tr = createTriad(org, v[0], mod[ind_val])
                        #else:
                        #    tr= createTriad(listOrg[-1], v[0], i)
                add = addListTriads(listTriads, tr)
                #adding of the triad in the general list of triads
                del listVal[ind_val]
                #we delete the value which is no more needed to evaluate
    if add != None:
        return(add)  
        
#------------ IMPORTANT NOTE --------------------------------------------------
    #CAREFUL if the property deduction produces a list longer than one item, we cannot know which one is the good one
    #the user has to decide himself
    
#------------------------------------------------------------------------------
    
#this function allows to manage a particular case: the number property, which has to be guessed
def newNumberProp(source, listOrg, posOrg, listTriads):  
    add = None
    relativeTo = ''
    numFinal = []
    posNum = []
    pattern = re.compile(r"(\d)+\s(-|to|or)\s(\d)+")
    #pattern to find values in the form 'num to num' / 'num or num' / 'num - num'

    for num in pattern.finditer(source): #we search for this pattern in the source
       pos = [num.start(), num.end()]
       numFinal.append(num.group())
       posNum.append(pos)
    for i in posOrg: #positions of the organs in the source
        ind_org = posOrg.index(i)
        for j in posNum: #positions of the value in the source
            ind_num = posNum.index(j)
            if i[0] > j[0] and relativeTo == '': 
                #if the position of the numerical value is before the position of an organ
                #then this organ should be related to the value
                relativeTo = listOrg[ind_org]
                tr = createTriad(relativeTo, 'number', numFinal[ind_num])
                #creation of the triad with 'number' as property
                add = addListTriads(listTriads, tr)
                
    if add != None:
        return(add)
    #returns the global list of triads found in this source

#------------------------------------------------------------------------------

#for all remaining triads, creation of triads with not available values ('NA')
#the user will have to change the values himself
def remainingTriads(listOrg, listProp, listVal, listTriads):
    add = None
    l = max(len(listOrg), (max(len(listProp), len(listVal))))
    # l is the length of the longer list between the lists of organs, prop and values
    for i in range(l):
        if i>(len(listOrg)-1): #for organs
        # if the index i is superior to the length of this list
        #then this list is not the longest
            a = 'NA'
        else: # if there is still an item in this list
            a = listOrg[i] #we store it
            
        #same
        if i>(len(listProp)-1): #for properties
            b = 'NA'
        else:
            b = listProp[i]

        if i>(len(listVal)-1): #for values
            c = 'NA'
        else:
            c = listVal[i]

        tr = createTriad(a, b, c)
        #creation of the triad with three values, 'NA' replaces an empty value
        add = addListTriads(listTriads, tr)
                
    if add != None:
        return(add)
    #returns the global list of triads found in this source
        
        
        
###############################################################################
#-------------- Management of all the triads ---------------------------------#
###############################################################################
        
        
# concatenate all the triads in a general list
# Be careful not to forget to initialize bigList = [] before starting 
def createTotalListTriad(bigList,listTriad):
    bigList.extend(listTriad)
    return(bigList)
    
# --------------------------------------------------------------------------- #

# creation of a dictionnary like {"sentence1" : [[triad1],[triad2]], "sentence2" : [[triade]],"sentence3" etc }
# need to initialize dicoText to {} before the loop at the begining of the programm
def createDicoText(dicoText,phrase,listTriad): 
    if phrase not in dicoText.keys():
        dicoText[phrase] = []
        dicoText[phrase].extend(listTriad)
    with open('generalTriadsDico','wb') as newdico: # open the file containing the dico (with 'write' argument)
        pickle.dump(dicoText,newdico) # modify and save the file
        newdico.close() # close the file 
    return (dicoText)

# --------------------------------------------------------------------------- #

def modifTriad(dicoText):

    print("Triad modification : \n")
    for cle, valeur in dicoText.items():
        print("-----------------------------------------------------")
        print("\nSentence : ", cle, "\n")
        print("List of triads : ") 
        for i in range(len(valeur)): 
            print(i, " : ", valeur[i])
        choice = input("Do you want to modify a triad for this sentence ? y/n \n")
        if choice == 'y' or choice == 'Y': 
            secondChoice = input("\nWhich one ? Please enter the triad number : ")
            chiffre = int(secondChoice)
            if chiffre < len(valeur): # if the number corresponds to the number of a triad
                thirdChoice = input("Do you want to change the organ (o), the property (p) or the value (v) ?")
                if thirdChoice == 'o' or thirdChoice == 'O': 
                    replace = input("You chose to modify the organ. By which word would you like to replace it ? \n")
                    valeur[i][0] = replace
                    print("Done. \n")
                    print(valeur[i])
                    with open('generalTriadsDico','wb') as newdico: # open the file containing the dico (with 'write' argument)
                        pickle.dump(dicoText,newdico) # modify and save the file
                        newdico.close() # close the file 
                elif thirdChoice == 'p' or thirdChoice == 'P': 
                    replace = input("You chose to modify the property. By which word would you like to replace it ? \n")
                    valeur[i][1] = replace
                    print("Done. \n")
                    print(valeur[i])
                    with open('generalTriadsDico','wb') as newdico: # open the file containing the dico (with 'write' argument)
                        pickle.dump(dicoText,newdico) # modify and save the file
                        newdico.close() # close the file 
                elif thirdChoice == 'v' or thirdChoice == 'V': 
                    replace = input("You chose to modify the value. By which word would you like to replace it ? \n")
                    valeur[i][2] = replace
                    print("Done. \n")
                    print(valeur[i])
                    with open('generalTriadsDico','wb') as newdico: # open the file containing the dico (with 'write' argument)
                        pickle.dump(dicoText,newdico) # modify and save the file
                        newdico.close() # close the file 
                else: 
                    print("Error.")
            else: 
                print("This number does not exist. \n")
        elif choice == 'n' or choice == 'N':
            print("\n")
        else: 
            print("Error. \n")

# --------------------------------------------------------------------------- #

        
###############################################################################
# ----------- Functions of management of lists and dictionaries ------------- #
###############################################################################

# --------------------------------------------------------------------------- #

#the function triBulle2 has for aim to put the items in the order in which they appear in the text
#because the search functions store the items in the order they appear in the dictionary and not the text

def triBulle2(listItem, listPos):
    n = len(listPos)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if listPos[j][0] < listPos[j-1][0]: #comparison of the start positions of the items in the text
                #if the start position of an item is inferior to the position of the precedent one
                listPos[j],listPos[j-1] = listPos[j-1],listPos[j] #we exchange the values of the positions
                listItem[j],listItem[j-1] = listItem[j-1],listItem[j] #we exchange the items with the same index
    return(listItem, listPos) #returns sorted lists

# --------------------------------------------------------------------------- #

#this function goes with detectionRelativeProp (which finds values from relative properties in the text)
#creation of a triad with relative properties with a deduction from the value
def addRelativeProp(listRelativeVal, posRelativeVal, listOrgans, posOrgans, listProp, dicoRelativeProp, listTriads):
    #we keep the position of the value in the text and compare it to the positions of the organs
    relativeProp = ''    
    add = None
    
    if listRelativeVal!=[]: #if there is a relative value found in the text
        for i in listRelativeVal: 
            deduc = property_deduction2(i, dicoRelativeProp)  #we guess the associate relative property
            #deduc is a list containing the possible relative properties for this value
            if deduc!=[]: #if we find the relative property
                if listOrgans!=[]: #if there are organs in the list
                    for j in posRelativeVal: #positions of the values of relative properties found
                        ind_prop = posRelativeVal.index(j)
                        for k in posOrgans: #for each organ found in the source
                            ind_org = posOrgans.index(k) #we get the index of its position in the source
                            if j[0] < k[0] and relativeProp=='': #if the relative property is located before an organ
                                relativeProp = deduc[0] + ' ' + listOrgans[ind_org] #then we concatenate them
                                if k[ind_org - 1] != None: #if there is another organ located just before
                                    organ = listOrgans[ind_org - 1] #we store it
                                    relativeVal = listRelativeVal[ind_prop]
                                    tr = createTriad(organ, relativeProp, relativeVal)
                                    #and we associate this organ with the relative property and its value
                                else: #if we cannot identify which organ it refers to
                                    tr = createTriad("Organ not found", relativeProp, relativeVal)
                                add = addListTriads(listTriads, tr)
                                
                                # then we delete the elements since we do not need them anymore
                                del listOrgans[ind_org]#ind_org is the index of the position of the value in the text
                                del posOrgans[ind_org]
                                del listRelativeVal[ind_prop]
                                del posRelativeVal[ind_prop]
    if add!=None:
        return(listOrgans, posOrgans, listRelativeVal, posRelativeVal, add)
    else :
        return(listOrgans, posOrgans, listRelativeVal, posRelativeVal)
    
#-------------------- IMPORTANT NOTE -----------------------------------------
    #the property is composed of the guessed property from the value found in the text + the organ situated just after
    #we get the PROPERTY AND ITS RELATIVE ORGAN, for example 'position relative to anus'
    #what I call value is what we initially find in the text, for example 'anterior to'
    #we need to keep both to associate them
    #we delete the RELATIVE ORGAN, since it is in the text to describe the relation with another organ (the main organ of the triad)

# --------------------------------------------------------------------------- #

#this function is related to the modifiersDetect function (which finds the modifiers present in the source)
#it associates the modifier whith its related value and replaces the new value in the list of values found in the text
def addModifiers(listValue, posValue, listModifiers, posModifiers):
    newString = ''
    if listValue!=[]: #if there are qualitative values in the text
        if listModifiers!=[]: #if there are 'modifiers' in the sentence
            for i in posValue: #for each position in the list of positions
                ind_val = posValue.index(i) #we keep the indexof this value in the list
                for j in posModifiers: #for each modifier found
                    ind_mod = posModifiers.index(j) #we store its index in the list
                    if j[0] < i[0] and newString=='': #if the modifier is situated before the value
                        newString = listModifiers[ind_mod] + ' ' + listValue[ind_val] #then we concatenate them
                        listValue[ind_val]=newString #we replace the new value in the list of values
    return(listValue)
    #returns the list of value with replaced values if needed
      
# --------------------------------------------------------------------------- #

#in case of unexplicable double matches for some values
def deleteDouble3(listItem, listPos):
    if listItem!=[] and listPos!=[]:
        n = len(listItem)
        i = 0
        while i < n:
            if n>1:
                if (listPos[i][0] == listPos[i-1][0] or (listPos[i][0]>listPos[i-1][0] and listPos[i][0]<listPos[i-1][1])):
                #if the start position of a word is the same start position than the last word in the list
                #or if the start position of the world is included in the interval of position of the precedent one
                #then it is a double detection or a word is included in an other
                    del listPos[i] #we delete the double word
                    del listItem[i] #we delete its positions 
                    i = i-1 #we stay at the same index
                    n = n-1 #the list is shorter of 1 item
            i = i + 1 #we search in the rest of the list
    return(listItem, listPos)
    #returns the list of items and their positions cleaned
    