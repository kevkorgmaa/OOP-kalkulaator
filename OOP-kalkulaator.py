# Põhiklass User (kasutaja)
class User():

    # Konstruktor – käivitatakse objekti loomisel
    def __init__(self, name, age, gender):
        self.name = name  # Kasutaja nimi
        self.age = age  # Kasutaja vanus
        self.gender = gender  # Kasutaja sugu

    # Meetod kasutaja andmete kuvamiseks
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)


# Alamklass Bank, mis pärib User klassi omadused
class Bank(User):

    # Konstruktor – lisaks kasutaja andmetele luuakse ka konto saldo
    def __init__(self, name, age, gender):
        # Kutsutakse välja User klassi konstruktor
        super().__init__(name, age, gender)
        self.balance = 0  # Konto algsaldo

    # Raha sissemakse meetod
    def deposit(self, amount):
        self.amount = amount  # Sissemakse summa
        self.balance = self.balance + amount  # Saldo uuendamine
        print("Account balance has been updated : €", self.balance)

    # Raha väljavõtmise meetod
    def withdraw(self, amount):
        self.amount = amount  # Väljavõetav summa

        # Kontrollitakse, kas kontol on piisavalt raha
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : €", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : €", self.balance)

    # Meetod kontoinfo ja saldo kuvamiseks
    def view_balance(self):
        self.show_details()  # Kuvab kasutaja isikuandmed
        print("Account balance: €", self.balance)

    def transfer(self, amount, target_account):
        # target_account peab olema samuti Bank tüüpi objekt
        if amount > self.balance:
            print(f"Transfer failed! Not enough funds. Your balance: €{self.balance}")
        else:
            # Vähendame saatja saldot
            self.balance -= amount
            # Suurendame saaja saldot
            target_account.balance += amount

            print(f"Transfer successful!")
            print(f"You sent €{amount} to {target_account.name}.")
            print(f"Your new balance: €{self.balance}")
