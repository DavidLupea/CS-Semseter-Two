    #Append two names to the end of the file
#One name per line

filehandle = open('kids.txt', 'a')              #a = append
filehandle.write('Yuki\n')
filehandle.write('Fred\n')
filehandle.close()
