#!/usr/bin/env python3
"""Module for updating weights with gradient descent and Dropout."""
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """Updates the weights of a neural network with Dropout
    regularization using gradient descent.

    Args:
        Y: one-hot numpy.ndarray of shape (classes, m) with correct labels
        weights: dictionary of the weights and biases of the neural network
        cache: dictionary of the outputs and dropout masks of each layer
        alpha: the learning rate
        keep_prob: the probability that a node will be kept
        L: the number of layers of the network

    All layers use the tanh activation function except the last, which
    uses the softmax activation function. The weights are updated
    in place.
    """
    m = Y.shape[1]
    dZ = cache['A' + str(L)] - Y

    for i in range(L, 0, -1):
        A_prev = cache['A' + str(i - 1)]
        W_key = 'W' + str(i)
        b_key = 'b' + str(i)

        dW = (1 / m) * np.matmul(dZ, A_prev.T)
        db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)

        if i > 1:
            dZ = np.matmul(weights[W_key].T, dZ) * (1 - A_prev ** 2)
            dZ = dZ * cache['D' + str(i - 1)]
            dZ = dZ / keep_prob

        weights[W_key] = weights[W_key] - alpha * dW
        weights[b_key] = weights[b_key] - alpha * db
