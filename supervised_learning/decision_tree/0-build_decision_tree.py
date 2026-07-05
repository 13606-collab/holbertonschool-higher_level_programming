#!/usr/bin/env python3
"""Module that defines the basic building blocks of a Decision Tree.

This module contains the `Node`, `Leaf` and `Decision_Tree` classes that
will progressively be extended throughout the project to build, fit and
use a decision tree for classification tasks.
"""
import numpy as np


class Node:
    """Represents an internal node of a decision tree.

    An internal node stores the feature and threshold used to split the
    population reaching it, as well as references to its left and right
    children.
    """

    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """Initialize a Node.

        Args:
            feature: The index of the feature used for the split.
            threshold: The threshold value used for the split.
            left_child: The left child node (or leaf).
            right_child: The right child node (or leaf).
            is_root (bool): Whether this node is the root of the tree.
            depth (int): The depth of this node within the tree.
        """
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """Return the maximum depth of the nodes below this node.

        Returns:
            int: The maximum depth found among this node's children,
            computed recursively (including leaves).
        """
        left_depth = self.left_child.max_depth_below()
        right_depth = self.right_child.max_depth_below()
        return max(left_depth, right_depth)


class Leaf(Node):
    """Represents a leaf of a decision tree.

    A leaf stores the predicted value for the individuals that reach it
    and has no children.
    """

    def __init__(self, value, depth=None):
        """Initialize a Leaf.

        Args:
            value: The predicted value stored by this leaf.
            depth (int): The depth of this leaf within the tree.
        """
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Return the depth of this leaf.

        Returns:
            int: The depth attribute of this leaf.
        """
        return self.depth


class Decision_Tree():
    """Represents a full decision tree.

    The tree is built from a root `Node` and can be used to predict the
    target value of a set of individuals based on their explanatory
    features.
    """

    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        """Initialize a Decision_Tree.

        Args:
            max_depth (int): The maximum depth allowed for the tree.
            min_pop (int): The minimum population size required to split
                a node further.
            seed (int): Seed used for the tree's random number generator.
            split_criterion (str): The criterion used to choose splits.
            root (Node): An existing root node to use for this tree.
        """
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """Return the maximum depth of the tree.

        Returns:
            int: The maximum depth of the tree, computed recursively
            from the root node.
        """
        return self.root.max_depth_below()
