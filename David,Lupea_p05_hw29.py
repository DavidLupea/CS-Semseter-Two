#David Lupea
#IntroCS2 pd5
#HW29 -- BeginOfFiles
#2018-4-29

def text_file_copy(filename):
    newname = filename[:-4] + 'COPY' + filename[-4:]
    
    firstfile = open(filename, 'r')

    text = ''
    for line in firstfile:
        text = text + line.upper()
    firstfile.close()

    secondfile = open(newname, 'w')

    secondfile.write(text)

    secondfile.close()
    
    
    
