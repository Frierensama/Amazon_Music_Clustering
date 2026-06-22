````markdown
# Amazon Music Clustering

## Overview

This project uses **K-Means Clustering** to group songs based on their audio characteristics such as danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, and duration.

The goal is to automatically discover meaningful song groups without predefined genre labels.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit

---

## Dataset

- Records: **95,837 Songs**
- Features Used: **10 Audio Features**

```python
[
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
    'duration_ms'
]
```

---

## Project Workflow

1. Data Cleaning & EDA
2. Feature Scaling
3. K-Means Clustering
4. Cluster Evaluation
5. Cluster Profiling
6. Visualization
7. Streamlit Dashboard

---

## Model Performance

| Metric | Value |
|----------|----------|
| Algorithm | K-Means |
| Clusters | 4 |
| Silhouette Score | 0.243 |
| Davies-Bouldin Index | 1.333 |

---

## Cluster Summary

| Cluster | Description |
|----------|----------|
| 0 | Speed & Short Type |
| 1 | High-Energy & Danceble Type |
| 2 | Acoustic & Instrumental Type |
| 3 | Long Duration Type |

---

## Streamlit Dashboard

Features:

- Dataset Overview
- Cluster Analysis
- Song Explorer
- Project Report


