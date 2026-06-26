#!/usr/bin/env python3
"""
Module implementing confusion matrix creation for classification evaluation.
"""

import numpy as np


def create_confusion_matrix(labels, logits):
    """
    Creates a confusion matrix from one-hot encoded labels and logits.

    Parameters:
    labels (numpy.ndarray): One-hot encoded correct labels of shape (m, classes)
    logits (numpy.ndarray): One-hot encoded predicted labels of shape (m, classes)

    Returns:
    numpy.ndarray: Confusion matrix of shape (classes, classes)
    """
    # Get the true class indices
    true_classes = np.argmax(labels, axis=1)
    # Get the predicted class indices
    pred_classes = np.argmax(logits, axis=1)
    
    # Number of classes
    num_classes = labels.shape[1]
    
    # Initialize confusion matrix
    confusion = np.zeros((num_classes, num_classes), dtype=int)
    
    # Fill the confusion matrix
    for t, p in zip(true_classes, pred_classes):
        confusion[t, p] += 1
    
    return confusion
