#!/usr/bin/env python3
"""Module that sets up the gradient descent with momentum optimization
algorithm in TensorFlow.
"""
import tensorflow as tf


def create_momentum_op(alpha, beta1):
    """Sets up the gradient descent with momentum optimization
    algorithm in TensorFlow.

    Args:
        alpha (float): the learning rate.
        beta1 (float): the momentum weight.

    Returns:
        optimizer: the momentum optimizer.
    """
    optimizer = tf.keras.optimizers.SGD(
        learning_rate=alpha, momentum=beta1)
    return optimizer
