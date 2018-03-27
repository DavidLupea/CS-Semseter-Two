#David Lupea and Kevin Mesta
#David Lupea
#IntroCS2 pd5
#HW11 -- RockPaperScissors
#2018-3-4

#RockPaperScissors_v1.py
p1_choice = raw_input("Player 1, enter your choice <rock,paper,scissors>: ") #asks for player one to input their choice
p2_choice = raw_input("Player 2, enter your choice <rock,paper,scissors>: ") #asks for player two to input their choice 


if p1_choice == "rock": #checks if player ones choice is rock
   if p2_choice == "scissors":	#Based on player two's choice, it determines if who won or if it is a tie
        print "Player 1 wins"  #if rock and then scissors that means player one wins
   elif p2_choice == "paper": #checks if player twos choice is paper
       print "Player 2 wins" #if rock and then paper that means player two wins
   elif p2_choice == "rock": #checks if player two chose rock
       print "Tie" #if rock and then rock then tie
   else: 
       print "Player 2 input is in error" #If player two's input is none of the three options, it says that their input was in error
elif p1_choice == "paper": #checks if player ones choice is paper
    if p2_choice == "scissors": #checks if player twos choice is scissors
        print "Player 2 wins" #if rock and then scissors that means player two wins
    elif p2_choice == "paper": #checks if player twos choice is paper
        print "Tie"          #if paper and then paper that means its a ties between the players 
    elif p2_choice == "rock": #checks to see if player twos choice is rock
        print "Player 1 wins" #if paper and the rock player 1 wins
    else:
        print "Player 2 input is in error" #if none of these are chosen that means player twos input was an error
elif p1_choice == "scissors": #checks if player ones choice is scissors
    if p2_choice == "scissors": #checks if player twos choice is scissors
        print "Tie" #if scissors and then scissors then thats a tie
    elif p2_choice == "paper": #checks if player twos choice is paper
        print "Player 1 wins" #if scissors and then paper that maeans player one wins
    elif p2_choice == "rock": #checks to see if player twos choice is rock
        print "Player 2 wins" #if scissors and then rock then player two wins
    else: 
        print "Player 2 input is in error" #if non of these are chosen that means player twos input is an error
else:
    print "Player 1 input is in error" #if players choice is none of the above that means the input was an error
    
 

#RockPaperScissors_v2.py
import random  #imports the random library to use rand.int
h_choice = raw_input("Human, enter your choice <rock,paper,scissors>: ") #asks the human to enter one of rock,paper,or scissors

comp_num = random.randint(1,3) #chooss a random number from 1 2 or 3

if comp_num == 1:
    comp_choice = "rock" i#f the random number is one then the computers choice is rock
elif comp_num == 2:
    comp_choice = "paper" #if the random number is two then the computers choice is paper
else:
    comp_choice = "scissors" #if the random number is three the computers choice is paper

print "Computer chooses", comp_choice #prints the computers choice

def rock_paper_scissors(human, comp): #a function that takes two inputs, the humans choice and the compuyters
    if human == "rock":
       if comp == "scissors":
            print "Human wins" #If human picks rock and comp picks scissors human wins
       elif comp == "paper":
           print "Computer wins" #If human picks rock and comp picks paper computer wins
       else:
           print "Tie" #If human picks rock and comp picks rock then they tie
    elif human == "paper":
        if comp == "rock": 
            print "Human wins" #If human picks paper and comp picks rock human wins
        elif comp == "scissors":
            print "Computer wins" #If human picks paper and comp picks scissors computer wins
        else:
            print "Tie" #If human picks paper and comp picks paper then they tie
    elif human == "scissors":
        if comp == "paper":
            print "Human wins" #If human picks scissors and comp picks paper human wins
        elif comp == "rock":
            print "Computer wins" #If human picks scissors and comp picks rock computer wins
        else:
            print "Tie" #If human picks scissors and comp picks scissors then they tie
    else:
        print "Human input is in error" #if human did not choose, rock paper or scissors then they put in an error
rock_paper_scissors(h_choice, comp_choice) #executes the function above using the humans choice and the computers choice



