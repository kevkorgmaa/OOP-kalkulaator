import math

class Calculator:
    """Lihtne kalkulaator klass OOP põhimõtetel."""

    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    # ----- Põhifunktsioonid -----

    def liitmine(self):
        return self.a + self.b

    def lahutamine(self):
        return self.a - self.b

    def korrutamine(self):
        return self.a * self.b

    def jagamine(self):
        if self.b == 0:
            return "Viga: nulliga jagamine!"
        return self.a / self.b

    def astendamine(self):
        return self.a ** self.b

    def ruutjuur(self):
        if self.a < 0:
            return "Viga: negatiivi ruutjuurt ei saa võtta!"
        return math.sqrt(self.a)

    # ----- Lisafunktsioonid (hinne 5 jaoks) -----

    def protsent(self):
        return (self.a * self.b) / 100

    def absoluut(self):
        return abs(self.a)

    def keskmine(self):
        return (self.a + self.b) / 2


# ----- Programm -----
def menu():
    print("""
--- KALKULAATOR ---
1. Liita
2. Lahutada
3. Korrutada
4. Jagada
5. Astendada
6. Ruutjuur
7. Protsent (%)
8. Absoluutväärtus
9. Keskmine
0. Välju
""")


while True:
    menu()
    valik = input("Vali toiming: ")

    if valik == "0":
        print("Programm lõpetatud.")
        break

    # Üks sisend ruutjuure ja absoluutväärtuse jaoks
    if valik in ["6", "8"]:
        a = float(input("Sisesta arv: "))
        calc = Calculator(a)

    # Kaks sisendit muudele toimingutele
    else:
        a = float(input("Sisesta esimene arv: "))
        b = float(input("Sisesta teine arv: "))
        calc = Calculator(a, b)

    # Toimingute töötlemine
    if valik == "1":
        print("Vastus:", calc.liitmine())
    elif valik == "2":
        print("Vastus:", calc.lahutamine())
    elif valik == "3":
        print("Vastus:", calc.korrutamine())
    elif valik == "4":
        print("Vastus:", calc.jagamine())
    elif valik == "5":
        print("Vastus:", calc.astendamine())
    elif valik == "6":
        print("Vastus:", calc.ruutjuur())
    elif valik == "7":
        print("Vastus:", calc.protsent())
    elif valik == "8":
        print("Vastus:", calc.absoluut())
    elif valik == "9":
        print("Vastus:", calc.keskmine())
    else:
        print("Vigane valik!")
