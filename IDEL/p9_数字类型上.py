import decimal
# 整数
""" 精度无限大 """

# 浮点数, 有误差，和js一样

x = 0.1 + 0.2
print(x == 0.3)
""" 有误差。所以需第三方模块处理"""
a = decimal.Decimal("0.1")
b = decimal.Decimal("0.2")
print(a + b)

# 复数 complex number

c = 1 + 2j
# 获取实部
c.real
# 获取虚部
c.imag
