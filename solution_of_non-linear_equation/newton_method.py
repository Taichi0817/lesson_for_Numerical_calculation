# ニュートン法による非線型方程式の解法
import math


# 関数f(x)
def f(x):
    return x - math.exp(-x)


# 関数f'(x)
def f_d(x):
    return 1 + math.exp(-x)


# ニュートン法
def newton_method(x0):
    # 初期値設定
    n = 1
    error = 1
    ex = 1e-5  # 収束判定
    x_n = x0  # 第0近似根

    while error > ex:
        x_n1 = x_n - f(x_n) / f_d(x_n)  # 第n+1近似根の導出
        error = abs(x_n1 - x_n)
        print(n, '\t', x_n1)

        x_n = x_n1
        n += 1


#  入力
print("***ニュートン法を用いて解を求めます。***")
x0 = float(input("第0近似根 x0 = ?"))

#  結果の出力
print("解は以下の通りです。")
print("n \t xi")
newton_method(x0)
