# 별찍기
# 1.
n1 = int(input("정수 입력:"))
for i in range (0, n1):
    for j in range (i+1):
        print("*" , end= " ")
    print()
print()
# 2. 역으로 찍기
n2 = int(input("정수 입력:"))
for i in range (n2, 0, -1):
    for j in range(i):
        print("*" , end= " ")
    print()

# 3. 우측기준 직각삼각형
n3 = int(input("정수 입력:"))
for i in range(n3, 0, -1):
    for s in range(n3 - i): # 공백추가. 공백은 정방향으로 커져야 하는데, i는 큰수부터 작아짐. 따라서 고정되어있는 n3(최댓값)에서 i를 뺴는 것
        print(" ", end= " ")
    for j in range(i):
        print("*", end= " ")
    print()

# 4. 뒤집힌 삼각형
n3 = int(input("정수 입력:"))
for i in range(n3, 0, -1):
    for s in range(n3 - i):
        print(" ", end= "")
    for j in range(i):
        print("*", end= " ")
    print()

