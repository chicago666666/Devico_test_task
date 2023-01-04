import json

with open('animals.json', 'r') as animals_file:
    animals_j = json.load(animals_file)
    global pigs, chickens, cows 
    animals = animals_j
    print(animals)
    pigs = animals.get("pigs")
    chickens = animals.get("chickens")
    cows = animals.get("cows")

print("На ферме свинок: " + str(pigs) + " по 4 ратыци у каждой")
print("На ферме циплят: " + str(chickens) + " по 2 лапки у каждой")
print("На ферме коров: " +  str(cows) +  " по 4 копыта у каждой")


def total_legs(pigs, chickens, cows):
    print ("Всего лап, копыт и ратыць на ферме: " + str(chickens*2 + cows*4 +pigs*4))

total_legs(pigs, chickens, cows)
