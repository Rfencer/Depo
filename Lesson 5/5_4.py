src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_result = []

count = 0
prev = 0
for i in src:
    if count > 0 and i > prev:
        list_result.append(i)
        prev = i
        count += 1
    else:
        prev = i
        count += 1


print(list_result)







