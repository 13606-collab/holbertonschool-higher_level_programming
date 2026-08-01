#!/usr/bin/env python3
"""Module for calculating cost of a neural network with L2 regularization."""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """Calculates the cost of a neural network with L2 regularization.

    Args:
        cost: a tensor containing the cost of the network without
            L2 regularization
        model: a Keras model that includes layers with L2 regularization

    Returns:
        a tensor containing the total cost for each layer of the network,
        accounting for L2 regularization
    """
    l2_costs = []
    for loss in model.losses:
        l2_costs.append(cost + loss)

    return tf.stack(l2_costs)
