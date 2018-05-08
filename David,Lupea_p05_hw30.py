#David Lupea
#IntroCS2 pd5
#HW29 -- BeginOfFilesTake2
#2018-4-30

#Question 1
def text_file_copy(filename):
    location = filename.find('.')
    newname = filename[:location] + 'COPY' + filename[location:]
    
    firstfile = open(filename, 'r')

    text = ''
    for line in firstfile:
        text = text + line.upper()
    firstfile.close()

    secondfile = open(newname, 'w')

    secondfile.write(text)

    secondfile.close()


#Question 2
def wordCount(filename):
    fileIn = open(filename, 'r')

    numlines, numwords, numchars = 0,0,0

    for line in fileIn:
        numlines += 1
        numchars += len(line)
        numwords += len(line.split())

    print numlines, numwords, numchars, filename

    fileIn.close()


#Question 3
def writeCSV(filename):
    fileOut = open(filename, 'a')

    last = raw_input('Enter a last name: ')
    first = raw_input('Enter a first name: ')
    age = raw_input('Enter an age: ')

    last.strip().title()
    first.strip().title
    age.strip()

    record = last + ',' + first + ',' + age + '\n'
    fileOut.write(record)

    fileOut.close()


#Start of Homework number 30
#Question 4
def readCSV(filename):
    fileIn = open(filename, 'r')                                                                                #Opens file for reading

    oldestAge = None                                                                                            #Sets the oldest age and oldest person to None
    oldestPerson = None
    
    for line in fileIn:                                                                                         #Iterates through each line in the CSV file
        data = line.strip('\n').split(',')                                                                      #Creates a list called data, the first value being the last name, the second being the first name and the third being teh age
        if int(data[2]) > oldestAge:                                                                            #If the integerized age is greater than the oldest age 
            oldestAge = int(data[2])                                                                            #It sets the oldest age to the integerized current age
            oldestPerson = data[1] + ' ' + data[0]                                                              #Sets the oldest person to the current name
    output = 'At age ' + str(oldestAge) + ', ' + oldestPerson + ' is the oldest person'                         #Creates a variable called output for formatting
    fileIn.close()                                                                                              #Closes file
    return output                                                                                               #Returns output
    

#Question 5
def readCSVwithTies(filename):
    fileIn = open(filename, 'r')                                                                                #Opens file for reading

    oldestAge = None                                                                                            #Sets oldest age to none
    oldestPeople = []                                                                                           #Sets oldest people to an empty list
    
    for line in fileIn:                                                                                         #Iterates through each line of the CSV file
        data = line.strip('\n').split(',')                                                                      #Creates a list of each value
        if int(data[2]) > oldestAge:                                                                            #If the integerized age is larger than the oldest age
            oldestAge = int(data[2])                                                                            #Sets the oldest age to the integerized current age
            oldestPeople = [data[1] + ' ' + data[0]]                                                            #Creates a list of oldest people containing only the current person
        elif int(data[2]) == oldestAge:                                                                         #If the integerized age is equal to the oldest age
            oldestPeople.append(data[1] + ' ' + data[0])                                                        #Adds the current person to the list of oldest people
    if len(oldestPeople) == 1:                                                                                  #Formatting
        output = 'At age ' + str(oldestAge) + ' '+ oldestPeople[0] + ', is the oldest person'
    elif len(oldestPeople) > 1:
        output = 'At age ' + str(oldestAge) + ', there is a ' + str(len(oldestPeople)) + ' way tie between, '
        for name in oldestPeople:
            output += name + ', '
        output += 'for the oldest person'
    fileIn.close()                                                                                              #Closes file
    return output                                                                                               #Returns outputs
        
    














    
