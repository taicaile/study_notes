import numpy as np


def sigmoid(inX):
    return 1/(1+np.exp(-inX))


weights = np.array([-np.log(4), np.log(2), -np.log(3)])
input_vec = np.array([1, 1, 1])

print(sigmoid(np.sum(weights*input_vec)))
