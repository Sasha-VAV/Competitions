import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
counts = [87, 63, 58, 43, 20, 14, 9, 6]
s = ""
for i in range(8):
    s += alphabet[i] * counts[i]
print(len(s), s)


probability = counts.copy()
for i in range(8):
    probability[i] /= sum(counts)


def shannon(p):
    p_sum = 0.0
    codes = []
    for i in range(len(p)):
        x = math.ceil(-math.log(p[i], 2))
        a = float.hex(p_sum)[2:]
        a = a[a.find(".") + 1: a.find("p")]
        s = ""
        d = {
            "0":"0000",
            "1":"0001",
            "2":"0010",
            "3":"0011",
            "4":"0100",
            "5":"0101",
            "6":"0110",
            "7":"0111",
            "8":"1000",
            "9":"1001",
            "a":"1010",
            "b":"1011",
            "c":"1100",
            "d":"1101",
            "e":"1110",
            "f":"1111"
        }
        for j in a:
            s += d[j]
        s += "0" * len(p)
        s = s[:x]
        codes.append(s)
        p_sum += p[i]
    return codes


# print(shannon([0.36, 0.18, 0.18, 0.12, 0.12, 0.09, 0.07]))

sh = ['00', '010', '100', '101', '1101', '11100', '111100', '111110']
n = ""
for i in range(len(sh)):
    n += counts[i] * sh[i]

print(len(n), n)

print(903 - 785)