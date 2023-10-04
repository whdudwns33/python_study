word = []
for i in range(5):
    word.append(list(input()))
a = []
for i in range(len(word)):
    a.append(len(word[i]))
rst = []
for i in range(max(a)):
    for j in range(max(a)):
        if len(word[j]) < i:
            word[j].append("*")
        else:
            rst.append(word[j][i])
print(rst)



# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx

# rst = "".join(list)
# print(rst.replace("*", ""))


