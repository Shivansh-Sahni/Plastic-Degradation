# -*- coding: utf-8 -*-
"""PlasticDB Microorganism Scikit-Learn Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18nxhnImZJR_xIXeI8TeFPvXKffdPiO4t
"""

!pip install pandas scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# Load the dataset
degraders_df = pd.read_csv('/content/degraders_list.tsv', sep='\t')

# Select relevant columns and drop missing values
df = degraders_df[['Sequence', 'Degradation extrapolated from enzyme']].dropna()

# Convert the target variable to binary (Yes/No -> 1/0)
df['Degradation'] = df['Degradation extrapolated from enzyme'].apply(lambda x: 1 if x == 'Yes' else 0)

# Use CountVectorizer to transform sequences into features
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 4))
X = vectorizer.fit_transform(df['Sequence'])

# Encode the target variable
y = df['Degradation'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier

# Initialize and train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Display the results
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")