import random

def num_days(hours):
   days = int(hours / 24)
   # print(days)
   return days
# d8 How many random encounters
def rand_encounter(number, monster):
   match int(number):
      case 1:
         print("One encounter in the morning at (dawn - noon).")
         rand_num = random.randrange(1, 20)
         print("The party faces: ", monster[rand_num])
         print("The number rolled was", rand_num)
      case 2:
         print("One encounter in the afternoon(noon - dusk).")
         rand_num = random.randrange(1, 20)
         print("The party faces: ", monster[rand_num])
         print("The number rolled was", rand_num)
      case 3:
         print("One encounter in the evening (dusk - midnight).")
         rand_num = random.randrange(1, 20)
         print("The party faces: ", monster[rand_num])
         print("The number rolled was", rand_num)
      case 4:
         print("One encounter in the night (midnight - dawn).")
         rand_num = random.randrange(1, 20)
         print("The party faces: ", monster[rand_num])
         print("The number rolled was", rand_num)
      case 5:
         print("Two encounters;  Rolling 2d4.")
         value1 = random.randrange(1, 4)
         print("The number rolled was", value1)
         value2 = random.randrange(1, 4)
         print("The number rolled was", value2)
         print("Encounter_1:", rand_encounter(value1, monster))
         print("Encounter_2:", rand_encounter(value2, monster))
      case 6:
         print("Two encounters;  Rolling 2d4.")
         value1 = random.randrange(1, 4)
         print("The number rolled was", value1)
         value2 = random.randrange(1, 4)
         print("The number rolled was", value2)
         print("Encounter_1:", rand_encounter(value1, monster))
         print("Encounter_2:", rand_encounter(value2, monster))
      case 7:
         print("No encounter.")
      case 8:
         print("No encounter.")
      case _:
         print("no matching case!")
# Rand Encounter Monsters list (edit as needed)
monsters = ['Yeti', 'Goliath werebear', 'Crag cats', 'Coldlight walker', 'Ice troll',
            'Frost druid and friends', 'Chardalyn berserkers', 'Frost Giant riding a mammoth',
            'Battlehammer dwarves', 'Arveiaturace(Ancient white dragon)', 'Snowy Owlbear',
            'Gnolls', 'Orcs of the Many-Arrows tribe', 'Goliath party', 'Chwinga', 'Awakened beast',
            'Icewind kobolds', 'Humans', 'Herd of beasts', 'Perytons']

hours = input("How many hours is your party travelling? ")
days = num_days(int(hours))

if days == 1:
   rand_num = random.randrange(1, 8)
   rand_encounter(rand_num, monsters)
else:
   for i in range(days):
      rand_num = random.randrange(1, 8)
      print(f"Encounter %d: ", i)
      rand_encounter(rand_num, monsters)
