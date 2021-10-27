# はさみうち法による非線形方程式の解法

# 関数f(x)


def f(x):
    return x ** 2 - 16


# はさみうち法
def squeeze(a, b, ex):
    n = 1
    error_a = 1
    error_b = 1
    while error_a > ex and error_b > ex :
        # 点(a, f(a) と　点(b, f(b))を直線で結び、x軸との交点を求める
        x_i = (a * f(b) - b * f(a)) / (f(b) - f(a))
        y_i = f(x_i)
        print(n, "\t", x_i)

        posi_nega = y_i * f(b)
        error_a = abs(x_i - a) / abs(a)
        error_b = abs(x_i - b) / abs(b)

        if posi_nega < 0:  # f(x)とf(b)が異符号であれば、解は区間(x, b)の中に存在
            a = x_i
        else:  # f(x)とf(b)が同符号であれば、解は区間(a, x)の中に存在
            b = x_i
        n += 1


#  入力
print("***はさみうち法を用いて解を求めます。***")
print("収束判定の値を代入してください。ex = ? [1e-5程度]")
ex = float(input())
print("探索範囲となる2点a, bを入力してください。 [a, b]")
a, b = map(float, input().split())

#  結果の出力
print("解は以下の通りです。")
print("n \t xi")
squeeze(a, b, ex)