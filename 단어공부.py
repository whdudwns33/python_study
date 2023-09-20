s = list(input().upper())
rst = []
for i in range(len(s)):
    str_num = s.count(s[i])
    rst.append(str_num)
print(rst)
