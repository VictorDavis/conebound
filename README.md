# Bounding Cones

> "I could be bounded in a cone and count myself a king of infinite space."
>                                                           ~ Hamlet, II.ii

Finds the minimum bounding cone of N points in any dimension in O(n log n) time.

Implements the Voronoi-based algorithm described by [Barequet & Elber](http://www.cs.technion.ac.il/~gershon/papers/bounding_cones.pdf)

## Dependencies

- **numpy** for maths
- **scipy** for calculating convex hull

## Installation

```{bash}
pip install conebound
```

## Tests

![Bounding Cone Tests](https://github.com/VictorDavis/conebound/workflows/Bounding%20Cone%20Tests/badge.svg)

- Covers acute, obtuse, reflex cases
- Covers dimensions 2, 3, 4

```{bash}
pytest -v
```
