import random
import math

menu = {}

def add_lizard(name, gender, color, age):
  temp = {"Gender":gender, "Color":color, "Age":age}
  menu[name] = temp

print("Currently, you have these lizards:", end=" ")
for lizard in menu.keys():
  print(lizard, end=", ")

print()

def new():
  name = input("What is the name of the new lizard? ")
  while name in menu: 
    print("Name is already in use you idiot, I'm starting to think you are a jew.")
    name = input("What is the name of the new lizard? ")
  gender = input("What is its gender? (F or M) ")
  while gender != "F" and gender != "M": 
    print("You fucking jew, there are 2 options. Piece of jewish nigga.")
  color = input("Can you describe its color? ")
  age_correct = False
  age = input("How old is it? (years old) ")
  while not age_correct:
    try:
      age = float(age)
      age_correct = True
    except ValueError:
      print("Did you learn Math you Juden????")
      age = input("How old is it? ")
      age_correct = False


  add_lizard(name, gender, color, age)
  print("Currently, you have these lizards:", end=" ")
  for lizard in menu.keys():
    print(lizard, end=", ")

  print()


while True:
  add = input("Would you like to add a lizard? (Y or N) ")
  while add != "Y" and add != "N" and add != "K":
    print("So you said you're a jew???")
    add = input("Would you like to add a lizard? (Y or N) ")

  if add == "N":
    print("Adding finished. Your farm currently has these lizards: ")
    for lizard in menu.keys():
      print(lizard + ": ",menu[lizard])

  elif add == "K":
    if not bool(menu):
      print("Farm empty, you are spared this time.")
      continue
    kill = random.choice(list(menu.keys()))
    print("\n",kill, "was sacrificed to hungry kids in Africa.\n")
    menu.pop(kill)
    
    print("Currently, you have these lizards:", end=" ")
    for lizard in menu.keys():
      print(lizard)
    print()

  else:
    new()