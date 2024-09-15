import random
print("Welcome To The Random Number Guessing Game\n Try To Guess A Random Number")

i=1
rand= random.randint(1,100)
#print(rand)
while True:
    guess=input("Guess a number: ")
    try:
        guess=int(guess)
        if guess>=0:
            if guess<rand:
                print("Your guess is too low")
                #break
                i+=1
            elif guess>rand:
                print("Your Guess is too high")
                #break
                i+=1
            elif guess==rand:
                print("Congratulations you have guessed the right number in ",i,"attempts")
                break
        else:
            print("Enter a number which is 0 or more than 0")
    except ValueError:
        print("Enter a Numeric value")



