# Crop Yield Prediction System
This project is developed by:

1. Raghav Singhal
2. Shobhit Choudhury
3. Abhyuday Tripathi

## Overview
The Crop Yield Prediction System is a machine learning project designed to predict the yield of various crops based on historical agricultural data. This system focuses on factors such as average rainfall, pesticide use, average temperature, area of land, and specific crop items, particularly in the context of India.
## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)

## Features

- Predict crop yield based on input parameters.
- Machine learning model using KNN
- Visualization for better understanding.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Seaborn
- Jupyter Notebook

## Dataset

The project uses a dataset named `yield_df.csv`, which contains historical crop yield data for various crops over the World. The dataset includes the following fields:

- Year
- Country
- Crop Item (e.g., wheat, rice, etc.)
- Yield(hg/ha)
- Average Rainfall (mm)
- Pesticide Use (liters per hectare)
- Average Temperature (°C)

## Procedure
Training Multiple Models:
o	Trained different models to find the most accurate predictor. Models include:
	Linear Regression, Lasso, and Ridge – Basic regression models that help predict yield based on input features.
	K-Nearest Neighbors (KNN) Classifier – A non-parametric method used for both classification and regression.
	Decision Tree – A versatile model that learns data patterns through a tree structure, capturing non-linear relationships.

Model Selection Based on R² Score and Accuracy:
o	Compared the models based on performance metrics such as R² score and accuracy to select the best-performing model. This ensures that the final model provides reliable predictions, critical for agricultural planning and resource allocation.
Used KNN as our final model to predict


