import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Amazon Music Clustering",page_icon="🎵",layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv(os.getenv('clustered_csv_path'))

df = load_data()

st.sidebar.title("Amazon Music Clustering")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Cluster Analysis",
        "Song Explorer",
        "Project Report"
    ]
)

TOTAL_SONGS = len(df)
TOTAL_CLUSTERS = df["Cluster"].nunique()

SILHOUETTE_SCORE = 0.243
DAVIES_BOULDIN = 1.333

features = [
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

if page == "Overview":

    st.title("Amazon Music Clustering Dashboard")

    st.markdown("""
    This project groups songs into meaningful clusters based on their
    audio characteristics using **K-Means Clustering**.
    """)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Songs", f"{TOTAL_SONGS:,}")
    c2.metric("Clusters", TOTAL_CLUSTERS)
    c3.metric("Silhouette Score", SILHOUETTE_SCORE)
    c4.metric("Davies-Bouldin", DAVIES_BOULDIN)

    st.markdown("---")

    st.subheader("Cluster Distribution")

    cluster_counts = df["Cluster"].value_counts().reset_index()

    cluster_counts.columns = ["Cluster", "Count"]

    fig = px.bar(
        cluster_counts,
        x="Cluster",
        y="Count",
        text="Count",
        title="Songs per Cluster"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Project Objective")

    st.info("""
    Automatically group similar songs using audio features such as
    danceability, energy, loudness, speechiness, acousticness,
    instrumentalness, liveness, valence, tempo and duration.
    """)

elif page == "Cluster Analysis":

    st.title("Cluster Analysis")

    cluster_profile = df.groupby("Cluster")[features].mean()

    st.subheader("Cluster Feature Heatmap")

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.heatmap(cluster_profile,annot=True,cmap="coolwarm",ax=ax)
    st.pyplot(fig)

    st.subheader("Cluster Profiles")

    cluster_choice = st.selectbox("Select Cluster", sorted(df["Cluster"].unique()))

    st.dataframe( cluster_profile.loc[[cluster_choice]].round(3),use_container_width=True)

    cluster_descriptions = {
        0: """
        Speed & Short Type

        - speechness, liveness, dancebility +ve
        - duration, loudness -ve
        """,

        1: """
        High-Energy & Danceble Type

        - energy, loudness, valence +ve
        - acousticness -ve
        """,

        2: """
        Acoustic & Instrumental Type

        - instrumental, acousticness +ve
        - energy , dancebility, valence -ve
        """,

        3: """
        Long Duration Type

        - duration, livemness, speechieness +ve
        - loudness, tempo -ve
        """
    }

    st.success(cluster_descriptions[cluster_choice])


elif page == "Song Explorer":

    st.title("Song Explorer")

    cluster_filter = st.selectbox("Select Cluster",sorted(df["Cluster"].unique()))
    filtered = df[df["Cluster"] == cluster_filter]

    st.write(
        f"Songs in Cluster {cluster_filter}: "
        f"{len(filtered):,}"
    )

    display_cols = ["name_song","name_artists","Cluster"]
    st.dataframe(filtered[display_cols],use_container_width=True,height=600)

elif page == "Project Report":

    st.title("Project Report")

    st.markdown('---')

    st.header("problem statement")

    st.write("""
    With millions of songs available on streaming platforms,manually categorizing music is impractical.
    This project uses K-Means clustering to automatically group songs based on audio characteristics.
    """)

    st.header("Procedure - ")

    st.markdown("""
    - Data Cleaning
    - Feature Selection
    - Standard Scaling
    - K-Means Clustering
    - Silhouette Analysis
    - Cluster Profiling
    - Business Interpretation
    """)

    st.header("Model Performance")

    metrics_df = pd.DataFrame({
        "Metric": [
            "Algorithm",
            "Clusters",
            "Silhouette Score",
            "Davies-Bouldin Index"
        ],
        "Value": [
            "K-Means",
            4,
            0.243,
            1.333
        ]
    })

    st.table(metrics_df)

    st.header("Summary")

    summary_df = pd.DataFrame({
        "Cluster": [0,1,2,3],
        "Description": [
            "Speed & Short Type",
            "High-Energy & Dancble Type",
            "Acoustic & Instrumental Type",
            "Long Duration Type"
        ]
    })

    st.table(summary_df)

    st.header("Conclusion")

    st.success("""
    K-Means clustering successfully identified four
    distinct groups of songs based on audio features.
    """)