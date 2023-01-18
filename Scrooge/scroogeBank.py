Huey = {
    "name": "Huey",
    "amount": 150,
    "accNumber": "700007"
}

Dewey = {
    "name": "Dewey",
    "amount": 350,
    "accNumber": "800008"
}

Louie = {
    "name": "Louie",
    "amount": 25,
    "accNumber": "900009"
}

Scrooge = {
    "name": "Scrooge",
    "amount": 1000000,
    "accNumber": "100001"
}

nephews = ["Huey", "Louie", "Dewey"]
class Bank:
    
    def __init__(self, name, accNumber, withAmount):
        ''' instantizes the name account Number and withdrawl 
        amount to be used throughout the class'''
        self.name = name
        self.withAmount = withAmount
        self.account = accNumber

    def withdraw(self):
        ''' This portion of the code takes the instantized withdrawl amount 
        and checks whether it is over 10% of the total amount, 
        and provides a $5 penalty if it is. Also ensures that the funds for the 
        other nephews are properly applied and withdrawn from scrooge's account'''
        dNephews = [Huey, Louie, Dewey]
        dNephews.remove(self.name)

        if self.account != self.name['accNumber']:
            return "Your account number is incorrect"

        if self.withAmount > .1*(self.name["amount"]): # the penalty portion of the code
            Scrooge['amount'] -= 5
        
        else: 
    
            self.name['amount'] -= self.withAmount # if the withdraw goes through
            for nephew in dNephews:
                nephew['amount'] += self.withAmount
                Scrooge['amount'] -= self.withAmount
                
        outList = [[Scrooge['name'], Scrooge['amount']],
                        [Huey['name'], Huey['amount']],
                        [Dewey['name'], Dewey['amount']],
                        [Louie['name'], Louie['amount']]
                        ]    
        return outList

    def _str_(self):
        '''prints the string of the withdraw result'''
        return f'{self.withdraw()}'

    def __repr__(self):
        '''references the withdraw result'''
        return f'{self.withdraw()}'

First = Bank(Louie, '900009', 2)
Second = Bank(Dewey, '800008', 20)
Third = Bank(Huey, '700007', 20)
Fourth = Bank(Louie, '900009', 10)
Fifth = Bank(Dewey, '800008', 20)
Sixth = Bank(Huey, '700007', 30)
Seventh = Bank(Louie, '900009', 40)
print(First)
print(Second)
print(Third)
print(Fourth)
print(Fifth)
print(Sixth)
print(Seventh)