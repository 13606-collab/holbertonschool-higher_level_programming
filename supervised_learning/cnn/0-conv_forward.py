#!/usr/bin/env python3
"""Module that performs forward propagation over a convolutional layer."""
import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """Perform forward propagation over a convolutional layer of a NN.

    Args:
        A_prev: numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
            containing the output of the previous layer.
        W: numpy.ndarray of shape (kh, kw, c_prev, c_new) containing
            the kernels for the convolution.
        b: numpy.ndarray of shape (1, 1, 1, c_new) containing the
            biases applied to the convolution.
        activation: activation function applied to the convolution.
        padding: string that is either 'same' or 'valid', indicating
            the type of padding used.
        stride: tuple of (sh, sw) containing the strides for the
            convolution.

    Returns:
        The output of the convolutional layer.
    """
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, c_prev, c_new = W.shape
    sh, sw = stride

    if padding == "same":
        ph = int(np.ceil(((h_prev - 1) * sh + kh - h_prev) / 2))
        pw = int(np.ceil(((w_prev - 1) * sw + kw - w_prev) / 2))
    else:
        ph, pw = 0, 0

    A_prev_pad = np.pad(
        A_prev,
        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode="constant",
        constant_values=0,
    )

    h_new = (h_prev + 2 * ph - kh) // sh + 1
    w_new = (w_prev + 2 * pw - kw) // sw + 1

    output = np.zeros((m, h_new, w_new, c_new))

    for i in range(h_new):
        for j in range(w_new):
            slice_A = A_prev_pad[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            for k in range(c_new):
                output[:, i, j, k] = np.sum(
                    slice_A * W[:, :, :, k], axis=(1, 2, 3)
                )

    return activation(output + b)
