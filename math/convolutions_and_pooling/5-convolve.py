#!/usr/bin/env python3
"""Module that performs a convolution on images using multiple kernels."""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Perform a convolution on images using multiple kernels.

    Args:
        images: numpy.ndarray with shape (m, h, w, c) containing multiple
            images.
            m is the number of images.
            h is the height in pixels of the images.
            w is the width in pixels of the images.
            c is the number of channels in the image.
        kernels: numpy.ndarray with shape (kh, kw, c, nc) containing the
            kernels for the convolution.
            kh is the height of a kernel.
            kw is the width of a kernel.
            nc is the number of kernels.
        padding: either a tuple of (ph, pw), 'same', or 'valid'.
            if 'same', performs a same convolution.
            if 'valid', performs a valid convolution.
            if a tuple:
                ph is the padding for the height of the image.
                pw is the padding for the width of the image.
            the image should be padded with 0's.
        stride: tuple of (sh, sw).
            sh is the stride for the height of the image.
            sw is the stride for the width of the image.

    Returns:
        numpy.ndarray containing the convolved images.
    """
    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(np.ceil(((sh * (h - 1)) + kh - h) / 2))
        pw = int(np.ceil(((sw * (w - 1)) + kw - w) / 2))
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    padded = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode='constant'
    )

    out_h = (h + 2 * ph - kh) // sh + 1
    out_w = (w + 2 * pw - kw) // sw + 1
    convolved = np.zeros((m, out_h, out_w, nc))

    for i in range(out_h):
        for j in range(out_w):
            y = i * sh
            x = j * sw
            image_slice = padded[:, y:y + kh, x:x + kw, :]
            for k in range(nc):
                convolved[:, i, j, k] = np.sum(
                    image_slice * kernels[:, :, :, k], axis=(1, 2, 3)
                )

    return convolved
