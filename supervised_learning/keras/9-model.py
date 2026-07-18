#!/usr/bin/env python3
"""Module that saves and loads an entire Keras model."""
import tensorflow.keras as K


def save_model(network, filename):
    """Save an entire model.

    Args:
        network (keras.Model): the model to save.
        filename (str): the path of the file that the model should
            be saved to.

    Returns:
        None
    """
    network.save(filename)

    return None


def load_model(filename):
    """Load an entire model.

    Args:
        filename (str): the path of the file that the model should
            be loaded from.

    Returns:
        keras.Model: the loaded model.
    """
    network = K.models.load_model(filename)

    return network
