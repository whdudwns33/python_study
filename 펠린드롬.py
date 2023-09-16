S = input()
s =list(S)
p = []
for i in range(len(s)):
    if s[i] == s[len(s)-i - 1]:
        se = 1
        p.append(se)
    else:
        se = 0
        p.append(se)

if set(p) == {1}:
    print(1)
else :
    print(0)
