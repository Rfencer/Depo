

def odd_nums(count):
    for i in range(1, count+1, 2):
        yield i


odd_to_15 = odd_nums(15)

for _ in range(10):
    print(next(odd_to_15))


