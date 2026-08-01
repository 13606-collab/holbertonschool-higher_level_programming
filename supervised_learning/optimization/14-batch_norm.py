#!/usr/bin/env python3
"""Module that creates a batch normalization layer for a neural
network in tensorflow.
"""
import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """Creates a batch normalization layer for a neural network in
    tensorflow.

    Args:
        prev: the activated output of the previous layer.
        n (int): the number of nodes in the layer to be created.
        activation: the activation function that should be used on
            the output of the layer.

    Returns:
        A tensor of the activated output for the layer.
    """
    kernel_init = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    dense = tf.keras.layers.Dense(units=n, kernel_initializer=kernel_init)
    Z = dense(prev)

    gamma = tf.Variable(
        initial_value=tf.ones((1, n)), trainable=True, name='gamma')
    beta = tf.Variable(
        initial_value=tf.zeros((1, n)), trainable=True, name='beta')

    mean, variance = tf.nn.moments(Z, axes=[0])
    epsilon = 1e-7
    Z_norm = tf.nn.batch_normalization(
        Z, mean, variance, beta, gamma, epsilon)

    return activation(Z_norm)
#!/usr/bin/env python3
"""Module for calculating cost of a neural network with L2 regularization."""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """Calculates the cost of a neural network with L2 regularization.

    Args:
        cost: the cost of the network without L2 regularization
        lambtha: the regularization parameter
        weights: dictionary of the weights and biases (numpy.ndarrays)
            of the neural network
        L: the number of layers in the neural network
        m: the number of data points used

    Returns:
        the cost of the network accounting for L2 regularization
    """
    weights_sum = 0
    for i in range(1, L + 1):
        weights_sum += np.linalg.norm(weights['W' + str(i)])

    l2_cost = cost + (lambtha / (2 * m)) * weights_sum
    return l2_cost