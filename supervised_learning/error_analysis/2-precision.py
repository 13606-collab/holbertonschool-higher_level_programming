#!/usr/bin/env python3
"""Calculates the precision for each class in a confusion matrix."""

import numpy as np


def precision(confusion):
    """Compute per-class precision from a confusion matrix."""
    return np.diag(confusion) / np.sum(confusion, axis=0)
