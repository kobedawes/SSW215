def max_name_len(firstName, lastName):
    result = max(len(str(firstName)), len(str(lastName)))
    return f"The largest value of the length of my firstname and lastname is {result}"

print(max_name_len('kobe', 'dawes'))