import scipy.special as sc

n = 10
k = 5

# а)
a = n**k
# б)
a = sc.comb(n+k-1, k)
