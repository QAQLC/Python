# 列表增

hero = ["钢铁侠", "绿巨人"]

hero.append("黑寡妇")  # 每次添加一个
print(hero)

hero.extend(["鹰眼", '雷神', '灭霸', '索尔'])
print(hero)

heros = []
heros[len(hero):] = "和鲁特"
print(heros)
print(heros[:1])  # "格"
# 数组切片使用

s = []
s[len(s):] = [1, 2, 3, 4]
print(s)

s[len(s):] = [5, 6, 7]

# 插入位置

s.insert(7, "插入 位置")
print(s)

s.insert(len(s), "末尾位置")
print(s)

# 删除指定元素 多个只会删除第一个，删除的不存在就会报错

hero.remove("灭霸")

# 删除指定元素

hero.pop(2)
print(hero)

# 清空

hero.clear()
print(hero)
