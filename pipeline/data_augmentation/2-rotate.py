#!/usr/bin/env python3
"""Module that defines a function to rotate an image."""
import tensorflow as tf


def rotate_image(image):
    """Rotate an image by 90 degrees counter-clockwise.

    Args:
        image: a 3D tf.Tensor containing the image to rotate.

    Returns:
        The rotated image.
    """
    return tf.image.rot90(image)
