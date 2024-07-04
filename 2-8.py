my_list = [2,4,6,8,16]
print(my_list)
print(my_list + [3,6,9,12])


my_list.append(3)
my_list.append(6)
my_list.append(9)
print(my_list)

my_list.extend([12, 15])

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse()
print(my_list)

print(my_list[2:7])
print(my_list[2:7:2])
print(my_list[6:1:-1])
print(my_list[::-1])
print(my_list[6:100])
print(my_list[50:100])

my_list = [0,1,2,3,4,5,6,7,8]
my_list[0] = -1
print(my_list)

my_list = [0,1,2,3,4,5,6,7,8]
my_list[2:4] = [102, 103]
print(my_list)


my_list = [0,1,2,3,4,5,6,7,8]
my_list[2:6] = [101, 102]
print(my_list)


my_list = [0,1,2,3,4,5,6,7,8]
my_list[2:6] = []
print(my_list)
