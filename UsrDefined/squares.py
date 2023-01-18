def squares(n):
    return list(map((lambda x: x**2), filter((lambda x: x**2 < n), range(0, n))))

print(squares(10))