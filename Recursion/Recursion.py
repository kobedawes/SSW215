############################################################
# Name:Kobe Dawes
# Pledge:I pledge my honor that I have abided by the Stevens honor system. Kobe Dawes
# ssw215 hw12
############################################################

memo = {}
memo2 = {}


def middle(n):
    """helper function that takes in a list and
     outputs a list that is the sum of the first two numbers"""
    if n == []:
        return []
    if n == [1]:
        return []

    elif len(n) == 1:
        return []
    
    else:
        return [n[0] + n[1]] + middle(n[1:]) 


def pascal_row(n):
    """takesn an integer as an innput and creates that specific row as a list"""
    if n in memo:
        return memo[n]

    if n < 0:
        return 'invalid input'
    
    elif n == 0:
        memo[n] = [1]
        return [1]
    else:
        term = middle(pascal_row(n-1))
        memo[n] = [1] + term + [1]
        return [1] +term + [1] 


def pascal_triangle(n):
    """prints the list of pascal's triangle in ascedning order"""
    if n in memo2:
        return memo2[n]
    if n == []:
        return []
    if n == 0:
        memo2[n] = [[1]]
        return [[1]]
    
    if n < 0:
        return 'invalid input'
    
    else:
        triangle = pascal_triangle(n-1)
        row = [pascal_row(n)]
        memo2[n] = triangle + row
        return  triangle + row


print(pascal_triangle(5))