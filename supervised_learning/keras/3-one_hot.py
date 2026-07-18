#!/usr/bin/env python3
"""Module that converts a label vector into a one-hot matrix."""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """Convert a label vector into a one-hot matrix.

    Args:
        labels (array-like): the label vector to convert.
        classes (int): the number of classes. If None, it is
            inferred from the labels.

    Returns:
        numpy.ndarray: the one-hot matrix, where the last dimension
            is the number of classes.
    """
    one_hot_matrix = K.utils.to_categorical(labels, num_classes=classes)

    return one_hot_matrix
