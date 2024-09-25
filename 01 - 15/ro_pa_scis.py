import random
#n = 1:rock / 2:papper / 3:scissors

def play(n):

    get_random = random.randint(1, 3)
    if n == 1 and get_random == 1:
        print("no winners")
    if n == 1 and get_random == 2:
        print("you lose")
    if n == 1 and get_random == 3:
        print("you win")
    
    return

n = 1
print(play(n))