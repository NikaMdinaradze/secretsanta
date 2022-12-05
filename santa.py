import random
from os import system, name

mimgebebi = []
mchuqnelebi = []


saxeli = "saxeli"
while saxeli != "":
    saxeli = input("chaswerei saxeli: ")
    mimgebebi.append(saxeli)
    mchuqnelebi.append(saxeli)

mimgebebi.pop()
mchuqnelebi.pop()



for mchuqneli in mchuqnelebi:
    random_mimgebi = random.choice(mimgebebi)
    while random_mimgebi == mchuqneli:
        random_mimgebi = random.choice(mimgebebi)
    mimgebebi.remove(random_mimgebi)
    print(mchuqneli)
    input()
    print(random_mimgebi)
    input()
    system('cls')


    
    


