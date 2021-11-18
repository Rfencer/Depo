
count = 15
odd_to_15 = (x for x in range(1, count + 1, 2))

for _ in range(10):
    print(next(odd_to_15))


