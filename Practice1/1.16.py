import scipy.special as sc

# а)
a = round(2/(sc.factorial(10)/(sc.factorial(5)*sc.factorial(5))), 5)

# б)
a = round(sc.factorial(5)*2**5/sc.factorial(10), 5)
