import sys


with open('bakery.csv', 'a', encoding='utf-8') as f:
    if len(sys.argv) == 2:
        price = sys.argv[-1]
        f.write(price + '\n')
