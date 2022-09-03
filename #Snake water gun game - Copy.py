#Snake water gun
#game of 10
# snake>water , gun>snake , water>gun

import random

pp=0
cp=0
rounds=10
drounds=0
print("Pamu neeru thupaki aata")

while (rounds>0):
     
     cw=["snake" , "water" , "gun"]
     cwchoice=random.choice(cw)
    
     print("enter your choice")
     pwchoice=input()

     print("AI selects:",cwchoice )
     if pwchoice=="snake" :
         if cwchoice=="snake" :
          print("round draw")
          drounds += 1

         elif cwchoice=="water" :
            print("Player Wins the round!")
            pp += 1
         else :
            print("AI wins , You lose the round!")
            cp += 1
    
     elif pwchoice=="water" :
        if cwchoice=="water" :
            print("Round draw")
            drounds += 1
        elif cwchoice=="gun" :
            print("You Win the round!")
            pp += 1
        else :
            print("AI wins , You lose the round!")
            cp += 1
        
     elif pwchoice=="gun" :
        if cwchoice=="gun" :
            print(" Round Draw")
            drounds +=1
        elif cwchoice=="snake" :
            print(" You Win the round! ")
            pp += 1
        else :
            print("AI wins , You lose the round ")
            cp += 1
     rounds -= 1

if pp>cp :
    print("You Win the game!")
elif pp==cp :
    print("Tied Game!") 
else :
    print("You lose the game ! " , end=" ")
print("Total score at the end is , player =", pp ," - " , "AI = " , cp )
print("Total draws =" , drounds)
