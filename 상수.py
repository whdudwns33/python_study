n1, n2 = map(str, input().split())
number1 = ''
number2 = ''
for e in n1:
    number1 = e + number1
    number2 = e + number2
print(max(int(number1),int(number2)))



# if int(num1) > int(num2):
#     print(num1)
# elif int(num1 < int(num2)):
#     print(num2)
# else:
#     print(f"{num1} = {num2}")
