#!/usr/bin/env python3
"""Defines the Simple_GAN class, a basic Generative Adversarial Network
built on top of keras.Model, that trains a generator and a discriminator
against each other."""
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


class Simple_GAN(keras.Model):
    """A simple Generative Adversarial Network.

    The model owns a generator and a discriminator network (both keras
    Models), a latent vector generator, and a set of real examples. The
    train_step method overloads the default keras.Model training step to
    alternately train the discriminator (disc_iter times) and the
    generator (once) on every call.
    """

    def __init__(self, generator, discriminator, latent_generator,
                 real_examples, batch_size=200, disc_iter=2,
                 learning_rate=.005):
        """Initializes the Simple_GAN instance.

        Args:
            generator (keras.Model): the generator network.
            discriminator (keras.Model): the discriminator network.
            latent_generator (callable): a function that takes an int
                `size` and returns a batch of `size` latent vectors.
            real_examples (tf.Tensor): a tensor containing the real
                examples the discriminator is trained on.
            batch_size (int): the size of a training batch.
            disc_iter (int): the number of times the discriminator is
                trained for each generator training step.
            learning_rate (float): the learning rate used by both the
                generator's and the discriminator's Adam optimizers.
        """
        super().__init__()  # run the __init__ of keras.Model first.
        self.latent_generator = latent_generator
        self.real_examples = real_examples
        self.generator = generator
        self.discriminator = discriminator
        self.batch_size = batch_size
        self.disc_iter = disc_iter

        self.learning_rate = learning_rate
        self.beta_1 = .5  # standard value, but can be changed if necessary
        self.beta_2 = .9  # standard value, but can be changed if necessary

        # define the generator loss and optimizer:
        self.generator.loss = lambda x: tf.keras.losses.MeanSquaredError()(
            x, tf.ones(x.shape))
        self.generator.optimizer = keras.optimizers.Adam(
            learning_rate=self.learning_rate, beta_1=self.beta_1,
            beta_2=self.beta_2)
        self.generator.compile(
            optimizer=self.generator.optimizer, loss=self.generator.loss)

        # define the discriminator loss and optimizer:
        self.discriminator.loss = lambda x, y: (
            tf.keras.losses.MeanSquaredError()(x, tf.ones(x.shape)) +
            tf.keras.losses.MeanSquaredError()(y, -1 * tf.ones(y.shape)))
        self.discriminator.optimizer = keras.optimizers.Adam(
            learning_rate=self.learning_rate, beta_1=self.beta_1,
            beta_2=self.beta_2)
        self.discriminator.compile(
            optimizer=self.discriminator.optimizer,
            loss=self.discriminator.loss)

    def get_fake_sample(self, size=None, training=False):
        """Generates a fake sample of the given size.

        Args:
            size (int): the number of fake examples to generate. Defaults
                to self.batch_size when not provided.
            training (bool): whether the generator is called in training
                mode.

        Returns:
            tf.Tensor: a batch of fake examples produced by the generator.
        """
        if not size:
            size = self.batch_size
        return self.generator(
            self.latent_generator(size), training=training)

    def get_real_sample(self, size=None):
        """Picks a random real sample of the given size.

        Args:
            size (int): the number of real examples to pick. Defaults to
                self.batch_size when not provided.

        Returns:
            tf.Tensor: a random batch drawn from self.real_examples.
        """
        if not size:
            size = self.batch_size
        sorted_indices = tf.range(tf.shape(self.real_examples)[0])
        random_indices = tf.random.shuffle(sorted_indices)[:size]
        return tf.gather(self.real_examples, random_indices)

    def train_step(self, useless_argument):
        """Runs a single training step of the GAN.

        The discriminator is trained self.disc_iter times on a real and a
        fake sample, and then the generator is trained once, using
        gradient descent through Adam optimizers.

        Args:
            useless_argument: unused, required by the keras.Model API.

        Returns:
            dict: the discriminator loss and the generator loss for this
                training step, under the keys "discr_loss" and
                "gen_loss".
        """
        for _ in range(self.disc_iter):
            # compute the loss for the discriminator in a tape watching
            # the discriminator's weights
            with tf.GradientTape() as disc_tape:
                # get a real sample
                real_sample = self.get_real_sample()
                # get a fake sample
                fake_sample = self.get_fake_sample(training=True)
                # compute the loss discr_loss of the discriminator on
                # real and fake samples
                discr_loss = self.discriminator.loss(
                    self.discriminator(real_sample, training=True),
                    self.discriminator(fake_sample, training=True))
            # apply gradient descent once to the discriminator
            discr_gradients = disc_tape.gradient(
                discr_loss, self.discriminator.trainable_variables)
            self.discriminator.optimizer.apply_gradients(
                zip(discr_gradients, self.discriminator.trainable_variables))

        # compute the loss for the generator in a tape watching the
        # generator's weights
        with tf.GradientTape() as gen_tape:
            # get a fake sample
            fake_sample = self.get_fake_sample(training=True)
            # compute the loss gen_loss of the generator on this sample
            gen_loss = self.generator.loss(
                self.discriminator(fake_sample, training=False))
        # apply gradient descent to the generator
        gen_gradients = gen_tape.gradient(
            gen_loss, self.generator.trainable_variables)
        self.generator.optimizer.apply_gradients(
            zip(gen_gradients, self.generator.trainable_variables))

        return {"discr_loss": discr_loss, "gen_loss": gen_loss}
