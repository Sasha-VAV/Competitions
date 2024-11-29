T = [6, 3]
m = 13


def sum(P, Q):
    S = [0, 0]
    a = (Q[1] - P[1]) / (Q[0] - P[0])
    S[0] = (a**2 - P[0] - Q[0]) % 37
    S[1] = (a*(P[0] - S[0]) - Q[0])
    return S


def double(P):
    a = (3 * (P[0] ** 2) - 5) / (2 * P[0])
    S = [0, 0]
    S[0] = (a**2 - 2 * P[0])
    S[1] = (a*(P[0] - S[0]) - P[0])
    return S


t2 = double(T)
t4 = double(T)
t8 = double(T)
t3 = sum(T, t2)
t6 = double(t3)
t12 = double(t6)
t13 = sum(t12, T)
print(t13)