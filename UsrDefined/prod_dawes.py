def prod_len_name(firstName, lastName):
    result = len(str(firstName)) * len(str(lastName))
    return f"The product of the value of the lengths of my firstname and lastname is {result}."

print(prod_len_name('kobe', 'dawes'))

