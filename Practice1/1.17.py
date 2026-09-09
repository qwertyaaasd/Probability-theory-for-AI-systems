import scipy.special as sc

# а)
a = sc.comb(9, 2)*sc.comb(4, 4)*sc.comb(4, 3)*2/sc.comb(36, 7)

# б)
a = sc.comb(9, 7)*4**7/sc.comb(36, 7)

# в)
a = sc.comb(9, 3)* \
    (6*sc.comb(4, 4)*sc.comb(4, 2)*sc.comb(4, 1) + \
     3*sc.comb(4, 3)*sc.comb(4, 3)*sc.comb(4, 1) + \
     3*sc.comb(4, 2)*sc.comb(4, 2)*sc.comb(4, 3)) / \
     sc.comb(36, 7)
