import random

def rollStat():
    diceRolls = []
    for i in range(4):
        roll = random.randint(1,6)
        diceRolls.append(roll)

    lowest = min(diceRolls)
    print(diceRolls)
    diceRolls.remove(lowest)
    
    stat = 0
    for i in range(len(diceRolls)):
        stat = stat + diceRolls[i]

    return stat

def rollForStats():
    statTotal = 0

    while statTotal < 72:
        statNumbers = []
        for i in range(6):
            statNumbers.append(rollStat())
        statTotal = sum(statNumbers)

    return statNumbers

abilities = ['str', 'dex', 'con', 'wis', 'int', 'cha']
stats = rollForStats()

for i in range(len(abilities)):
    print(str(abilities[i]) + ': ' + str(stats[i]))

print(sum(stats))