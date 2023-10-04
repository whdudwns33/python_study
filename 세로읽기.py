word = []
rst = []
for i in range(5):
    word.append(list(input()))

for i in range(6):
    for j in range(len(word)):
        if len(word[j]) <= 6:
            word[j].append("")
        rst.append(word[j][i])

rst = "".join(rst)
print(rst)

# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx



