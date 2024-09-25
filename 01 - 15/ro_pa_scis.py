import random
#n = 1:rock / 2:papper / 3:scissors
""""
rock = ("✊")
paper = ("🖐️")
scis = ("🫰")

def play(n):

    get_random = random.randint(1, 3)

    if n == 1 and get_random == 1:
        print (f"{rock} vs {rock}")
        print("no winners")
    if n == 1 and get_random == 2:
        print (f"{rock} vs {paper}")
        print("you lose")
    if n == 1 and get_random == 3:
        print (f"{rock} vs {scis}")
        print("you win")

    if n == 2 and get_random == 1:
        print (f"{paper} vs {rock}")
        print("you win")
    if n == 2 and get_random == 2:
        print (f"{paper} vs {paper}")
        print("no winner")
    if n == 2 and get_random == 3:
        print (f"{paper} vs {scis}")
        print("you lose")

    if n == 3 and get_random == 1:
        print (f"{scis} vs {rock}")
        print("you lose")
    if n == 3 and get_random == 2:
        print (f"{scis} vs {paper}")
        print("you win")
    if n == 3 and get_random == 3:
        print (f"{scis} vs {scis}")
        print("no winners")
    
    return

n = 2
print(play(n))
"""
# Choices
rock = "✊"
paper = "🖐️"
scissors = "🫰"

def play(n):
    get_random = random.randint(1, 3)

    # Mapping number to the corresponding symbol
    symbols = {1: rock, 2: paper, 3: scissors}
    
    # Print the choices
    print(f"{symbols[n]} vs {symbols[get_random]}")

    # Determine the result
    if n == get_random:
        print("No winners")
    elif (n == 1 and get_random == 3) or (n == 2 and get_random == 1) or (n == 3 and get_random == 2):
        print("You win")
    else:
        print("You lose")

# Prompt for user input
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("Choose your option: 1: Rock ✊, 2: Paper 🖐️, 3: Scissors 🫰")
n = int(input("Enter the number corresponding to your choice: "))

# Play the game
play(n)