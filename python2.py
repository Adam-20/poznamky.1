#ukol1
print("napis svoje jmeno")
jmeno = inpup()

print("napis svuj vek")
vek = int(input())

print(f"ahoj jmenuji se {jmeno} a je mi {vek}")

#ukol2
print("napis desetine cislo")
cislo1 = int(input())
print("napis znamenko")
zanmenko = input()
print("napis druhe desetine cislo")
cislo2 = int(input())

soucet = (cislo1 + cislo2)
rozdil = (cislo1 - cislo2)
soucin = (cislo1 * cislo2)
podil = (cislo1 / cislo2)

vysledek = soucet or rozdil or soucin or podil
print(vysledek)


