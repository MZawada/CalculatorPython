print("Calculator " + '\n')

num1 = float(input('1st num: ' + '\n'))
num2 = float(input('2nd num: ' + '\n'))
math = input("Calculate... \n +  - * / ")
if math == '+':
    score = num1 + num2
elif math == '-':
    score = num1 - num2
elif math == '*':
    score = num1 * num2
else:
    score = num1 // num2
print(score)


