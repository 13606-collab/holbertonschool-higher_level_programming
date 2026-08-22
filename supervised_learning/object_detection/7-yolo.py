#!/usr/bin/env python3
"""Defines the Yolo class that uses the Yolo v3 algorithm to perform
object detection.
"""
import glob
import os
import cv2
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

    def non_max_suppression(self, filtered_boxes, box_classes, box_scores):
        """Applies non-max suppression to the filtered boundary boxes.

        Args:
            filtered_boxes: a numpy.ndarray of shape (?, 4) containing
                all of the filtered bounding boxes.
            box_classes: a numpy.ndarray of shape (?,) containing the
                class number for the class that filtered_boxes
                predicts, respectively.
            box_scores: a numpy.ndarray of shape (?) containing the
                box scores for each box in filtered_boxes,
                respectively.

        Returns:
            A tuple of (box_predictions, predicted_box_classes,
            predicted_box_scores):
                box_predictions: a numpy.ndarray of shape (?, 4)
                    containing all of the predicted bounding boxes
                    ordered by class and box score.
                predicted_box_classes: a numpy.ndarray of shape (?,)
                    containing the class number for box_predictions
                    ordered by class and box score, respectively.
                predicted_box_scores: a numpy.ndarray of shape (?)
                    containing the box scores for box_predictions
                    ordered by class and box score, respectively.
        """
        box_predictions = []
        predicted_box_classes = []
        predicted_box_scores = []

        unique_classes = np.unique(box_classes)

        for cls in unique_classes:
            idxs = np.where(box_classes == cls)[0]
            cls_boxes = filtered_boxes[idxs]
            cls_scores = box_scores[idxs]

            order = np.argsort(cls_scores)[::-1]
            cls_boxes = cls_boxes[order]
            cls_scores = cls_scores[order]

            keep = []
            indices = np.arange(len(cls_boxes))

            while len(indices) > 0:
                i = indices[0]
                keep.append(i)

                if len(indices) == 1:
                    break

                rest = indices[1:]

                x1 = np.maximum(cls_boxes[i, 0], cls_boxes[rest, 0])
                y1 = np.maximum(cls_boxes[i, 1], cls_boxes[rest, 1])
                x2 = np.minimum(cls_boxes[i, 2], cls_boxes[rest, 2])
                y2 = np.minimum(cls_boxes[i, 3], cls_boxes[rest, 3])

                w = np.maximum(0, x2 - x1)
                h = np.maximum(0, y2 - y1)
                inter = w * h

                area_i = ((cls_boxes[i, 2] - cls_boxes[i, 0]) *
                          (cls_boxes[i, 3] - cls_boxes[i, 1]))
                area_rest = ((cls_boxes[rest, 2] - cls_boxes[rest, 0]) *
                             (cls_boxes[rest, 3] - cls_boxes[rest, 1]))

                union = area_i + area_rest - inter
                iou = inter / union

                indices = rest[iou <= self.nms_t]

            box_predictions.append(cls_boxes[keep])
            predicted_box_classes.append(np.full(len(keep), cls))
            predicted_box_scores.append(cls_scores[keep])

        box_predictions = np.concatenate(box_predictions, axis=0)
        predicted_box_classes = np.concatenate(
            predicted_box_classes, axis=0)
        predicted_box_scores = np.concatenate(
            predicted_box_scores, axis=0)

        return box_predictions, predicted_box_classes, predicted_box_scores

    @staticmethod
    def load_images(folder_path):
        """Loads images from a folder.

        Args:
            folder_path: a string representing the path to the folder
                holding all the images to load.

        Returns:
            A tuple of (images, image_paths):
                images: a list of images as numpy.ndarrays.
                image_paths: a list of paths to the individual images
                    in images.
        """
        image_paths = glob.glob(folder_path + '/*')
        images = [cv2.imread(image_path) for image_path in image_paths]

        return images, image_paths

    def preprocess_images(self, images):
        """Preprocesses images for the Darknet model.

        Args:
            images: a list of images as numpy.ndarrays.

        Returns:
            A tuple of (pimages, image_shapes):
                pimages: a numpy.ndarray of shape (ni, input_h,
                    input_w, 3) containing all of the preprocessed
                    images:
                        ni: the number of images that were
                            preprocessed.
                        input_h: the input height for the Darknet
                            model. Note: this can vary by model.
                        input_w: the input width for the Darknet
                            model. Note: this can vary by model.
                        3: number of color channels.
                image_shapes: a numpy.ndarray of shape (ni, 2)
                    containing the original height and width of the
                    images:
                        2 => (image_height, image_width)
        """
        input_h = self.model.input.shape[2]
        input_w = self.model.input.shape[1]

        pimages = []
        image_shapes = []

        for image in images:
            image_shapes.append([image.shape[0], image.shape[1]])

            resized = cv2.resize(
                image, (input_w, input_h), interpolation=cv2.INTER_CUBIC)
            rescaled = resized / 255
            pimages.append(rescaled)

        pimages = np.array(pimages)
        image_shapes = np.array(image_shapes)

        return pimages, image_shapes

    def show_boxes(self, image, boxes, box_classes, box_scores, file_name):
        """Displays the image with all boundary boxes, class names,
        and box scores.

        Args:
            image: a numpy.ndarray containing an unprocessed image.
            boxes: a numpy.ndarray containing the boundary boxes for
                the image.
            box_classes: a numpy.ndarray containing the class indices
                for each box.
            box_scores: a numpy.ndarray containing the box scores for
                each box.
            file_name: the file path where the original image is
                stored.

        Boxes are drawn as a blue line of thickness 2. Class names
        and box scores are drawn above each box in red, rounded to 2
        decimal places, written 5 pixels above the top left corner of
        the box in FONT_HERSHEY_SIMPLEX with a font scale of 0.5, a
        line thickness of 1, and LINE_AA as the line type. If the s
        key is pressed, the image is saved in the detections
        directory (created if it does not exist) under file_name, and
        the window is closed. If any other key is pressed, the window
        is closed without saving.
        """
        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = box
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

            class_name = self.class_names[box_classes[i]]
            score = round(box_scores[i], 2)
            text = "{} {}".format(class_name, score)

            cv2.putText(image, text, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1,
                        cv2.LINE_AA)

        cv2.imshow(file_name, image)
        key = cv2.waitKey(0)

        if key == ord('s'):
            if not os.path.exists('detections'):
                os.makedirs('detections')
            cv2.imwrite(os.path.join('detections', file_name), image)

        cv2.destroyAllWindows()

    def predict(self, folder_path):
        """Predicts and displays bounding boxes for all images in a
        folder.

        Args:
            folder_path: a string representing the path to the folder
                holding all the images to predict.

        All image windows are named after the corresponding image
        filename without its full path, and displayed using the
        show_boxes method.

        Returns:
            A tuple of (predictions, image_paths):
                predictions: a list of tuples for each image of
                    (boxes, box_classes, box_scores).
                image_paths: a list of image paths corresponding to
                    each prediction in predictions.
        """
        images, image_paths = self.load_images(folder_path)
        pimages, image_shapes = self.preprocess_images(images)

        outputs = self.model.predict(pimages)

        predictions = []

        for i, image in enumerate(images):
            single_outputs = [output[i] for output in outputs]
            image_size = image_shapes[i]

            boxes, box_confidences, box_class_probs = (
                self.process_outputs(single_outputs, image_size))
            filtered_boxes, box_classes, box_scores = self.filter_boxes(
                boxes, box_confidences, box_class_probs)
            box_predictions, predicted_box_classes, predicted_box_scores = (
                self.non_max_suppression(
                    filtered_boxes, box_classes, box_scores))

            file_name = os.path.basename(image_paths[i])

            self.show_boxes(
                image, box_predictions, predicted_box_classes,
                predicted_box_scores, file_name)

            predictions.append(
                (box_predictions, predicted_box_classes,
                 predicted_box_scores))

        return predictions, image_paths
