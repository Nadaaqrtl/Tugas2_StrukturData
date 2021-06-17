class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self.acnt = acnt
        self.customer = customer
        self.bank = bank
        self.limit = limit
        self.balance = balance

    def is_numeric(self, value):
        return type(value)==type(1) or type(1.0)


    def charge(self, price):
        if not self.is_numeric(price):
            raise TypeError("price must be int or float")

        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True

    def make_payment(self, amount):
        if not self.is_numeric(amount):
            raise TypeError("amount must be int or float")
        if amount<0 :
            raise ValueError("amount cant be negative")
        self.balance -= amount



card = CreditCard('Nadaa', 'BBRRII', 'E1E119034', 200,100)
print(card.__dict__)
card.charge(100)
print(card.__dict__)
card.make_payment(50)
print(card .__dict__)
