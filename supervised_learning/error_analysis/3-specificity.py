#!/usr/bin/env python3
"""Calculates the specificity for each class in a confusion matrix."""

import numpy as np


def specificity(confusion):
    """Compute per-class specificity from a confusion matrix."""
    total = np.sum(confusion)
    tp = np.diag(confusion)
    fn = np.sum(confusion, axis=1)
    fp = np.sum(confusion, axis=0)

    tn = total - fn - fp + tp
    return tn / (tn + fp - tp)
