''' 
 Author: Dan Blanchette
 Date: July 1, 2023
 Description: This Program will generate random overworld encounters for the Dungeon Master (User).
'''


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
         print("Two encounters!  Rolling 2d4.")
         value1 = random.randrange(1, 4)
         print("d4 #1 rolled: ", value1)
         value2 = random.randrange(1, 4)
         print("d4 #2 rolled: ", value2)
         print("Special Encounter 1: ")
         rand_encounter(value1, monster)
         print("Special Encounter 2: ")
         rand_encounter(value2, monster)
      case 6:
         print("Two encounters!  Rolling 2d4.")
         value1 = random.randrange(1, 4)
         print("d4 #1 rolled: ", value1)
         value2 = random.randrange(1, 4)
         print("d4 #2 rolled: ", value2)
         print("Special Encounter 1: ")
         rand_encounter(value1, monster)
         print("Special Encounter 2: ")
         rand_encounter(value2, monster)
      case 7:
         print("No Encounter.")
      case 8:
         print("No Encounter.")
      case _:
         print("no matching case!")

def main():
   # Rand Encounter Monsters list (edit as needed)
   monsters = ['Yeti', 'Goliath Werebear', 'Crag Cats', 'Coldlight Walker', 'Ice Troll',
               'Frost Druid and Friends', 'Chardalyn Berserkers', 'Frost Giant Riding a Mammoth',
               'Battlehammer Dwarves', 'Arveiaturace(Ancient White Dragon)', 'Snowy Owlbear',
               'Gnolls', 'Orcs of the Many-Arrows Tribe', 'Goliath Party', 'Chwinga', 'Awakened Beast',
               'Icewind kobolds', 'Humans', 'Herd of beasts', 'Perytons']

   hours = input("How many hours is your party travelling?[24 hours min]: ")
   # make sure they party is travelling at least one day
   if int(hours) < 24:
      print('Please enter at least 24 hours')
      exit(0)
   else:
      days = num_days(int(hours))

   if days == 1:
      rand_num = random.randrange(1, 8)
      rand_encounter(rand_num, monsters)
      print("\n")
   else:
      for i in range(days):
         print(f"Encounter {i+1}: ")
         rand_num = random.randrange(1, 8)
         # print(f"Encounter {i+1}: ", i)
         rand_encounter(rand_num, monsters)
         print("\n")

if __name__=="__main__":
   main()
