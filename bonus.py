salary=float(input("Mbeca:"))
years=int(input("Miaka:"))
if years>10:
    bonus=10/100*salary
    print(bonus)
if years>=6 and years<=10:
    bonus=8/100*salary
    print(bonus)
    if years<6:
        bonus=5/100*salary
        print(bonus)