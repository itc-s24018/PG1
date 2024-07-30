i_num_list = range(1, 11)
s_sum_list = list(map(lambda i: "No."+ str(i), i_num_list))
print("文字列リスト：", s_sum_list)

#　数値を文字に変換して修飾
for s in map(lambda i: "No."+ str(i), range(1, 11)):
    print(s, end=' ')

#偶数だけ取り出す
for e in filter(lambda i: i%2==0, range(1, 11)):
    print(e, end=" ")
