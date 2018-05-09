#David Lupea
#IntroCS2 pd5
#HW34 -- End ofEndOfFiles
#2018-5-08

#Reads a .csv file consisting of 3 rows: a last name, a first name and an unknown number of letter grades:
#A being 4, B being 3, C being 2, D being 1 and F being 0 points. Computes and prints the grade point average
#of each student.

def gradepointAVG(filename):
    fileIn = open(filename, 'rU')

    names = []
    grades = []
    for line in fileIn:
        data = line.strip().split(',')
        
        names.append(data[1] + ' ' + data[0])

        total = 0
        num_grades = len(data[2])

        for letter in data[2].upper():
            if letter == 'A':
                total += 4.0
            elif letter == 'B':
                total += 3.0
            elif letter == 'C':
                total += 2.0
            elif letter == 'D':
                total += 1.0
            else:
                total += 0.0

        grades.append(total / num_grades)
    

    fileIn.close()

    for i in range(len(names)):
        if grades[i] > 3.75:
            print names[i] + '  ' +str(grades[i]) + ' *'
        else:
            print names[i] + '  ' +str(grades[i])
                       
        
    

    
