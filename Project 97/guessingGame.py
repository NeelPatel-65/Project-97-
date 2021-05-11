import random
guessit = random.randint(1,9)
guess = int(input("enter a integer from 1 to 9"))
while guessit != "guess":
    print
    if guess < guessit:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 9: "))
    elif guess > guessit:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print ("you guessed it!")
        break
    print
