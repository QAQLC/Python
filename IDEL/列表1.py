# 列表是一个序列

rhyme = [1, 2, 3, 4, 5, '山上打老虎']

for each in rhyme:
    print(each)

print()
print(rhyme[0])
print()

print(rhyme[-1])
print()

# 列表切片
print(rhyme[0:3])
print(rhyme[3:6])
print()
print(rhyme[:4])
print(rhyme[:])
print(rhyme[::2])

print(rhyme[::-1])  # 倒序输出
print(rhyme[::-2])  # 倒序输出
