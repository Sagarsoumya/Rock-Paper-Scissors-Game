# 0 for rock
# 1 for paper
# 2 for scissors
import random

user=int(input("Enter your choice :"))
a=random.randint(0,2)
print("computer input is "+str(a))

if a==user:
    print("It is a draw.")

if a>user :
    if(a==2 & user == 0):
        print("user win")
    else :
        print("Computer win")    
if user>a :
    if(user==2 & a == 0):
        print("computer win")
    else :
        print("user win")
