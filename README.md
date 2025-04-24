# Collaborative Filtering Recommendation System

## 📌 Overview
This project builds a collaborative filtering recommendation system using the MovieLens 100K dataset. It features both user-based and item-based filtering implemented with the Surprise library, and evaluates model accuracy with RMSE and Top-N recommendation metrics. Designed for clarity and modularity, it's ideal for learning or portfolio use.


## 🗃️ Dataset
- Source: [Kaggle - MovieLens 100K](https://www.kaggle.com/datasets/prajitdatta/movielens-100k-dataset)
- Files: `u.data`, `u.item`, `u.user`

## 📁 Project Structure
collaborative-filtering-recommender/
├── README.md
├── requirements.txt
├── data/
│   └── u.data
│   └── u.item
│   └── u.user
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_user_based_cf.ipynb
│   ├── 03_item_based_cf.ipynb
│   └── 04_evaluation_and_visualization.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── recommender.py
│   └── evaluation.py
└── results/
    ├── top_n_recommendations.csv
    └── evaluation_metrics.json
