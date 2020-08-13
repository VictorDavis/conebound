# bloody dependencies
import numpy as np
from numpy.linalg import norm
import unittest

# things to test
from conebound import bounding_cone


# unit tests
class ConeBoundTest(unittest.TestCase):

    # bounding cone aperture < 90
    def test_2d_acute(self):

        # hyperparameters
        ndim = 2
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 12, np.pi / 4)  # [15, 45]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(256, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9

    # bounding cone aperture > 90
    def test_2d_obtuse(self):

        # hyperparameters
        ndim = 2
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 4, np.pi / 2)  # [45, 90]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(256, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9

    # bounding cone aperture > 180
    def test_2d_reflex(self):

        # hyperparameters
        ndim = 2
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 2, 3 * np.pi / 4)  # [90, 135]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(256, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9

    # bounding cone aperture < 90
    def test_3d_acute(self):

        # hyperparameters
        ndim = 3
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 12, np.pi / 4)  # [15, 45]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(1024, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9

    # bounding cone aperture > 90
    def test_3d_obtuse(self):

        # hyperparameters
        ndim = 3
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 4, np.pi / 2)  # [45, 90]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(1024, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9

    # bounding cone aperture > 180
    def test_3d_reflex(self):

        # hyperparameters
        ndim = 3
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 2, 3 * np.pi / 4)  # [90, 135]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(1024, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9

    # bounding cone aperture < 90
    def test_4d_acute(self):

        # hyperparameters
        ndim = 4
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 12, np.pi / 4)  # [15, 45]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(4096, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9

    # bounding cone aperture > 90
    def test_4d_obtuse(self):

        # hyperparameters
        ndim = 4
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 4, np.pi / 2)  # [45, 90]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(4096, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9

    # bounding cone aperture > 180
    def test_4d_reflex(self):

        # hyperparameters
        ndim = 4
        axis = np.random.normal(size=ndim)
        axis /= norm(axis)
        angle = np.random.uniform(np.pi / 2, 3 * np.pi / 4)  # [90, 135]
        cos = np.cos(angle)

        # monte carlo construction of a cone
        points = np.random.normal(size=(4096, ndim))
        dot_products = np.dot(points, axis) / norm(points, axis=1)
        points = points[dot_products > cos, :]

        # get cone
        axis_, angle_ = bounding_cone(points)

        # bounding cone should be slightly narrower than monte carlo construction
        assert angle_ < angle

        # calculated axis should be "close" to construction axis
        assert sum(axis_ * axis) > 0.9
