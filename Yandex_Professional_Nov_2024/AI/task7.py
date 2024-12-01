m, n = map(int, input().split(','))
X = list()
for i in range(m):
    x = list(map(int, input().split(',')))
    X.append(x.copy())

h, w = map(int, input().split(','))
A = []
padding_width_arr = [0]*((w - 1) // 2)
padding_height_arr = [0]*(n + w - 1)
pw = len(padding_width_arr)
ph = len(padding_height_arr)
for i in range(-(h - 1) // 2, h + (h - 1) // 2):
    if -1 < i < h:
        x = padding_width_arr.copy() + X[i].copy() + padding_width_arr.copy()
    else:
        x = padding_height_arr.copy()
    A.append(x.copy())

C = []
for i in range(m):
    x = list(map(int, input().split(',')))
    C.append(x)

AA = []
CC = []
for i in range(h):
    for j in range(w):
        CC.append(C[i][j])
        x = []
        for ii in range(h):
            for jj in range(w):
                a_i = i + ii
                a_j = j + jj
                x.append(A[a_i][a_j])
                print(A[a_i][a_j], end=' ')
        AA.append(x.copy())
        print()


import numpy as np
AA = np.array(AA)
CC = np.array(CC)
BB = np.linalg.solve(AA, CC)
print(BB, AA @ BB)

letters = "abcdefghij"
for i in range(9):
    s = ""
    for j in range(9):
        s += f"{AA[i][j]}{letters[j]} + "
    s += f"{CC[i]}"
    print(s)

"""Does not work!!!"""


"""Test samples
3,5
9,0,46,57,49
19,23,41,23,88
47,71,92,8,86
3,3
256,1096,1586,2501,1300
1135,1014,1028,2221,1341
1465,2149,1830,936,1860


6,1,2
15,11,11
-15,12,-10

--------------------------------


6,4
68,74,98,40
82,13,45,54
83,51,88,89
91,71,7,40
31,1,96,82
22,97,63,17
3,3
571,757,-167,-745
1203,3152,2777,994
1004,2371,1858,115
1692,2417,2833,1366
1646,3077,2159,-546
1448,2124,1274,1595



3,-2,-1
14,-5,-4
14,6,15

"""

exit(-1)

