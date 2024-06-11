def beker(uzenet, min, max):
    valasz = int(input(f"{uzenet}: "))
    while valasz < min or valasz > max:
        print(f"{min} és {max} közötti értéket adjon meg: ")
        valasz = int(input(f"{uzenet}: "))
    return valasz

ora = beker("Kérem adja meg az órát",0,23)
perc = beker("Kérem adja meg a percet"0,59)
ido = ora * 60 + perc

aktido = current[0] * 60 + current[1]

if aktido > ido:
    print("A vizsa már véget ért!")
else:
    print(f"A vizsa hátralévő ideje: {aktido-ido} perc.")