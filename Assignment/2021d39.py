import numpy as np

# 係数行列と定数ベクトルを含む行列
aa = np.array([[1e-13, 30, 40, 50], [20, 300, 20, 50], [30, 40, 40, 10]])


def gauss_jordan(matrix):
    matrix = matrix.copy()
    n = len(matrix)

    # 上三角行列へ変形
    for i in range(n):
        matrix[i] = matrix[i] / matrix[i, i]  # 正規化

        for j in range(i + 1, n):
            matrix[j] -= matrix[i] * matrix[j, i]

    # 後退代入フェーズ
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            matrix[j] -= matrix[i] * matrix[j, i]

    return matrix[:, -1]


def pivot_gauss_jordan(matrix):
    matrix = matrix.copy()
    n = len(matrix)

    # 上三角行列へ変形
    for i in range(n):

        # ピボットを選択
        max_val = 0
        pivot = i
        for j in range(i, n):
            if abs(matrix[j, i]) > max_val:
                max_val = abs(matrix[j, i])

            pivot = j

        # ピボット行を交換
        matrix[[i, pivot]] = matrix[[pivot, i]]

        matrix[i] = matrix[i] / matrix[i, i]  # 正規化
        for j in range(i + 1, n):
            matrix[j] -= matrix[i] * matrix[j, i]

    # 後退代入フェーズ
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            matrix[j] -= matrix[i] * matrix[j, i]

    return matrix[:, -1]


print("ガウス・ジョルダン法:")
try:
    x = gauss_jordan(aa)
    print(x)
except Exception as e:
    print(e)

print("\nピボット選択法:")
try:
    x = pivot_gauss_jordan(aa)
    print(x)
except Exception as e:
    print(e)


## result
## ガウス・ジョルダン法:
## [-1.390625    0.18996416  1.10752688]
## 
## ピボット選択法:
## [-1.39520958  0.18562874  1.11077844]