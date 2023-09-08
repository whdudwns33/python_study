# 1.
A = list(map(int, input().split()))
n = int(input())
arr =[]
for i in range(len(A)):
    if A[i] < n :
        arr.append(A[i])
print(arr)
# 2.
n, x = int(input().split())
A = list(map(int, input().split()))

for i in range(n):
    if A[i] < x :
        print(A[i], end= " ")