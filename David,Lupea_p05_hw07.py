#David Lupea
#IntroCS2 pd<5
#HW7 -- PassJudgement
#2018-2-26   


def pythTriple(a, b, c):
#Checks to see if they are all integers(all triples are integers)
    if type(a) == int and type(b) == int and type(c) == int:
#Tries the three cases as to whether or not the sum of the square of the length of two sides equals the square of the length of the third
        if (a ** 2) + (b ** 2) == (c ** 2):
            return True
        elif (a ** 2) + (c ** 2) == (b ** 2):
            return True
        elif (b ** 2) + (c ** 2) == (a ** 2):
            return True
#If the sum of the squares of two sides are ot equal to the square of the third, it gives you false.
        else:
            return False
    else:
        return False


def gradeConnv(g):
#Runs through each of the letter grades to see which letter the score is on
    if (g < 65) and (g >= 0):
        return "F"
    elif (g >=65) and (g < 70):
        return "D"
    elif (g >= 70) and (g < 80):
        return "C"
    elif (g >= 80) and (g < 90):
        return "B"
    elif (g >= 90) and (g <= 100):
        return "A"
#If the score(g) is not in the range 0 <= g <= 100 it tells you the number is out of the accepted range
    else:
        return "Number out of range"

def passJudgement(letterGrade):
#Checks through each letter grade and gives it critiques based on it
    if letterGrade == "F":
        return "You did terrible, you failed. Did you even try!?"
    elif letterGrade == "D":
        return "You did very bad. Perhaps you should study next time?"
    elif letterGrade == "C":
        return "You did quite bad. Maybe a little more studying would have done the trick"
    elif letterGrade == "B":
        return "You did quite well. You were so close though. Review a bit better next time and you'll be at an A in no time"
#If all else is false then your grade must have been an A in which case it will tell you that you did great.
    else:
        return "Great job. I can tell that you are knowledgeable... or you just crammed the night before"
    

