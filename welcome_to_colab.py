

! pip install streamlit

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset (preloaded in seaborn)
iris = sns.load_dataset('iris')

# Display the first few rows of the dataset
print(iris.head())

# Basic statistical description
print(iris.describe())

# Visualize the data
# Pairplot of features colored by species
sns.pairplot(iris, hue='species', diag_kind='kde')
plt.suptitle('Iris Dataset Pairplot', y=1.02)

# Show plot
plt.show()

# Visualize the distribution of sepal length with respect to species
plt.figure(figsize=(10,6))
sns.boxplot(x='species', y='sepal_length', data=iris)
plt.title('Sepal Length Distribution by Species')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(iris.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Iris Dataset')
plt.show()
