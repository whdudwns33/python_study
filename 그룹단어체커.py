n = int(input())
cnt = 1;
for i in range(n - 1):
    s = list(input())
    for j in range(len(s)):
        while True:
            if (j + 1) < len(s):
                if ord(s[j]) < ord(s[j + 1]):
                    cnt += 1
                else:
                    break
            else:
                break
print(cnt)
