
def helperFunc(string, count, word):
    if string == '':
        return word
    elif count % 2 == 0:
        return helperFunc(string[1:], count + 1, word)
    else:
        word += string[0]
        return helperFunc(string[1:], count + 1, word)

def evenFunc(string):
    return helperFunc(string[1:], 1, string[0])

print(evenFunc('Individual software engineering'))

with open(r'/Users/kobe/Desktop/Academics/SSW215/Assignments/hw9/alice.txt') as string:
    stringList = string.readlines()


def count(word, list, counter):
    for item in list:
        box = item.split()
        for string in box:
            if string == word:
                counter += 1
    return counter

def findOver5(stack):
    output = []
    for item in stack:
        list = item.split()
        for string in list:
            if len(string) > 5:
                output += [(string, count(string, stack, 0))] 
    return output
#print(findOver5(stringList))
