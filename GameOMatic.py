
import random 

list = []
list2 = []
i = 1
n = 1

diceRolls = {'1': 0, '2': 0, '3':0, '4':0, '5': 0, '6': 0, '7':0, 
'8':0, '9': 0, '10': 0, '11':0, '12':0
}
diceRolls2 = {'1': 0, '2': 0, '3':0, '4':0, '5': 0, '6': 0, '7':0, 
'8':0, '9': 0, '10': 0, '11':0, '12':0
}

while i <= 10000:
    list.append(random.randrange(1, 13))
    i +=1

for roll in diceRolls.keys():
    for num in list:
        if str(num) == roll:
            diceRolls[roll] += 1
for roll in diceRolls.keys():
    diceRolls[roll] /= i

while n <= 10000:
    list2.append(random.randint(1, 12))
    n +=1

for roll in diceRolls2.keys():
    for num in list2:
        if str(num) == roll:
            diceRolls2[roll] += 1

for roll in diceRolls2.keys():
    diceRolls2[roll] /= n

print(diceRolls)
print(f'Probability with random.range() is : {sum(diceRolls.values())/12}')
print(diceRolls2)
print(f'Probability with random.range() is : {sum(diceRolls2.values())/12}')
#10000/12 = 833.33

characters = [ {'name':'Gandolf','food': 5, 'grapefruit': 10, 'green potions': 7, 'red potions': 8, 'spells of enchantment': 10},
{'name':'Frodo', 'food': 0, 'kiwi': 5, 'wands of confusion': 7, 'green potions':8},
{'name':'Sauron', 'bat wings': 5, 'evil spells': 10,'fire wands': 5}
]

class AddCount:
    def __init__(self, name, item, oper, val):
        self.name = str(name)
        self.item = str(item)
        self.oper = str(oper)
        self.val = int(val)

    def operCount(self):
        n= 0
        if self.oper == '+':
            while n < len(characters):
                if characters[n]['name'] == self.name:
                    if self.item in characters[n]:
                        characters[n][self.item] += abs(self.val)
                        return characters[n]
                n +=1


        elif self.oper == '-':
           while n < len(characters):
                if characters[n]['name'] == self.name:
                    if self.item in characters[n]:
                        characters[n][self.item] -= abs(self.val)
                    

                        if characters[n][self.item] <= 0:
                            characters[n][self.item] = 0
                            print(f'{self.item} store is empty')
                    return characters[n]
                n += 1
        else:
            print('invalid input')

    def _str_(self):
        '''prints the string of the withdraw result'''
        return f'{self.operCount()}'

    def __repr__(self):
        '''references the withdraw result'''
        return f'{self.operCount()}'
class AddItem:
   
    def __init__(self, name, item, oper, count):
        self.name = str(name)
        self.item = str(item)
        self.oper = str(oper)
        self.count = int(count)

    def operItem(self):
        n= 0
        if self.oper == '+':
            while n < len(characters):
                if characters[n]['name'] == self.name:
                    characters[n][self.item] += self.count
                    characters[n].update({self.item: characters[n][self.item]})
                    return characters[n]
                n +=1


        elif self.oper == '-':
           while n < len(characters):
                if characters[n]['name'] == self.name:
                    characters[n][self.item] += self.count
                    characters[n].update({self.item: characters[n][self.item]})                    

                    if characters[n][self.item] <= 0:
                        characters[n][self.item] = 0
                        print(f'{self.item} store is empty')
                    return characters[n]
                n += 1
        else:
            print('invalid input')

    def _str_(self):
        '''prints the string of the withdraw result'''
        return f'{self.operItem()}'

    def __repr__(self):
        '''references the withdraw result'''
        return f'{self.operItem()}'
class NewItem:
    def __init__(self, name, item, count):
        self.name = str(name)
        self.item = str(item)
        self.count = int(count)

    def NewItem(self):
        n = 0
        while n < len(characters):
            if characters[n]['name'] == self.name:
                characters[n].update({self.item: self.count})
                return characters[n]
            n += 1
    def _str_(self):
        '''prints the string of the withdraw result'''
        return f'{self.NewItem()}'

    def __repr__(self):
        '''references the withdraw result'''
        return f'{self.NewItem()}'

class AddCharacter:
    def __init__(self, name, items):
        self.name = str(name)
        self.items = items

    def Add(self):
        characters.append({self.name: self.items})
        return characters

    def _str_(self):
        '''prints the string of the withdraw result'''
        return f'{self.Add()}'

    def __repr__(self):
        '''references the withdraw result'''
        return f'{self.Add()}'

increment = AddCount('Sauron', 'bat wings', '+', 5)
additem = AddItem('Sauron', 'bat wings', '+', 5)
newitem = NewItem('Sauron', 'rings of power', 5)
addchar = AddCharacter('Bilbo', {'name':'Bilbo', 'food': 0, 'kiwi': 5, 'wands of confusion': 7, 'green potions':8})
print(increment)
print(additem)
print(newitem)
print(addchar)
