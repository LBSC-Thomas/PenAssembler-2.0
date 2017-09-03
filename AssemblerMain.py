#Main file of the PenAssembler V2.0.

import helper

#This is the instruction set layed out plus some keywords exclusive to assembly.
functionTable = {"NOP":"000", "ADD":"001", "SUB":"010", "NAND":"011", "JMP":"100", "LD":"101"}
registerTable = {"R0":"00", "R1":"01", "R2":"10", "R3":"11"}
conditionTable = {"COUT":"00", "JEQ":"01", "NEG":"10", "JMP":"11"}
labelTable = {}

#This is the initialization of useful variables.
lineCounter = 0
functionField = "000"
sourceField = "00"
destinationField = "00"
targetField = "00"
conditionField = "00"
valueField = "0000"
labelState = False

#This is loads the file.
fileImport = input("Please type in the directory of the file you'd like to assemble: ")
fileOpen = open(fileImport, "r")
fileRead = fileOpen.read()
fileLoad = str(fileRead)

#This is the main part of the assembler.
if fileLoad != None:
    program = fileLoad.split()

    #This part does the translation (Symbolic -> Binary)
    for symbol in program:
        if symbol in functionTable:
            functionField = functionTable.get(symbol, "000")
            lineCounter += 1
        elif helper.is_source(symbol) == True:
            registerSourceAddress = symbol.replace(",","")
            sourceField = registerTable.get(symbol, "00")
            lineCounter += 1
        elif helper.is_destination(symbol) == True:
            destinationField = registerTable(symbol, "00")
            lineCounter += 1
        elif helper.is_comment(symbol) == True:
            del symbol
            lineCounter += 1
        elif helper.is_value(symbol) == True:
            valueField = str(bin(symbol))
            lineCounter += 1
        '''elif helper.label(symbol) == True:
            labelTable[symbol] = lineCounter + 1
            lineCounter += 1
            labelState = True'''
        elif helper.is_target(symbol) == True:
            targetField = str(bin(symbol))
            lineCounter += 1
        elif symbol in conditionTable:
            conditionField = conditionTable.get(symbol, "00")
            lineCounter += 1

    if functionField == "000":
        print("0000000"+ "\n")
    elif functionField == "001":
        print(functionField + sourceField + destinationField + "\n")
    elif functionField == "010":
        print(functionField + sourceField + destinationField + "\n")
    elif functionField == "011":
        print(functionField + sourceField + destinationField + "\n")
    elif functionField == "100":
        print(functionField + targetField + conditionField + "\n")
    elif functionField == "101":
        print(functionField + valueField)