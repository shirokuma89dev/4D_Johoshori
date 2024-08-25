

import numpy as np
import matplotlib.pyplot as plt
import numpy as np

import numpy as np

# シグモイド関数とその導関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def compute_output_with_learned_weights(input_data):
    # 順伝播
    layer1 = sigmoid(np.dot(input_data, weights1))
    output = sigmoid(np.dot(layer1, weights2))
    return output

x = [
    [0, 0], [0, 0.5], [0, 1],
    [0.5, 0], [0.5, 0.5], [0.5, 1],
    [1, 0], [1, 0.5], [1, 1]
]

# 勾配降下法？で頑張って求めてみました（あんまりよくわかっていない）
weights1 = [
    [1.43642476, 1.44389249, -23.87867004, -4.61102169],
    [0.190902, 0.18345505, 12.62101136, 3.092514],
]
weights2 = [[-5.8954511], [-5.82563046], [-32.85718252], [35.82311971]]

# 出力の計算
outputs = [compute_output_with_learned_weights(np.array(i)) for i in x]

# 出力のプロット
plotx = [i[0] for i in x]
ploty = [i[1] for i in x]
plotsize = [300.0 if out > 0.5 else 0.0 for out in outputs]

plt.scatter(plotx, ploty, s=plotsize)
plt.title('Neural Network Output')
plt.xlabel('Input Index')
plt.ylabel('Output Value')
plt.grid(True)
plt.show()
