# 🎵 Amazon Music Clustering

## Overview

This project applies **K-Means Clustering** to group songs based on their audio characteristics without predefined genre labels.

Using features such as danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, and duration, the model identifies meaningful song segments that can support recommendation systems and playlist generation.

---

## Dataset

* Total Songs: **95,837**
* Features Used: **10 Audio Features**

### Features

```python
[
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
    "duration_ms"
]
```

---

## Workflow

* Data Cleaning
* Exploratory Data Analysis
* Feature Scaling
* K-Means Clustering
* Cluster Evaluation
* Cluster Profiling
* Dashboard Development

---

## Model Performance

| Metric               | Value   |
| -------------------- | ------- |
| Algorithm            | K-Means |
| Clusters             | 4       |
| Silhouette Score     | 0.243   |
| Davies-Bouldin Index | 1.333   |

---

## Cluster Summary

| Cluster | Description                            |
| ------- | -------------------------------------- |
| 0       | Spoken Content & Short Vocal Tracks    |
| 1       | High-Energy Dance & Pop Tracks         |
| 2       | Acoustic & Instrumental Relaxed Tracks |
| 3       | Long-Form Audio & Ambient Content      |

---

## Business Applications

### 🎧 Personalized Playlist Curation

Group similar songs together to create better playlists.

### 🔍 Song Recommendation

Recommend songs from the same audio cluster.

### 🎤 Artist Analysis

Identify songs competing within the same musical segment.

### 📈 Market Segmentation

Analyze listener preferences using cluster-based song groups.

---

## Dashboard Features

* Dataset Overview
* Cluster Distribution
* Cluster Analysis
* Song Explorer
* Business Insights
* Project Report

---

## Results

The final K-Means model successfully identified four distinct groups of songs based on audio characteristics.

These clusters can be used for recommendation systems, playlist generation, listener segmentation, and music discovery.
