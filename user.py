class User:		
    def __init__(self):
        self.name = "mohannad"
        self.email = "mohannadadeeb89@gmail.com"
        self.account_balance = 1000
        
    def make_deposite(self, amount):
        self.account_balance+=amount
    def with_drawal(self,amount):
        self.account_balance-=amount
    

dr=User()
dr.make_deposite(100)
dr.make_deposite(25)
dr.make_deposite(200)
dr.with_drawal(500)
te=User()
te.make_deposite(25)
te.make_deposite(200)
te.with_drawal(500)
te.with_drawal(300)

re=User()
re.make_deposite(1000)
re.with_drawal(500)
re.with_drawal(300)
re.with_drawal(300)

print("first instance =",te.account_balance)
print("2nd instance =",re.account_balance)

print("3rd instance =",dr.account_balance)