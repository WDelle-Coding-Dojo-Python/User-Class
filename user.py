class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name , "$",self.account_balance)

    def transfer(self, amount, other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(self.account_balance)
        print(other_user.account_balance)

Will = User("Will Dwelle", "ww@coolguy.com")
Gianna = User("Gianna Dwelle", "GW@selfcare.org")
Dad = User("Denzil Dwelle", "dd@blah.com")

Will.make_deposit(200)
Will.make_deposit(500)
Will.make_deposit(5)
Will.make_withdrawl(700)
#Will.display_user_balance()

Gianna.make_deposit(600)
Gianna.make_deposit(60)
Gianna.make_withdrawl(500)
Gianna.make_withdrawl(5)
#Gianna.display_user_balance()

Dad.make_deposit(10000)
Dad.make_withdrawl(50)
Dad.make_withdrawl(2500)
Dad.make_withdrawl(600)
#Dad.display_user_balance()

Dad.transfer(200, Will)