import itertools as it

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А',
]

gen_school = (x for x in it.zip_longest(tutors,klasses))

for _ in range(max(len(tutors), len(klasses))+1):
    print(next(gen_school))


