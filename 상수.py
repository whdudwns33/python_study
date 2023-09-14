n1, n2 = map(str, input().split())
number1 = ''
number2 = ''
for e in n1:
    number1 = e + number1
    number2 = e + number2
print(max(int(number1),int(number2)))


