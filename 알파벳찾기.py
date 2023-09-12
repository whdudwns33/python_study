alp = []
rst = []
for i in range(97, 124):
    alp.append(chr(i))
s = input()
for i in range(alp):
    if s == alp:
        rst.append(alp.index())
    else:
        rst.append(-1)
print(alp)