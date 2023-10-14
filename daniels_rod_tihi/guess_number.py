import random

low_number = 1
high_number = 10

number = random.randint(low_number,high_number)

guess = input("Gæt et tal mellem " + str(low_number) +" og " + str(high_number) + ": ")

if int(guess) == number:
    print("Tillykke, du gættede rigtigt!")
    
else: 
    print("Det var desværre forkert. Tallet var " + str(number))
