from random import sample as sl
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sample4 = sl(numbers, k=4)
num4 = ''.join(sample4)
print(num4)

while True:
    val = input('４桁の数字を入力してください：')
    if val == num4:
        print('OK')
        break
    else:
        print(val, ':NG')
