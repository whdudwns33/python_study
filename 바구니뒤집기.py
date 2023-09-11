n = int(input("배열 :"))
num = []
for i in range(n+1):
    num.append(i)
print(num)

while True:
    a = int(input("[1] go on [2] stop :"))
    if a == 1:
        start, finish = map(int, input("시작, 끝").split())
        rev = sorted(num[start:finish + 1], reverse= True)
        print(num[:start] + rev + num[finish + 1 :])
    elif a == 2:
        break


