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
    if len(val) != 4:
        print('input 4 numbers')
        continue
    answer = ''
    for i in range(4):
        if num4[i] == val[i]:
            answer += num4[i]
        else:
            answer += 'X'
    print('-> ' + answer)
