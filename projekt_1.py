"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Iveta Minaříková
email: pilatovaiveta@gmail.com
discord: Iveta M.
"""
from texty import TEXTS
registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

while True:
    jmeno = input ("Zadejte přihlašovací jméno:")
    if jmeno in registrovani_uzivatele:
        while True:  
            heslo = input ("Zadejte heslo:")
            if registrovani_uzivatele[jmeno] == heslo:
                print("-" * 40)
                print(f"Vítej, uživateli {jmeno}! K analýze je možné vybrat ze tří textů v nabídce.")
                print("-" * 40)
                while True:
                    cislo_textu = input ("Ke zvolení textu zadejte číslici od 1 do 3: ")
                    if cislo_textu.isdigit():
                        cislo_textu = int(cislo_textu)
                        if cislo_textu in [1, 2, 3]:
                            print("-" * 40)
                            print("Ve zvoleném textu je:")
                            zvoleny_text = TEXTS[cislo_textu - 1]
                            
                            slova = zvoleny_text.split()
                            pocet_slov = len(slova)
                            print(f"{pocet_slov} slov.")

                            velke_pocatecni_pismeno = 0
                            slova_velka_pismena = 0
                            slova_mala_pismena = 0
                            pocet_cisel = 0
                            suma_vsech_cisel = 0

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
                            
                            print(f"{velke_pocatecni_pismeno} slov začínajících velkým písmenem.")
                            print(f"{slova_velka_pismena} slov psaných velkými písmeny.")
                            print(f"{slova_mala_pismena} slov psaných malými písmeny.")
                            print(f"{pocet_cisel} čísla.")
                            print(f"Suma všech čísel je {suma_vsech_cisel}.")
                            print("-" * 40)

                            print(f"{'DÉLKA':<5}|{'ČETNOST':^15}|ČÍSLICE")
                            print("-" * 40)
                            
                            cetnosti_delek_slov = {}
                            for slovo in slova:
                                slovo = slovo.rstrip('.,')
                                delka = len(slovo)
                                if delka in cetnosti_delek_slov:
                                   cetnosti_delek_slov[delka] += 1
                                else:
                                   cetnosti_delek_slov[delka] = 1
                            for delka, cetnost in sorted(cetnosti_delek_slov.items()):
                                print(f"{delka:<5}|{'*' * cetnost:<15}|{cetnost}")
                            break     
                        else:
                            print("Zadané číslo není v nabídce.")
                            break
                    else:
                        print("Zadána neplatná hodnota.")
                        break
                break
            else:
                print("Zadali jste špatné heslo, zkuste to znovu.")
                continue
        break
    else:
        print("Uživatel není registrován.")
        break
