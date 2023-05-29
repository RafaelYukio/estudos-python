print("Welcome to the quiz!")

playing = input("Dou you want to play? [1] - Yes / [2] - No: ")

if(playing != "1"):
    quit()
    
print("Let's start!")

points = 0
total_points = 5

answer = input("1 + 7 = ")

if(answer == "8"):
    print("Correct!")
    points += 1
else:
    print("Not correct!")

answer = input("13 + 25 = ")

if(answer == "38"):
    print("Correct!")
    points += 1
else:
    print("Not correct!")

answer = input("3 * 17 = ")

if(answer == "51"):
    print("Correct!")
    points += 1
else:
    print("Not correct!")

answer = input("36 / 9 = ")

if(answer == "4"):
    print("Correct!")
    points += 1
else:
    print("Not correct!")

answer = input("95 * 7 = ")

if(answer == "665"):
    print("Correct!")
    points += 1
else:
    print("Not correct!")

percentage = points/total_points * 100

print(f"Your score is: {points}, {percentage}%")
