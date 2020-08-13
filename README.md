# Bounding Cones

> "I could be bounded in a cone and count myself a king of infinite space."
>                                                           ~ Hamlet, II.ii

Implements the $O(n \log n)$ Voronoi-based algorithm described by [Barequet & Elber](http://www.cs.technion.ac.il/~gershon/papers/bounding_cones.pdf) in arbitrary dimension.

## Dependencies

- **numpy** for maths
- **scipy** for calculating convex hull

## Installation

```{bash}
pip install conebound
```

## Tests

- Covers acute, obtuse, reflex cases
- Covers dimensions 2, 3, 4

```
pytest -v
```
