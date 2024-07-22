import random
import randomodule


random_intiger = random.randint(1, 10)
print(random_intiger)
print(randomodule.codigo)

"""flip coin"""

flip = random.randint(0, 1)
if flip == 0:
  print("Tails")
elif flip == 1:
  print("Heads")

"""random float"""

random_float = random.random()
print(random_float)

""" random between 0 - 5 """
random_between = random.random() * 5
print(random_between)

""" choose random """

input = ["pipi", "popo", "pepe", "pupu", "papa"]
random_name = random.choice(input)
print(f"{random_name} is going to buy the meal today!")

""" choose b """
names = names_string.split(", ")
# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[random_choice])