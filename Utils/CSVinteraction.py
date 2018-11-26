# Bryan BESSAUD           #
# 21/11/2018              #
# RecSys Competition 2018 #
# Politecnico di Milano   #

# mandatory import
import csv




# Exctraction of a content list from a csv
# input =>  a string of the full input file name. 
#           /!\ It must be a .csv file
# output => a list of lists, containing the rows of the input file
def fromCSVtoList(targetCSV) :
    
    # output list
    targetList = []
    
    # opening the CSV in read-only mode
    inputFile = open(targetCSV, 'r')
    csvInputReader = csv.reader(inputFile)
    
    # reading and extracting content
    for row in csvInputReader :
        targetList.append(row)
           
    # closing the CSV
    inputFile.close()
    
    return targetList




# Creation of a csv file of dimension 10 000 x 2
# inputs => targetList
#               Contains the target playlists and recommendations.
#               /!\ Its dimension must be 10 000 x 2
#           targetCSV
#               a string of the full output file name. 
#               /!\ It must be a .csv file.
#               /!\ It should be empty or not already greater than 10 000 x 2 and will be erased !
def fromListToCSV(targetList, targetCSV) :
    
    # opening the CSV in writing mode
    outputFile = open(targetCSV, 'w+', newline='')
    csvOutputWriter = csv.writer(outputFile)
    
    # writing content
    for row in targetList :
            csvOutputWriter.writerow(row)
      
    # closing the CSV
    outputFile.close() 
    
    return 0




# Exctraction of the number of rows in CSV
# input =>  a string of the full input file name. 
#           /!\ It must be a .csv file
# output => an integer of the number of rows in the input file
def getCSVtotalRows(targetCSV) :
    
    # output integer
    amountOfRows = 0
    
    # opening the CSV in read-only mode
    inputFile = open(targetCSV, 'r')
    csvInputReader = csv.reader(inputFile)
    
    # reading and extracting content
    for row in csvInputReader :
        amountOfRows += 1
           
    # closing the CSV
    inputFile.close()
    
    return amountOfRows 



  