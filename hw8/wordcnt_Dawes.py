'''
Created on 3/24/22
@author:   Kobe Dawes
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. Kobe Dawes 

SSW-215 Word Count
'''


with open(r'/Users/kobe/Desktop/Academics/SSW215/Assignments/hw8/alice.txt') as string:
    string = string.readlines()

count = 0
def word_count(string):
    """takes in a string/file, splits it to create a list 
    analyses it by line and adds every item in the list"""
    global count
    for line in string:
        list = line.split()
        count += len(list)
        
    return count    

print(word_count(string))
