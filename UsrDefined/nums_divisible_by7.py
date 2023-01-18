answer = list(filter((lambda x: x%7 == 0), filter((lambda x: x%5 != 0), range(2000, 3200))))
print(answer)