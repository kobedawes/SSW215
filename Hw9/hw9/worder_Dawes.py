import array


def word_order(string):
    list2 = list(set(string.split()))
    return sorted(list2)

print(word_order('apple, mango, carrot, apple, orange, mango, berry'))