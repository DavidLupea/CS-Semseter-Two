#Read 2 names from terminal and write the names to a file
#Format: One name per line

filehandle = open('kids.txt', 'w')          #w = wirte
#Will establish connection between the python script and the file

for i in range(2):
    name = raw_input('Enter a name: ')
    filehandle.write(name + '\n')
filehandle.close()
#Will close connection / stream
