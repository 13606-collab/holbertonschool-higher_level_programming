#!/usr/bin/env python3
"""Defines the Yolo class that uses the Yolo v3 algorithm to perform
object detection.
"""
import numpy as np
import tensorflow.keras as K


class Yolo:
    """Uses the Yolo v3 algorithm to perform object detection."""

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """Initializes the Yolo class.

        Args:
            model_path: path to where a Darknet Keras model is stored.
            classes_path: path to where the list of class names used
                for the Darknet model, listed in order of index, can
                be found.
            class_t: float representing the box score threshold for
                the initial filtering step.
            nms_t: float representing the IOU threshold for non-max
                suppression.
            anchors: numpy.ndarray of shape (outputs, anchor_boxes, 2)
                containing all of the anchor boxes:
                    outputs: number of outputs (predictions) made by
                        the Darknet model.
                    anchor_boxes: number of anchor boxes used for each
                        prediction.
                    2 => [anchor_box_width, anchor_box_height]

        Public instance attributes:
            model: the Darknet Keras model.
            class_names: a list of the class names for the model.
            class_t: the box score threshold for the initial filtering
                step.
            nms_t: the IOU threshold for non-max suppression.
            anchors: the anchor boxes.
        """
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'r') as f:
            self.class_names = [line.strip() for line in f.readlines()]
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    @staticmethod
    def sigmoid(x):
        """Applies the sigmoid activation function.

        Args:
            x: numpy.ndarray containing the values to activate.

        Returns:
            A numpy.ndarray of the same shape as x with the sigmoid
            function applied element-wise.
        """
        return 1 / (1 + np.exp(-x))

    def process_outputs(self, outputs, image_size):
        """Processes the outputs of the Darknet model for a single
        image.

        Args:
            outputs: list of numpy.ndarrays containing the predictions
                from the Darknet model for a single image. Each output
                has shape (grid_height, grid_width, anchor_boxes,
                4 + 1 + classes):
                    grid_height, grid_width: the height and width of
                        the grid used for the output.
                    anchor_boxes: the number of anchor boxes used.
                    4: (t_x, t_y, t_w, t_h)
                    1: box_confidence
                    classes: class probabilities for all classes.
            image_size: numpy.ndarray containing the image's original
                size [image_height, image_width].

        Returns:
            A tuple of (boxes, box_confidences, box_class_probs):
                boxes: a list of numpy.ndarrays of shape (grid_height,
                    grid_width, anchor_boxes, 4) containing the
                    processed boundary boxes for each output,
                    respectively:
                        4 => (x1, y1, x2, y2), representing the
                        boundary box relative to original image.
                box_confidences: a list of numpy.ndarrays of shape
                    (grid_height, grid_width, anchor_boxes, 1)
                    containing the box confidences for each output,
                    respectively.
                box_class_probs: a list of numpy.ndarrays of shape
                    (grid_height, grid_width, anchor_boxes, classes)
                    containing the box's class probabilities for each
                    output, respectively.
        """
        boxes = []
        box_confidences = []
        box_class_probs = []

        image_height, image_width = image_size[0], image_size[1]
        input_width = self.model.input.shape[1]
        input_height = self.model.input.shape[2]

        for i, output in enumerate(outputs):
            grid_height, grid_width, anchor_boxes, _ = output.shape

            box_confidences.append(self.sigmoid(output[..., 4:5]))
            box_class_probs.append(self.sigmoid(output[..., 5:]))

            t_x = output[..., 0]
            t_y = output[..., 1]
            t_w = output[..., 2]
            t_h = output[..., 3]

            cx = np.arange(grid_width).reshape(1, grid_width, 1)
            cx = np.repeat(cx, grid_height, axis=0)
            cx = np.repeat(cx, anchor_boxes, axis=2)

            cy = np.arange(grid_height).reshape(grid_height, 1, 1)
            cy = np.repeat(cy, grid_width, axis=1)
            cy = np.repeat(cy, anchor_boxes, axis=2)

            bx = (self.sigmoid(t_x) + cx) / grid_width
            by = (self.sigmoid(t_y) + cy) / grid_height

            anchor_width = self.anchors[i, :, 0]
            anchor_height = self.anchors[i, :, 1]

            bw = (anchor_width * np.exp(t_w)) / input_width
            bh = (anchor_height * np.exp(t_h)) / input_height

            x1 = (bx - bw / 2) * image_width
            y1 = (by - bh / 2) * image_height
            x2 = (bx + bw / 2) * image_width
            y2 = (by + bh / 2) * image_height

            box = np.zeros(output[..., :4].shape)
            box[..., 0] = x1
            box[..., 1] = y1
            box[..., 2] = x2
            box[..., 3] = y2

            boxes.append(box)

        return boxes, box_confidences, box_class_probs

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """Filters the boundary boxes using the box score threshold.

        Args:
            boxes: a list of numpy.ndarrays of shape (grid_height,
                grid_width, anchor_boxes, 4) containing the processed
                boundary boxes for each output, respectively.
            box_confidences: a list of numpy.ndarrays of shape
                (grid_height, grid_width, anchor_boxes, 1) containing
                the processed box confidences for each output,
                respectively.
            box_class_probs: a list of numpy.ndarrays of shape
                (grid_height, grid_width, anchor_boxes, classes)
                containing the processed box class probabilities for
                each output, respectively.

        Returns:
            A tuple of (filtered_boxes, box_classes, box_scores):
                filtered_boxes: a numpy.ndarray of shape (?, 4)
                    containing all of the filtered bounding boxes.
                box_classes: a numpy.ndarray of shape (?,) containing
                    the class number that each box in filtered_boxes
                    predicts, respectively.
                box_scores: a numpy.ndarray of shape (?) containing
                    the box scores for each box in filtered_boxes,
                    respectively.
        """
        box_scores_list = []
        box_classes_list = []

        for confidence, class_probs in zip(
                box_confidences, box_class_probs):
            box_scores = confidence * class_probs
            box_classes_list.append(np.argmax(box_scores, axis=-1))
            box_scores_list.append(np.max(box_scores, axis=-1))

        boxes_all = np.concatenate(
            [b.reshape(-1, 4) for b in boxes], axis=0)
        box_classes_all = np.concatenate(
            [c.reshape(-1) for c in box_classes_list])
        box_scores_all = np.concatenate(
            [s.reshape(-1) for s in box_scores_list])

        filter_mask = box_scores_all >= self.class_t

        filtered_boxes = boxes_all[filter_mask]
        box_classes = box_classes_all[filter_mask]
        box_scores = box_scores_all[filter_mask]

        return filtered_boxes, box_classes, box_scores
