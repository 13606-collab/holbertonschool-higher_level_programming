#!/usr/bin/env python3
"""Module that performs pooling on images."""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Perform pooling on images.

    Args:
        images: numpy.ndarray with shape (m, h, w, c) containing multiple
            images.
            m is the number of images.
            h is the height in pixels of the images.
            w is the width in pixels of the images.
            c is the number of channels in the image.
        kernel_shape: tuple of (kh, kw) containing the kernel shape for
            the pooling.
            kh is the height of the kernel.
            kw is the width of the kernel.
        stride: tuple of (sh, sw).
            sh is the stride for the height of the image.
            sw is the stride for the width of the image.
        mode: indicates the type of pooling.
            max indicates max pooling.
            avg indicates average pooling.

    Returns:
        numpy.ndarray containing the pooled images.
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    out_h = (h - kh) // sh + 1
    out_w = (w - kw) // sw + 1
    pooled = np.zeros((m, out_h, out_w, c))

    if mode == 'max':
        op = np.max
    else:
        op = np.average

    for i in range(out_h):
        for j in range(out_w):
            y = i * sh
            x = j * sw
            image_slice = images[:, y:y + kh, x:x + kw, :]
            pooled[:, i, j, :] = op(image_slice, axis=(1, 2))

    return pooled
