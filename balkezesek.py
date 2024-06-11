class Bal:
    def __init__(self,sor):
        #sor="Mitch Williams;1986-04-09;1997-05-10;180;75"
        adatok=sor.strip().split(";")
        #adatok[0]="Mitch Williams"  adatok[1]="1986-04-09" ..... adatok[4]="75"
        self.nev=adatok[0]
        self.elsop=adatok[1]
        self.utolsop=adatok[2]
        self.suly=int(adatok[3])
        self.magassag=int(adatok[4])

#példanyomtatás
balkezesek:list[Bal]=[]
#file megnyitása r-olvasás, w-írás

file=open("balkezesek.csv","r")
elsoSor=file.readline().strip()
for sor in file:
    balkezesek.append(Bal(sor))
file.close()

#print(*balkezesek,sep="\n")
#print(balkezesek[0].nev)

print(f"3. feladat: {len(balkezesek)}")

print("4. feladat")
for i in balkezesek:
    if "1999-10" in i.utolsop:
        print(f"\t{i.nev}, {i.magassag*2.54:.1f} cm")

print("5. feladat")
be_esz=int(input("Kérek egy 1990 és 1999 közötti évszámot: "))
while be_esz < 1990 or be_esz > 1999:
    be_esz = int(input("Hibás adat! Kérek egy 1990 és 1999 közötti évszámot: "))

print("6. feladat", end="")
osszsuly = 0
osszdb = 0
for i in balkezesek:
    if int(i.elsop[0:4]) <= be_esz and int(i.utolsop[0:4]) >= be_esz:
        osszsuly += i.suly
        osszdb += 1

print(f"{osszsuly/osszdb:.2f} font")