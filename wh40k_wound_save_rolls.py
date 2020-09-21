import random

bs = int(input("Enter your BS: "))
num_rolls = int(input("Enter number of attacks: "))

rolls = []
total_hits = []
hit_rolls = []
wound_rolls = []

#initial rolls
for i in range(0,num_rolls):
    n = random.randint(1,6)
    rolls.append(n)
print(f"Rolls: {rolls}")

#rolls that pass bs
for bsnum in rolls:
    if bsnum >= bs:
        total_hits.append(bsnum)
print(f"No. of hits: {len(total_hits)}")

strength = int(input("Enter your strength: "))
toughness = int(input("Enter enemy toughness: "))

#rolling for wounds
for hr in range(0,len(total_hits)):
    h = random.randint(1,6)
    hit_rolls.append(h)
print(f"Hit rolls: {hit_rolls}")

#checking for strength vs. toughness
for num in hit_rolls:
    if strength / 2 >= toughness:
        if num >= 2:
            wound_rolls.append(num)

    elif strength > toughness:
        if num >= 3:
            wound_rolls.append(num)

    elif strength == toughness:
        if num >= 4:
            wound_rolls.append(num)
    else:
    # if strength is less than toughness
        if num >= 5:
            wound_rolls.append(num)

print(f"Total Wounds: {len(wound_rolls)}")

ap = int(input("Enter AP: "))
save = int(input("Enter save: "))
invuln = int(input("Enter invulnerable save. if none, enter 0: "))
save_rolls = []
failed_saves = []

if invuln < (save + abs(ap)) and invuln != 0:
    save = invuln

#rolling for saves
for sr in range(0,len(wound_rolls)):
    s = random.randint(1,6)
    save_rolls.append(s)

print(f"Save rolls: {save_rolls}")

#checking for successful saves
for num in save_rolls:
    if num <= save:
        failed_saves.append(num)

print(f"Failed saves: {len(failed_saves)}")