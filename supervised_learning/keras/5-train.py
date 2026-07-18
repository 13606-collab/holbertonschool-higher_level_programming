#!/usr/bin/env python3
"""Module that trains a model using mini-batch gradient descent."""
import tensorflow.keras as K


def train_model(
        network, data, labels, batch_size, epochs,
        validation_data=None, verbose=True, shuffle=False):
    """Train a model using mini-batch gradient descent, and also
    analyze validation data if provided.

    Args:
        network (keras.Model): the model to train.
        data (numpy.ndarray): array of shape (m, nx) containing the
            input data.
        labels (numpy.ndarray): one-hot array of shape (m, classes)
            containing the labels of data.
        batch_size (int): the size of the batch used for mini-batch
            gradient descent.
        epochs (int): the number of passes through data for
            mini-batch gradient descent.
        validation_data: the data to validate the model with, if
            not None.
        verbose (bool): determines if output should be printed
            during training.
        shuffle (bool): determines whether to shuffle the batches
            every epoch. Normally, it is a good idea to shuffle, but
            for reproducibility, we have chosen to set the default
            to False.

    Returns:
        History: the History object generated after training the
            model.
    """
    history = network.fit(
        data, labels,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=validation_data,
        verbose=verbose,
        shuffle=shuffle)

    return history
