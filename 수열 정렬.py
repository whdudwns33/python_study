n = int(input())
t = list(map(int, input().split()))
s_li = sorted(t)
# print(s_li)
li = []
for i in range(n):
    idx = s_li.index(t[i])
    li.append(idx)
    print(li[i], end=" ")

