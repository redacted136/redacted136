ke = ['数学', '语文', '美术', '编程', '音乐']
st = [8, 9, 10, 13, 14]
et = [10, 11, 12, 15, 16]
index = [0]
curr = 0
for i in range(1, len(ke)):
    # 如果课程可排，则将i添加到index，并更新curr
    if st[i] >= et[curr]:
        index.append(i)
        curr = i

for p in index:
    print(ke[p])