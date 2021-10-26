class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name , "$",self.account_balance)
        return self

    def transfer(self, amount, other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(self.account_balance)
        print(other_user.account_balance)
        return self

Will = User("Will Dwelle", "ww@coolguy.com")
Gianna = User("Gianna Dwelle", "GW@selfcare.org")
Dad = User("Denzil Dwelle", "dd@blah.com")

Will.make_deposit(200).make_deposit(500).make_deposit(5).make_withdrawl(700).display_user_balance()

Gianna.make_deposit(600).make_deposit(60).make_withdrawl(500).make_withdrawl(5).display_user_balance()

Dad.make_deposit(10000).make_withdrawl(50).make_withdrawl(2500).make_withdrawl(600).display_user_balance().transfer(200, Will)