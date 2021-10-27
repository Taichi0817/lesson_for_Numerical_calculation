# 台形法による数値積分

# 関数f(x)
def f(x):
    return 3 * x ** 2 + 10

# 台形法
def trapezoidal(a, b, n):
    h = (b - a) / n # 微小区間
    G = h / 2 * ((f(a) + f(b)) + 2 * sum(f(a + h * i) for i in range(1, n)))
    return G, h

# 区間の設定
a = 1.0
b = 3.0

# 入力
n = int(input('定義域内の分割数(整数)を入力してください'))

# 結果の出力
print('結果および微小区間hは', *trapezoidal(a, b, n))
print('分割数n', n)