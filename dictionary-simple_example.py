## Dictionary 

bDay = {'Alice' : '01-02-87', 'Bob' : '02-03-66'}

def addBday (pName):
    global bDay
    
    print ('Type a birthday for ' + pName + ' : [dd-mm-yy]')
    pBDay = input()
    bDay[pName] = pBDay
    print (str(pName) + ':' + str(bDay[pName]) + ' Was added')

while True:
    print ('Please type a name to search for or blank to exit')
    try:
        pName = input()
        if pName in bDay:
            print (bDay[pName])
        elif (len(pName) == 0):
            print ('exit while')
            break;
        else:
            print ('We couldnt find ' + pName + ' in our list \nWould you like to add a new one ? Type "y" or blank to ignore')
            print (str.lower(pAnswer))
            if (str.lower(pAnswer) == 'y'):
                addBday (pName)
    except ValueError:
        print ('you must type a string')
