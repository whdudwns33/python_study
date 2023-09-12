alp = []
rst = []
for i in range(97, 124):
    alp.append(chr(i))

s = input()
for i in range(len(alp)):
    if s[:] == alp[i]:
        rst.append(alp[i])
    else:
        rst.append(-1)
print(rst)