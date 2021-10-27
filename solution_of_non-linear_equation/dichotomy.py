# 二分法による非線型方程式の解法

# 関数　f(x)


def f(x):
    return x ** 2 - 16


# 二分法


def dichotomy(a, b, ex):
    n = 1
    error = 1

    while error > ex:  # 中間値の計算
        c_n = (a + b) / 2.0
        y_n = f(c_n)
        print(n, "\t", c_n)

        posi_nega = y_n * f(b)
        error = abs(a - b)

        if posi_nega < 0:
            # f(x)とf(b)が異符号であれば、解は区間(c_n, b)の中に存在
            a = c_n
        else:  # f(x)とf(b)が同符号であれば、解は区間(a, c_n)の中に存在
            b = c_n
        n += 1
    #  入力


print("***二分法を用いて解を求めます。***")
print("収束判定の値を代入してください。ex = ? [1e-5程度]")
ex = float(input())
print("探索範囲となる2点a, bを入力してください。 [a, b]")
a, b = map(float, input().split())

#  結果の出力
print("解は以下の通りです。")
print("n \t xi")
dichotomy(a, b, ex)
