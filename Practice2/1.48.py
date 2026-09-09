from itertools import *

alph = '123456'
a = list(product(alph, repeat=3))
cnt = 0

# a)
for el in a:
    summ = 0
    for i in el:
        summ += int(i)
    if summ == 11:
        cnt += 1

p = cnt/6**3

# б)
cnt = 0
for el in a:
    summ = 0
    for i in el:
        summ += int(i)
    if summ >= 11:
        cnt += 1

p = cnt/6**3
