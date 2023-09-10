arr = []
tmp = 0
# 12345
n, m = map(int, input().split())
for i in range(n):
    arr.append(i + 1)

# for l in range (m):
#     i, j = map(int, input().split())
#     arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]
#     print(arr)
for s in range(m):
    i, j = map(int, input().split())
    tmp = arr[i -1]
    arr[i - 1] = arr [j - 1]
    arr[j - 1] = tmp
    print(arr)




