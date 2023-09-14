n1, n2 = map(int, input().split())
number1 = ''
number2 = ''
for e in str(n1):
    number1 = e + number1
for e in str(n2):
    number2 = e + number2
print(max(int(number1),int(number2)))


