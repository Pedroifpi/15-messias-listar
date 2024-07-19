popA=5000000
natA=3
popB=7000000
natB=2

anos=0

while popA<=popB:
    popA+=popA*natA/100
    popB+=popB*natB/100
    anos+=1
print("pais A ultrapassara o pais B em",anos,"anos.")  