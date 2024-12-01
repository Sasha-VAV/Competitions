def softmax(arr):
    sum_arr = 0
    e = 2.718281828459
    for i in range(len(arr)):
        sum_arr += e ** arr[i]
    result = [0.0] * len(arr)
    for i in range(len(arr)):
        result[i] = e ** arr[i] / sum_arr
    return result


def get_loss(z, y):
    sf = softmax(z)
    result = 0.0
    for i in range(len(y)):
        for j in range(len(y)):
            result += y[i][j] * sf[j]
    return result


m = int(input())
Z = list(map(float, input().split()))
V = list()
for i in range(m):
    x = list(map(float, input().split()))
    V.append(x.copy())

transposed_V = V.copy()
for ii in range(len(transposed_V)):
    for jj in range(ii + 1, len(transposed_V[ii])):
        transposed_V[ii] = V[ii].copy()
        transposed_V[jj] = V[jj].copy()
        transposed_V[ii][jj] = V[jj][ii]
        transposed_V[jj][ii] = V[ii][jj]

diff = 1e-5
for i in range(m):
    a = get_loss(Z, transposed_V)
    Z_diff = Z.copy()
    Z_diff[i] += diff
    b = get_loss(Z_diff, transposed_V)
    print((b - a) / diff, end=" ")
