def reverse(data):
    '''引数に受け取ったシーケンスを逆向きに渡す'''
    ret = []
    for index in range(len(data)-1, -1, -1):
        ret.append(data[index])
    return ret

# リストをforループのinに添える(forループで反復子が作られ)
for char in reverse('golf'):
    print(char, end=" ")


def reverse(data):
    for index in range(len(data) -1, -1, -1):
        yield data[index]

# ジェネレータをforループのinに添える
for char in reverse('golf'):
    print(char, end=" ")
