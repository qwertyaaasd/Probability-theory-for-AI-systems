import scipy.special as sc

m = 25
n = 365
inv_a = sc.perm(n, m)/n**m
print(round(inv_a, 5))
a = 1 - inv_a
