#RockPaperScissors_v1.py

p1_choice = raw_input("Player 1, enter your choice <rock,paper,scissors>: ")
p2_choice = raw_input("Player 2, enter your choice <rock,paper,scissors>: ")


if p1_choice == "rock":
   if p2_choice == "scissors":
        print "Player 1 wins"
   elif p2_choice == "paper":
       print "Player 2 wins"
   elif p2_choice == "rock":
       print "Tie"
   else:
       print "Player 2 input is in error"
elif p1_choice == "paper":
    if p2_choice == "scissors":
        print "Player 2 wins"
    elif p2_choice == "paper":
        print "Tie"
    elif p2_choice == "rock":
        print "Player 1 wins"
    else:
        print "Player 2 input is in error"
elif p1_choice == "scissors":
    if p2_choice == "scissors":
        print "Tie"
    elif p2_choice == "paper":
        print "Player 1 wins"
    elif p2_choice == "rock":
        print "Player 2 wins"
    else:
        print "Player 2 input is in error"
else:
    print "Player 1 input is in error"

