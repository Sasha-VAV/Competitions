f = open("task1.txt", encoding="utf-8")
s = f.readlines()[2:]
data = []
for line in s:
    x = line.split("|")
    a = float(x[2].replace(" ", ""))
    b = x[3].replace(" ", "")
    data.append([a, 0 if b.find("Нес") > -1 else 1])

data.sort(reverse=True)
print(data)
tp = 0
fp = 0
running_precision = 0.0
k = 0
for x in data:
    k += 1
    if x[0] < 0.5 and x[1] == 0 or x[0] >= 0.5 and x[1] == 1:
        tp += 1
    else:
        fp += 1
    running_precision += tp / (tp + fp)
    print(tp, fp, running_precision / k)

print(f"Answer: {round(running_precision / k, 2)}")
