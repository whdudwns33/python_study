A = list(map(int, input().split()))
n = int(input())
arr =[]
for i in range(len(A)):
    if A[i] < n :
        arr.append(A[i])
print(arr)

