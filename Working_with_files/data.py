#adds a record to a csv file
#format last, first, age
#filename
filename = 'data.csv'


#fileobject to append with
fileOut = open(filename, 'w')

#prompt the user to enter data
last = raw_input('Enter a last name: ')
first = raw_input('Enter a first name: ')
age = raw_input('Enter an age: ')

#Clean up data
last.strip().title()
first.strip().title
age.strip()

#Send data
record = last + ',' + first + ',' + age + '\n'
fileOut.write(record)

#close fileobject
fileOut.close()
