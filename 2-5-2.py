answer = '''○ ● ● ●
● ○ ● ●
● ● ○ ●
● ● ● ○
'''
print(answer)
a = ''
w = '○ '
b = '● '
for i in range(4):
    for j in range(4):
        if i == j:
            a += w
        else:
            a += b
    a += '\n'
print(a)
