# Spheregraph

A python module to create an icosahedron and recursively subdivide the faces to generate a graph of a sphere.

## usage
```python
import spheregraph

icosahedron = spheregraph.get_icosahedron()
spheregraph.generate_set(icosahedron)
```

## tests
```bash
python spheregraph_tests.py
```
