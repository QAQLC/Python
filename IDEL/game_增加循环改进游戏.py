""" 用Python设计第一个小游戏改进版本 """
# 如何获取随机数
import random
counts = 3
randomNum = random.randint(1, 10)
print('随机数的值', randomNum)
while counts > 0:
    temp = input("不妨猜一下小鲫鱼现在心里想的是哪一个数字：")
    guess = int(temp)
    if guess == randomNum:
        print("你是小甲鱼心里的蛔虫吗？")
        print("猜中了也是没有奖励")
        break
    else:
        if guess < randomNum:
            print("小啦")
        else:
            print("大啦")
    counts = counts - 1
print("游戏结束了，不玩了")
