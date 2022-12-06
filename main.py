import random
print("welcome to Rolling Dice Game")
def rolldice(min,max):
     score = 0
     while True:
         a=int(input("Enter your Guess:"))
         wins=0
         if 0<a<7:
             print("your number:",a)
         else:
             print("Error")
             print("Since we are rolling a single dice you can select your number from the range 1 to 6")
             continue
         print("rolling dice....")
         number = random.randint(min, max)
         print(f"Dice number : {number}")
         if a==number:
             print("Congratulations You Won")
             score+=1
             print("Congrat's, you score",score," points")
             rand=random.randint(1,6)
             print()
         else:
             print("you lose")
             print("Better Luck Next Time!")
         choice = input("Do you want to Roll the dice again press enter! if you need to exit type no and press enter? (press enter/no)")
         if choice.lower() == 'no':
           print("Your total score is", score)
           break
           if choice.lower() == '':
             continue
rolldice(1,6)
