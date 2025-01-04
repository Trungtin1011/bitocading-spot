#############################
# Coin state:               #
#     Value = 1 (Cent)     #
#     Color = "Gold"        #
#     Number of edges 1     #
#     Diameter = 22 (mm)    #
#     Thickness = 2 (mm)    #
#     Heads = True          #
#############################
import random


class Coin:
    # Constructor
    def __init__(self, rare=False, clean=True, head=True, **kwargs):
        # Set value for each data in coin from kwargs
        for key, val in kwargs.items():
            setattr(self, key, val)
        self.is_rare: bool = rare
        self.is_clean: bool = clean
        self.is_head: bool = head

        if self.is_rare:
            self.value = self.origin_value * 1.5
        else:
            self.value = self.origin_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def print_coin(self):
        print("-----")
        print(
            f"{self.value} Cent - Color: {self.color}, Value: {self.value}, Diameter (mm): {self.diameter}, Thickness (mm): {self.thickness}, Edges: {self.edges}, Mass: {self.mass}"
        )

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def flip(self):
        head_options: list = [True, False]
        choice = random.choice(head_options)
        self.heads = choice

    # def __str__(self):
    #     return f"{int(self.origin_value)} Cent"

    # Destructor
    def __del__(self):
        print("Coin Spent!")


class Cent(Coin):
    def __init__(self):
        data = {
            "origin_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "edges": 1,
            "diameter": 22.00,
            "thickness": 2.00,
            "mass": 9.50,
            # "head": True
        }
        super().__init__(**data)


class ten_cent(Coin):
    def __init__(self):
        data = {
            "origin_value": 10.00,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56,
            # "head": True
        }
        super().__init__(**data)


class twenty_cent(Coin):
    def __init__(self):
        data = {
            "origin_value": 20.00,
            "clean_color": "silver",
            "rusty_color": None,
            "edges": 1,
            "diameter": 22.3,
            "thickness": 1.63,
            "mass": 4.52,
            # "head": True
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean(self):
        self.color = self.clean_color


class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account : Balance £{}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance)


coins: list = [ten_cent(), twenty_cent()]
for coin in coins:
    coin.print_coin()
