#!/usr/bin/env python3
"""Module for updating weights with gradient descent and L2 regularization."""
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """Updates the weights and biases of a neural network using gradient
    descent with L2 regularization.

    Args:
        Y: one-hot numpy.ndarray of shape (classes, m) with correct labels
        weights: dictionary of the weights and biases of the neural network
        cache: dictionary of the outputs of each layer of the neural network
        alpha: the learning rate
        lambtha: the L2 regularization parameter
        L: the number of layers of the network

    The neural network uses tanh activations on each layer except the
    last, which uses a softmax activation. The weights and biases are
    updated in place.
    """
    m = Y.shape[1]
    A_prev = cache['A' + str(L)]
    dZ = A_prev - Y

    for i in range(L, 0, -1):
        A_prev = cache['A' + str(i - 1)]
        W_key = 'W' + str(i)
        b_key = 'b' + str(i)

        dW = (1 / m) * np.matmul(dZ, A_prev.T) + (lambtha / m) * weights[W_key]
        db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)

        if i > 1:
            dZ = np.matmul(weights[W_key].T, dZ) * (1 - A_prev ** 2)

        weights[W_key] = weights[W_key] - alpha * dW
        weights[b_key] = weights[b_key] - alpha * db
