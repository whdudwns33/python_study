d = list(input())
a = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
sum = 0

for i in range(len(a)):
    for j in range(len(d)):
        if d[j] in a[i]:
            sum += (i+1+2)
print(sum)

