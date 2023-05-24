from pojistenec import Pojisteny
from pojistenec import Evidence

def main():
    evidence = Evidence()
    prvni_opakovani = True

    while True:
        print("Menu:")
        print("1. Vytvořit pojištěnce")
        print("2. Zobrazit seznam pojištěných")
        print("3. Vyhledat pojišteného")
        print("4. Konec\n")

        if prvni_opakovani:
            volba = input("Zadejte volbu [1-4]: ")
            prvni_opakovani = False
        else:
            volba = input("Pokračujte libovolnou klávesou nebo zadejte volbu [1-4]: ")

        if volba == "1":
            jmeno = input("\nJméno: ")
            prijmeni = input("Příjmení: ")
            vek = int(input("Věk: "))
            telefon = input("Telefonní číslo: ")
            pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            evidence.pridej_pojisteneho(pojisteny)
            print("Pojištěný byl úspěšně vytvořen.\n")

        elif volba == "2":
            if len(evidence.pojisteni) > 0:
                print("Seznam pojištěných:\n")
                evidence.zobraz_seznam()
            else:
                print("V seznamu pojištěných nikoho neeviduji.\n")

        elif volba == "3":
            jmeno = input("Jmeno: ")
            prijmeni = input("Příjmení: ")
            pojisteny = evidence.najdi_pojisteneho(jmeno, prijmeni)
            if pojisteny:
                print("Nalezený pojištěnec:\n")
                print(pojisteny)
            else:
                print("Pojištěnec nebyl nalezen.\n")

        elif volba == "4":
            break

        else:
            print("Neplatná volba. Zadejte prosím znovu.\n")


if __name__ == "__main__":
    main()





