# bloody dependencies
import numpy as np
from numpy.linalg import inv, norm
from scipy.spatial import ConvexHull

# global constants
ZERO = 1e-15


def circumcenter(simplex: np.ndarray):
    """
    Circumcenter of a simplex on a unit hypersphere.

    :param simplex: ndarray of floats, shape (npoints, ndim)
    """

    npoints, ndim = simplex.shape
    assert npoints == ndim, "Object is not a simplex!"
    assert all(norm(simplex, axis=1) >= 1 - ZERO), "Object is not a simplex!"
    inverted = inv(simplex)
    one = np.ones(shape=(ndim, 1))
    center = np.dot(inverted, one)
    center = center.flatten()
    center = center / norm(center)
    return center


def bounding_cone(points: np.ndarray) -> tuple:
    """
    Bounding cone in N dimensions.

    :param points: ndarray of floats, shape (npoints, ndim)
        Coordinates of points.

    :return axis: ndarray of floats, shape (ndim,)
        Coordinates of cone axis.

    :return angle: float
        Half-aperture, angular distance from cone axis to surface
    """

    # meta
    npoints, ndim = points.shape
    points /= norm(points, axis=1, keepdims=True)

    # outsource convex hull
    hull = ConvexHull(points)

    # voronoi vertices <=> simplex circumcenters
    voronoi_vertices = np.array(
        [circumcenter(points[simplex, :]) for simplex in hull.simplices]
    )

    # cone apertures <=> simplex circumradii
    cosines = (points[hull.simplices[:, 0], :] * voronoi_vertices).sum(axis=1)

    # special case: reflex cones
    ref_points = points[0 : ndim + 1]
    is_reflex = [
        all(np.dot(ref_points, vertex) >= cos - ZERO)
        for vertex, cos in zip(voronoi_vertices, cosines)
    ]
    voronoi_vertices[is_reflex] = -voronoi_vertices[is_reflex]
    cosines[is_reflex] = -cosines[is_reflex]

    # widest aperture <=> biggest simplex circumradius
    widest = cosines.argmin()
    axis = voronoi_vertices[widest]
    angle = np.arccos(cosines[widest])

    # optimal bounding cone = complement of widest empty spanning cone
    axis = -axis
    angle = np.pi - angle

    # return as tuple
    return axis, angle
