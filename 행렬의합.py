n , m = map(int, input().split())
rst1 = []
rst2 = []
for i in range(n):
    a = list(map(int, input().split()))
    rst1.append(a)
print(rst1)

for i in range(m):
    b = list(map(int, input().split()))
    rst2.append(b)
print(rst2)

for i in range(n):
    rst3 = []
    for j in range(n):
        rst3.append(rst1[i][j] + rst2[i][j])
    print(rst3)


# A, B = [], []
# N , M = map(int, input().split())
# for i in range(N):
#     A.append(list(map(int, input().split())))
# for i in range(M):
#     B.append(list(map(int, input().split())))
# for i in range(N):
#     for j in range(M):
#         print(A[i][j] + B[i][j], end = ' ')
#     print()