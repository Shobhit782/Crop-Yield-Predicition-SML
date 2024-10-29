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
- [Structured Workflow](#Workflow)

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

## Workflow
1.	Dataset Collection:
o	The dataset is sourced from Kaggle and GitHub, with modifications made to enhance accuracy. With over 15,000 entries, it includes features such as country name, average rainfall, year, pesticide usage, average temperature, area, and crop name, providing a comprehensive base for analysis.

2.	Data Exploration:
o	Analyze the data to understand its structure, identify missing values, and observe preliminary trends. This helps in getting an overview of potential relationships between variables and crop yield.

3.	Data Pre-processing:
Clean and prepare the data for analysis. This step includes handling missing values, encoding categorical variables, and ensuring that the data is in a suitable format for modeling.

4.	Exploratory Data Analysis (EDA):
Perform visual and statistical analysis to gain deeper insights into the data. Using libraries like Matplotlib and Seaborn, create visualizations to explore relationships and patterns, aiding in hypothesis formation.

5.	Standardization and Column Transformation:
o	Standardize features to bring them to a common scale, especially useful for algorithms sensitive to feature magnitudes. Apply transformations to prepare data effectively for machine learning models.

6.	Train-Test Split:
o	Split the data into training and testing sets, ensuring that model evaluation is unbiased. This division allows us to assess the model’s performance on unseen data, validating its real-world applicability.

7. Training Multiple Models:
Trained different models to find the most accurate predictor. Models include:
a. Linear Regression, Lasso, and Ridge – Basic regression models that help predict yield based on input features.
b. K-Nearest Neighbors (KNN) Classifier – A non-parametric method used for both classification and regression.
c. Decision Tree – A versatile model that learns data patterns through a tree structure, capturing non-linear relationships.

8. Model Selection Based on R² Score and Accuracy:
Compared the models based on performance metrics such as R² score and MAE to select the best-performing model. This ensures that the final model provides reliable predictions, critical for agricultural planning and resource allocation.

Used KNN as our final model to predict


