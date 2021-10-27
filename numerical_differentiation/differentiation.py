# 数値微分による、１次、２次の微分係数の算出

# 関数f(x)
def f(x):
    return 2 * x ** 3 - 4 * x ** 2 + 6 * x


# 1次微分係数の計算
def first(x, h):
    d1 = f(x + h) - f(x)
    r1 = d1 / h
    return r1

def second(x, h):
    d2 = f(x + 2 * h) - 2.0 * f(x + h) + f(x)
    r2 = d2 / h ** 2
    return r2

# 入力
h = float(input('微小区間を代入してください'))

# x座標
x = 2

# 出力の結果
print('x  \t ', x)
print('微小区間h', h)
print('1次微分係数', first(x, h))
print('2次微分係数', second(x, h))
