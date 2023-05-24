class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, vek: {self.vek}, telefon: {self.telefon}"

class Evidence:
    def __init__(self):
        self.pojisteni = []

    def zobraz_seznam(self):
        for pojisteny in self.pojisteni:
            print(pojisteny)

    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None
