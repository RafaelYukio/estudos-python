import random

random_number = random.randint(0, 100)
guessing = "-1"

def check_int(input_number):

    if input_number == -1:
        message = "Guess a number between 0 and 100: "
    elif input_number > random_number:
        message = "Try a smaller number: "
    else:
        message = "Try a bigger number: "            
        
    input_number = input(message)
    while input_number.isdigit() != True:
        input_number = input("Enter a correct number: ")
    return input_number

print("Let's start!")

while int(guessing) != random_number:
    guessing = check_int(int(guessing))
    print(random_number)

if int(guessing) == random_number:
    print(f"You win! The number is {random_number}!")
