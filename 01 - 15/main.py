""" L05 sumar ab > a + b """
two_digit_number = input() #input = XX
num = int(two_digit_number) # force int / two_digit_number(39) = str not int
a = num // 10 # decenas
b = num % 10 # unidades
print(a + b)
"""L05 ver 2"""
two_digit_number = input()
first_digit = int(two_digit_number[0]) #access 1st
second_digit = int(two_digit_number[1]) #access 12nd
two_digit_number = first_digit + second_digit
print(two_digit_number)
""" int y float A"""
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# Write your code below this line 👇
new_height = float(height)
new_weight = int(weight)
fh = new_height * new_height
he_to_int = fh * 100
tt = int(he_to_int)
bmi = (new_weight * 100) / tt
f_bmi = int(bmi)
print(f_bmi)
"""print(type(a)) B"""
bmi = new_weight / new_height ** 2 #square
bmi = new_height / (new_height * new_height)
bmi_to_int = int(bmi)
print(bmi_to_int)
"""weeks left"""
age = input()
year = int(52)
age_int = int(age)
lifelong = year * age_int
wholelife = int(4680)
leftlife = wholelife - lifelong
life = str(leftlife)
print("You have " + life + " weeks left.")
"""solution"""
age = input()
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")
"""tip calculator"""
#If the bill was $150.00, split between 5 people, with 12% tip. 
print("welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
tip = int(input("What porcentage of tip would you like too give? 10, 12 or 15? "))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
people = int(input("How many people to split the bill? "))
#Write your code below this line 👇
tip_pp = (bill / people) * tip / 100
total_each = (bill / people) + tip_pp
final_total = round(total_each, 2)
final_total = "{:.2f}".format(total_each)
print(f"Each one pay: ${final_total}")
"""if indent"""
year = int(input())
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0: 
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
"""pizza python"""
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
"""truelove code"""
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

codet = "true"
codel = "love"
love_score = 0
true_score = 0

sum_names = (name1).lower() + (name2).lower()

for letter in codet:
  love_score += sum_names.count(letter)

for letter in codel:
  true_score += sum_names.count(letter)

total = str(love_score) + str(true_score)
intotal = int(total)

if intotal < 10 or intotal > 90:
  print(f"Your score is {intotal}, you go together like coke and mentos.")
elif intotal >= 40 and intotal <= 50:
  print(f"Your score is {intotal}, you are alright together.")
else:
  print(f"Your score is {intotal}.")
"""true love solution"""
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
"""band name"""
#1. Create a greeting for your program.
print("Welcome to the band name generator")
#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up?\n")
#3. Ask the user for the name of a pet.
pet = input("your pet name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("your band name is " +  city + " " + pet)
#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end
"""tip generator"""
#If the bill was $150.00, split between 5 people, with 12% tip. 
print("welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
tip = int(input("What porcentage of tip would you like too give? 10, 12 or 15? "))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
people = int(input("How many people to split the bill? "))
#Write your code below this line 👇
tip_pp = (bill / people) * tip / 100
total_each = (bill / people) + tip_pp
final_total = round(total_each, 2)
final_total = "{:.2f}".format(total_each)
print(f"Each one pay: ${final_total}")
"""ride ticket"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")
"""teasure game"""
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
stage1 = input('>>Where do you want to go? \n "left" or "right"\n').lower()
if stage1 == "left":
  stage2 = input('You\'re in the middle of the lake.\n >>Do you want to: \n"swim" or "wait" for the boat\n').lower()
  if stage2 == "wait":
    stage3 = input('You found the boat and you are in the island.\n >>Which door do you want to open? \n"red", "blue" or "yellow"\n')
    if stage3 == "yellow":
      print("YEEEY You win!!")
    elif stage3 == "red":
      print("OUCH! You are burned by fire. Game over!")
    elif stage3 == "blue":
      print("you are eaten by beasts. Game over!")
    else:
      print("Game Over")
  else:
    print("You are attacked by the trout. Game over!")
else: 
  print("You fell into the hole, Game over uwu")