#!/usr/bin/env python3
"""Module that defines a function to flip an image horizontally."""
import tensorflow as tf


def flip_image(image):
    """Flip a 3D image horizontally.

    Args:
        image: a 3D tf.Tensor containing the image to flip.

    Returns:
        The flipped image.
    """
    return tf.image.flip_left_right(image)
