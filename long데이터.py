n = int(input("숫자 입력: "))

while n > 0:
    if n > 0 :
        long = 4
        print("long " * n + "int")
        print(long * n)
        break
    else:
        print("error")