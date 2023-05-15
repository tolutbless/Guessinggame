import random

print("The Random Number Game")
Chosen_num = random.randint(1, 100)
print()
print()
print("Lets get it started")
while True:
 Player_1 = int(input("Player 1 guess the chosen number: "))
 Player_2 = int(input("Player 2 guess the chosen number: "))
 Player_3 = int(input("Player 3 guess the chosen number: "))
 print()
 print("Who guessed right?")
 print()
 print("Player 1 your result")
 if Player_1 == Chosen_num:
   print("You guessed right")
 if Player_1 < Chosen_num:
   print("That is lower than chosen number")
 if Player_1 > Chosen_num:
   print("That is greater than chosen number")
   print()
 print("Player 2, your result")  
 if Player_2 == Chosen_num:
   print("You guessed right")
 if Player_2 < Chosen_num:
   print("That is lower than chosen number")
 if Player_2 > Chosen_num:
   print("That is greater than chosen number")
   print()
   print("Player 3, your result")  
 if Player_3 == Chosen_num:
   print("You guessed right")
 if Player_3 < Chosen_num:
   print("That is lower than chosen number")
 if Player_3 > Chosen_num:
   print("That is greater than chosen number")
   print()
 if Player_1 and Player_2 and Player_3 != Chosen_num:
   print("The chosen number is ", Chosen_num)
   Next = input("Do you want to try again? ")
   if Next == "No":
     print("End")
     break
 