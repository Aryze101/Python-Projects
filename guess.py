from random import *
a=int(input("Enter Lower Bounds for guessing:"))
b=int(input("Enter Higher Bounds for guessing:"))
number=randint(a,b)
end=0
while(end!=1):
  guess=int(input("Enter your guess:"))
  if(guess==number):
    print("Correct!")
    end=1
  elif(guess>number):
    print("Lower than that!")
  else:
    print("Higher than that!")

