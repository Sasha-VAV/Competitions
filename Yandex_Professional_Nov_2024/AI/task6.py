def square_sum(arr):
    s = 0.0
    for x in arr:
        s += x ** 2
    return s


def square_normalization(arr):
    s = square_sum(arr)
    s = s ** 0.5
    for i in range(len(arr)):
        arr[i] /= s
    return arr


def get_pearson_correlation_coefficient(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    n = len(x)
    sum_xy = sum(x * y)
    sum_xx = sum(x * x)
    sum_yy = sum(y * y)
    r = (n * sum_xy - sum_y * sum_x) / ((n * sum_xx - sum_x ** 2) * (n * sum_yy - sum_y ** 2)) ** 0.5
    return r


a = float(input())
x0, x1 = map(float, input().split())

exit(-1)
