num = list(map(int, input().split()))
n = [1,1,2,2,2,8]
rst = []
for i in range(len(num)) :
    e = n[i] - num[i]
    print(e, end=" ")