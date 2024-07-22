"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Iveta Minaříková
email: pilatovaiveta@gmail.com
discord: ivet_13 (Iveta M.)
"""
from texty import TEXTS
registrovani_uzivatele ={
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

jmeno = input("Zadejte přihlašovací jméno: ")

if jmeno in registrovani_uzivatele:
    for pokus in range(3):
        heslo = input("Zadejte heslo: ")
        if registrovani_uzivatele[jmeno] == heslo:
            print("-" * 40)
            print(f"Vítej uživateli {jmeno}! K analýze je možné vybrat ze tří textů v nabídce.")
            print("-" * 40)
            break
        else:
            print(f"Špatné heslo, pokus {pokus + 1} z 3.")
    else:
        print("Třikrát jste zadali špatné heslo. Ukončuji program.")
        exit()
else:
    print("Uživatel neexistuje, ukončuji program.")
    exit()   
    
cislo_textu = input("Ke zvolení textu zadejte číslici od 1 do 3: ")

if cislo_textu.isdigit():
        cislo_textu = int(cislo_textu)
        if cislo_textu in list(range(1, len(TEXTS) + 1)):
            print("-" * 40)
            print("Ve zvoleném textu je:")
        else:
            print("Zadané číslo není v nabídce, ukončuji program.")
            exit()
else:
    print("Zadána neplatná hodnota, ukončuji program.")
    exit()  

zvoleny_text = TEXTS[cislo_textu - 1]
slova = zvoleny_text.split()

pocet_slov = len(slova)
velke_pocatecni_pismeno = 0
slova_velka_pismena = 0
slova_mala_pismena = 0
pocet_cisel = 0
suma_vsech_cisel = 0
cetnosti_delek_slov = {}

for slovo in slova:
    if slovo.istitle():
        velke_pocatecni_pismeno += 1
    elif slovo.isupper() and slovo.isalpha():
        slova_velka_pismena += 1
    elif slovo.islower():
        slova_mala_pismena += 1
    elif slovo.isdigit():
        pocet_cisel += 1
        suma_vsech_cisel += int(slovo)

    ocistene_slovo = slovo.rstrip('.,')
    delka = len(ocistene_slovo)

    cetnosti_delek_slov[delka] = cetnosti_delek_slov.setdefault(delka, 0) + 1
                                
print(f"{pocet_slov} slov.")
print(f"{velke_pocatecni_pismeno} slov začínajících velkým písmenem.")
print(f"{slova_velka_pismena} slov psaných velkými písmeny.")
print(f"{slova_mala_pismena} slov psaných malými písmeny.")
print(f"{pocet_cisel} čísla.")
print(f"Suma všech čísel je {suma_vsech_cisel}.")
print("-" * 40)

print(f"{'DÉLKA':<5}|{'ČETNOST':^18}|ČÍSLICE")
print("-" * 40)

for delka, cetnost in sorted(cetnosti_delek_slov.items()):
    print(f"{delka:<5}|{'*' * cetnost:<18}|{cetnost}")