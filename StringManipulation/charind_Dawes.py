'''
Created on 3/20/22
@author:   Kobe Dawes
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. Kobe Dawes 

SSW-215 String Manipulation
'''


with open(r'/Users/kobe/Desktop/Academics/SSW215/Assignments/StringManipulation/fruits.txt') as string:
    string = string.read().strip('""')

def indexHelp(letter, string, count):
    """helper function that keeps track of the index while checking if the first 
    index of each string is the same as the character, and returns the list of all indexes in which that is true """
    if string == '':
        return []
    if letter == '':
        return []
    elif letter != string[0]:
        return indexHelp(letter, string[1:], count + 1)
    else:
        return [count] + indexHelp(letter, string[1:], count + 1)

def char_index(ch, str):
    """checks whether the indicated character is in the string and returns the list of the indexes that are """
    if str == '':
        return []
    if ch == '':
        return []
    else: 
        return f"This index values of each occurrence of character '{ch}' in the string are {indexHelp(ch, str, 0)}"
print(char_index('r', string))

def vc_helper(str, vowelnum, consonants):
    """helper function that checks whether the string has vowels are returns the number of vowels, 
    and consonants"""
    vowels = 'aeiou'
    
    if str == '':
        return f'The amount of vowels are {vowelnum} and the amount of consonants are {consonants}'
    elif str[0].lower() in vowels:
        return vc_helper(str[1:], vowelnum + 1, consonants)
    else:
        return vc_helper(str[1:], vowelnum, consonants + 1)
        
def vc_counter(str):
    """takes in a string eliminates the whitespace within it, and uses a helper 
    function to count the amount of vowels and consonants"""
    str = "".join(string.split())
    if str == '':
        return 0
    else:
        return vc_helper(str, 0, 0)
print(vc_counter(string))


def vowel_helper(str, a, e, i, o, u):
    """function that checks whether the string is a specific vowel and increments the vowels accordingly"""
    if str == '':
        return f'A-{a}, E-{e}, I-{i}, O-{o}, U-{u}'

    elif str[0].lower() == 'a':
        return vowel_helper(str[1:], a + 1, e, i, o, u)

    elif str[0].lower() == 'e':
        return vowel_helper(str[1:], a , e + 1, i, o, u)

    elif str[0].lower() == 'i':
        return vowel_helper(str[1:], a , e, i + 1, o, u)

    elif str[0].lower() == 'o':
        return vowel_helper(str[1:], a , e , i, o + 1, u)

    elif str[0].lower == 'u': 
        return vowel_helper(str[1:], a , e , i, o , u + 1)

    else:
        return vowel_helper(str[1:], a , e , i, o , u)

def vowel(str):
    """function that checks whether the string is a specific vowel and increments the vowels accordingly"""
    nstr = "".join(string.split())
    if nstr == '':
        return 0
    else:
        return vowel_helper(nstr, 0, 0, 0, 0, 0)
print(vowel(string))

def alternate(str):
    """takes in a string and outputs a string where if a character is 
    uppercase it will be changed to lowercase, and vice-versa"""
    if str == '':
        return ''
    return alternate2(str[0], '') + alternate(str[1:])

def alternate2(str, word):
    """takes in a string and outputs a string where if a character is 
    uppercase it will be changed to lowercase, and vice-versa"""
    if str == '':
        return ''

    elif str[0].islower() is True:  
        
        return  word + str[0].upper() + alternate2(str[1:], word)
    else:
        
        return word + str[0].lower() + alternate2(str[1:], word)
print(alternate(string)) 



