import random

def arvo():
    earthquake = False
    burglar = False
    alarm = False
    if random.random() < 1/111:
        earthquake = True
        
    if random.random() < 1/365:
        burglar = True

    if burglar and earthquake:
        if random.random() < 0.97:
            alarm = True
    elif burglar:
        if random.random() < 0.92:
            alarm = True
    elif earthquake:
        if random.random() < 0.81:
            alarm = True
    if not burglar and not earthquake and random.random() < 0.0095:
        alarm = True
    return (earthquake, burglar, alarm)

i = 0
positiiviset = 0
kohta1total = 0
kohta1Bis1 = 0
kohta2total = 0
kohta2Bis1 = 0
while i < 100000:
    i+=1
    testattava = arvo()
    if testattava[2]:
        kohta1total += 1
        if testattava[1]:
            kohta1Bis1 += 1
    if testattava[2] and testattava[0]:
        kohta2total += 1
        if testattava[1]:
            kohta2Bis1 += 1

print(f"Kohtaan 1: {kohta1Bis1 / kohta1total}")
print(f"Kohtaan 2: {kohta2Bis1 / kohta2total}")