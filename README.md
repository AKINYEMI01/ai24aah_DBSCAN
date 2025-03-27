# ai24aah_DBSCAN

# DBSCAN

DBSCAN is a density-based clustering algorithm that groups together points that are closely packed together, marking as outliers the points that lie alone in low-density regions.

# Key Concepts:
Epsilon (ε): The maximum radius of the neighborhood around a point.
MinPts: The minimum number of points required to form a dense region.
Core Point: A point that has at least MinPts points within its ε-neighborhood (including the point itself).
Border Point: A point that has fewer than MinPts within its ε-neighborhood but is in the neighborhood of a core point.
Noise Point: A point that is not a core point or a border point.


# Features
instagram dataset 


# Parameters

- `eps`: The maximum distance between two samples for them to be considered as in the same neighborhood.
- `min_samples`: The number of samples (or total weight) in a neighborhood for a point to be considered as a core point.
  
# Installation

To run the DBSCAN algorithm, you need to have Python installed on your machine. You can install the required packages using `pip`.

```bash
pip install -r requirements.txt
```

# Visualizing Clusters

```python
from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



