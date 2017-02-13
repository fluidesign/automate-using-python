#! python3
# Identify files larger then X in path Y

import sys, os

# vars
PATH_TO_SEARCH_IN = ""
MINIMUM_FILE_SIZE = ""

# function section
def converBytesToMB(number):
 
    number /= 1<<20
    return "%f" % (number)

def usage(case):

    if ( case == 1 ):
        print ("Please add folder to search in and the requried files size")  
    elif ( case == 2 ):
        print ("Wrong number parameters was identified")
    elif ( case == 3 ):
        print ("Wrong path or it doesnt exist")
    elif ( case == 4 ):
        print ("Size should be a number")
    
    print("Syntax: <Script.py> <folder path> <size in MB>")
    exit (int(case))

def verifyUserInput(folderPath, fileSize):

    if ( os.path.exists(folderPath) == False ):
        usage(3)
    elif ( fileSize.isdigit() == False ):
        usage(4)
        
def getUserInput(userInput): # we will use userinput as global params
    
    global PATH_TO_SEARCH_IN
    global MINIMUM_FILE_SIZE

    if (len(userInput) == 1 ): usage(1)
    elif (len(userInput) != 3 ): usage(2)
        
    verifyUserInput(userInput[1], userInput[2])
    
    PATH_TO_SEARCH_IN = userInput[1]
    MINIMUM_FILE_SIZE = userInput[2]

def findLargeFile():
    
    counter = 0 
    for subFolders, folders, files in os.walk(PATH_TO_SEARCH_IN): ## iterate the all folders
        for file in files:
            _file = os.path.join(subFolders,file)
            _fileSize = float(converBytesToMB((os.stat(_file).st_size)))
            if (( _fileSize ) > float(MINIMUM_FILE_SIZE) ):
                print (str(_file) + " size : " + str(_fileSize) + " Bigger then " + str(MINIMUM_FILE_SIZE))
                counter += 1
                
    if (counter == 0):
        print ("We couldnt identify any files larger then " + str(MINIMUM_FILE_SIZE) + " MB in : " + str(PATH_TO_SEARCH_IN))

def main(userInput):
    getUserInput(userInput)
    findLargeFile()
    
# end of functions

main(sys.argv)