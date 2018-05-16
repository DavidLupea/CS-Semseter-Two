#Team David + Ling
#David Lupea and Ling Chen
#IntroCS2 pd 5
#MadLibs Lab
#2018-05-15

def main():
    fileIn = open('Jungle.txt', 'rU')

    text = fileIn.read()
          
    manimal = raw_input("What is the animal? ")
    mfood = raw_input("What is the food? ")
    mcity = raw_input("What is the name of the city? ")

    fileIn.close()

    fileOut = open('JungleMadLibs.txt', 'w')
    fileOut.write(text.format(animal = manimal, food = mfood, city = mcity))

    fileOut.close()

main()
      
        
        
