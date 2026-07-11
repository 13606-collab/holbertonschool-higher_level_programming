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

    def count_nodes_below(self, only_leaves=False):
        """Count the nodes below this node.

        Args:
            only_leaves (bool): If True, only count leaves. Otherwise
                count every node (including this one).

        Returns:
            int: The number of nodes (or leaves) below this node.
        """
        left_count = self.left_child.count_nodes_below(
            only_leaves=only_leaves)
        right_count = self.right_child.count_nodes_below(
            only_leaves=only_leaves)
        if only_leaves:
            return left_count + right_count
        return 1 + left_count + right_count

    def left_child_add_prefix(self, text):
        """Indent and prefix the string representation of a left child.

        Args:
            text (str): The string representation of the left child.

        Returns:
            str: The text with a branch prefix on the first line and a
            vertical bar prefix on the following lines.
        """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("    |  " + x) + "\n"
        return (new_text)

    def right_child_add_prefix(self, text):
        """Indent and prefix the string representation of a right child.

        Args:
            text (str): The string representation of the right child.

        Returns:
            str: The text with a branch prefix on the first line and a
            blank-space prefix on the following lines.
        """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("       " + x) + "\n"
        return (new_text)

    def __str__(self):
        """Return the string representation of this node and its subtree.

        Returns:
            str: A human-readable, tree-shaped representation of this
            node and all the nodes/leaves below it.
        """
        if self.is_root:
            s = f"root [feature={self.feature}, threshold={self.threshold}]\n"
        else:
            s = (f"-> node [feature={self.feature}, "
                 f"threshold={self.threshold}]\n")
        if self.left_child:
            s += self.left_child_add_prefix(self.left_child.__str__())
        if self.right_child:
            s += self.right_child_add_prefix(self.right_child.__str__())
        return s


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

    def count_nodes_below(self, only_leaves=False):
        """Count this leaf.

        Args:
            only_leaves (bool): Unused for leaves, kept for interface
                consistency with `Node.count_nodes_below`.

        Returns:
            int: Always 1, since a leaf counts as a single node.
        """
        return 1

    def __str__(self):
        """Return the string representation of this leaf.

        Returns:
            str: A human-readable representation of the leaf's value.
        """
        return (f"-> leaf [value={self.value}]")


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

    def count_nodes(self, only_leaves=False):
        """Count the nodes of the tree.

        Args:
            only_leaves (bool): If True, only count the leaves of the
                tree. Otherwise count every node, including internal
                nodes and the root.

        Returns:
            int: The number of nodes (or leaves) in the tree.
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        """Return the string representation of the whole tree.

        Returns:
            str: A human-readable, tree-shaped representation of the
            tree, starting from its root.
        """
        return self.root.__str__()
