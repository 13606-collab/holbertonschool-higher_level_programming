#!/usr/bin/env python3
"""Module that builds the ResNet-50 architecture as described in
Deep Residual Learning for Image Recognition (2015)"""
from tensorflow import keras as K
identity_block = __import__('2-identity_block').identity_block
projection_block = __import__('3-projection_block').projection_block


def resnet50():
    """Builds the ResNet-50 architecture as described in Deep Residual
    Learning for Image Recognition (2015)

    You can assume the input data will have shape (224, 224, 3)
    All convolutions inside and outside the blocks should be followed
    by batch normalization along the channels axis and a rectified
    linear activation (ReLU), respectively.
    All weights should use he normal initialization
    The seed for the he_normal initializer should be set to zero
    Returns: the keras model
    """
    init = K.initializers.he_normal(seed=0)
    X = K.Input(shape=(224, 224, 3))

    conv1 = K.layers.Conv2D(
        filters=64,
        kernel_size=(7, 7),
        strides=(2, 2),
        padding='same',
        kernel_initializer=init)(X)
    bn1 = K.layers.BatchNormalization(axis=3)(conv1)
    act1 = K.layers.Activation('relu')(bn1)
    pool1 = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same')(act1)

    conv2 = projection_block(pool1, [64, 64, 256], s=1)
    conv2 = identity_block(conv2, [64, 64, 256])
    conv2 = identity_block(conv2, [64, 64, 256])

    conv3 = projection_block(conv2, [128, 128, 512], s=2)
    conv3 = identity_block(conv3, [128, 128, 512])
    conv3 = identity_block(conv3, [128, 128, 512])
    conv3 = identity_block(conv3, [128, 128, 512])

    conv4 = projection_block(conv3, [256, 256, 1024], s=2)
    conv4 = identity_block(conv4, [256, 256, 1024])
    conv4 = identity_block(conv4, [256, 256, 1024])
    conv4 = identity_block(conv4, [256, 256, 1024])
    conv4 = identity_block(conv4, [256, 256, 1024])
    conv4 = identity_block(conv4, [256, 256, 1024])

    conv5 = projection_block(conv4, [512, 512, 2048], s=2)
    conv5 = identity_block(conv5, [512, 512, 2048])
    conv5 = identity_block(conv5, [512, 512, 2048])

    avg_pool = K.layers.AveragePooling2D(
        pool_size=(7, 7),
        padding='same')(conv5)

    output = K.layers.Dense(
        units=1000,
        activation='softmax',
        kernel_initializer=init)(avg_pool)

    model = K.models.Model(inputs=X, outputs=output)

    return model
