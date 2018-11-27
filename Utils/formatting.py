# Bryan BESSAUD           #
# 27/11/2018              #
# RecSys Competition 2018 #
# Politecnico di Milano   #


# Turning a list of 10 elements into a string
# input =>  a list of the elements to be recommended 
#           /!\ It must contain elements
# output => a string of the well-formatted 10 elements, ready for submission
def fromListToString(targetList) :
    
    # warning in case of abnormal number of recommendations
    if len(targetList) != 10 :
        print("WARNING : not exactly 10 tracks recommended")
    
    # output string
    outputString = ""
    
    # creating the output string
    for index in range(0, len(targetList)) :
        if type(targetList[index] != str) :
            if index != len(targetList) - 1 :
                outputString += str(targetList[index]) + " "
            else :
                outputString += str(targetList[index])
        else :
            if index != len(targetList) - 1 :
                outputString += targetList[index] + " "
            else :
                outputString += targetList[index]
             
    return outputString
  