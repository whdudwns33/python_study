word = []
rst = []
max = 0
for i in range(5):
    word.append(list(input()))
    if max < len(word[i]):
        max = len(word[i])

for i in range(max):
    for j in range(len(word)):
        if len(word[j]) <= max:
            word[j].append("")
        rst.append(word[j][i])

rst = "".join(rst)
print(rst)

# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx

# ABCDE
# abcde
# 01234
# FGHIJ
# fghij

