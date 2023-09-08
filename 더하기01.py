n = int(input("몇번 :"))
for i in range(0, n, 1):
    p = map(int, input("숫자입력 :").split())
    print(i+1,"번.", sum(p))

