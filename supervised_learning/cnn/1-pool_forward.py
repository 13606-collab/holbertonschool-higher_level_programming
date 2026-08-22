#!/usr/bin/env python3
"""Module that performs forward propagation over a pooling layer."""
import numpy as np


def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """Perform forward propagation over a pooling layer of a NN.

    Args:
        A_prev: numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
            containing the output of the previous layer.
        kernel_shape: tuple of (kh, kw) containing the size of the
            kernel for the pooling.
        stride: tuple of (sh, sw) containing the strides for the
            pooling.
        mode: string containing either 'max' or 'avg', indicating
            whether to perform maximum or average pooling.

    Returns:
        The output of the pooling layer.
    """
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    h_new = (h_prev - kh) // sh + 1
    w_new = (w_prev - kw) // sw + 1

    output = np.zeros((m, h_new, w_new, c_prev))

    for i in range(h_new):
        for j in range(w_new):
            slice_A = A_prev[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            if mode == 'max':
                output[:, i, j, :] = np.max(slice_A, axis=(1, 2))
            else:
                output[:, i, j, :] = np.mean(slice_A, axis=(1, 2))

    return output
