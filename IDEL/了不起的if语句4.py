# for 变量 in 可迭代的对象

for each in "licheng":
    print(each)

print()
# 使用while循环再次实现
index = 0
# len 获取对象的长度
while index < len("licheng"):
    print("licheng"[index])
    index += 1

# 1 ~ 100W

sum = 0
for i in range(1000001):
    sum += i
print(sum)
