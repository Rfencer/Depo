import sys


with open('bakery.csv', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        for line in f:
            print(line)
    elif len(sys.argv) == 2:
        for index, line in enumerate(f, 1):
            if index >= int(sys.argv[-1]):
                print(line)
    else:
        for index, line in enumerate(f, 1):
            if int(sys.argv[1]) <= index <= int(sys.argv[2]):
                print(line)
