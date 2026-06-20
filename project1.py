#sank water gun game

import random

computer=random.choice([1,-1,0])
youstr=input("enter your chioce:")
youDist={"s":1,"w":-1,"g":0}
revseDist={1:"sank",-1:"water",0:"gun"}

you=youDist[youstr]

print(f"you choice :{revseDist[you]}\ncomputer choice  :{revseDist[computer]}")

if(computer==you):
    print("match draw")

else:
    if(computer==1 and you==-1):
        print("you lose")
    
    
    elif(computer==1 and you==0):
        print("you win")

    elif(computer==-1 and you==1):
        print("you win") 
    

    elif(computer==-1 and you==0):
        print("you lose ")
    

    elif(computer==0 and you==1):
        print("you lose")
    
    elif(computer==0 and you==-1):
        print("you lose")
    
    else:
        print("somthing with rong")