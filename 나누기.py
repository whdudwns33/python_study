m = int(input())
n = list(map(int,input().split()))
num = 0
max_num = max(n)
for i in range(m):
    num += (n[i]/ max_num) * 100
print(num/m)

