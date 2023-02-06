""" 用Python设计第一个小游戏 """

temp = input("不妨猜一下小鲫鱼现在心里想的是哪一个数字：")
guess = int(temp)

if guess == 8:
    print("你是小甲鱼心里的蛔虫吗？")
    print("猜中了也是没有奖励")
else:
    print("你猜错啦")

print("游戏结束了，不玩了")
