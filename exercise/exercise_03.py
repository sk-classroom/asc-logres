#
# In this expercise, you will:
# 1. understand the concept of regularization and how it helps to avoid overfitting.
# %%
%load_ext autoreload
%autoreload 2
import sys
import numpy as np
sys.path.append("../assignments")
from utils import *
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns

# Load the penguin dataset
penguins = sns.load_dataset("penguins")

# Drop the rows with missing values
penguins = penguins.dropna()

penguins.describe()
# %%

# We will use the all numerical features
focal_cols = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]
X = penguins[focal_cols].values
y = penguins["species"].values

# %% Split the data into training and testing sets
# Notice that we are using 95% of the data for testing and 5% for training
# This is because we want to simulate an overfitting scenario
X_train, X_test, y_train, y_test = train_test_split(
    X,  # Feature matrix
    y,  # Target variable
    test_size=0.95,  # Proportion of the dataset to include in the test split
    random_state=42,  # The seed used by the random number generator
    #stratify=y  # This stratify parameter makes a split so that the proportion of values in the sample produced will be the same as the proportion of values provided to parameter stratify
)
# %% Apply the standard scaler to the training data
sc = StandardScaler()
sc.fit(X_train) # Do not use the testing data for fitting the scaler
X_train_std = sc.transform(X_train) # Standardize the training data
X_test_std = sc.transform(X_test) # Standardize the testing data

# %% Apply the logistic regression model using scikit-learn without regularization
lr = LogisticRegression(
    penalty = None, # The penalty term is used to prevent overfitting. The "none" means no penalty term
    solver = "saga",
    multi_class="ovr",  # The "ovr" stands for One-vs-Rest, which means that in the case of multi-class classification, a separate model is trained for each class predicted against all other classes
    random_state=42  # The seed used by the random number generator for shuffling the data
)
lr.fit(
    X_train_std,  # The training data
    y_train  # The target variable to try to predict in the case of supervised learning
)

# %%
# TODO: Evaluate the performance by using accuracy as a metric. Do not use scikit-learn's accuracy_score function. Use numpy to calculate the accuracy.
y_pred = lr.predict(X_test_std)
print("Accuracy: %f" % np.mean(y_pred == y_test))


# %%
# TODO: Fit the logistic regression model with L2 regularization using scikit-learn. Use the following parameters:
# - penalty="l2" # The penalty term is used to prevent overfitting. The "l2" means L2 regularization
# - C = 2.0 # The inverse of regularization strength. Smaller values cause stronger regularization
# - solver = "saga"
# - multi_class="ovr"
# - random_state=42
lr_reg = ...

# %% Evaluate the accuracy of the prediction for the test data
y_pred = lr_reg.predict(X_test_std)
print("Accuracy: %f" % np.mean(y_pred == y_test))