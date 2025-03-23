import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load dataset
df = pd.read_csv("/mnt/data/diabetes.csv")

# Display basic info and first few rows
print("Dataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Descriptive statistics
desc_stats = df.describe().T
print("\nDescriptive Statistics:")
print(desc_stats)

# Calculate mode for each column
modes = df.mode().iloc[0]
print("\nMode for each column:")
print(modes)

# Calculate skewness and kurtosis for each column
skewness = df.skew()
kurtosis = df.kurtosis()
print("\nSkewness of each column:")
print(skewness)
print("\nKurtosis of each column:")
print(kurtosis)

# Correlation matrix
corr_matrix = df.corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

# Hypothesis Testing: t-test for Glucose levels between Outcome groups
group0 = df[df['Outcome'] == 0]['Glucose']
group1 = df[df['Outcome'] == 1]['Glucose']
t_stat, p_val = stats.ttest_ind(group0, group1, nan_policy='omit')
print("\nT-test for Glucose levels between Outcome groups:")
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.4f}")

# Visualization 1: Histograms for each variable
df.hist(bins=20, figsize=(15, 10))
plt.tight_layout()
plt.suptitle("Histograms of Diabetes Dataset Features", y=1.02)
plt.show()

# Visualization 2: Boxplots for each feature by Outcome
plt.figure(figsize=(15, 10))
for idx, col in enumerate(df.columns[:-1], 1):  # Excluding Outcome
    plt.subplot(3, 3, idx)
    sns.boxplot(x='Outcome', y=col, data=df)
    plt.title(f"{col} by Outcome")
plt.tight_layout()
plt.suptitle("Boxplots of Features by Outcome", y=1.02)
plt.show()

# Visualization 3: Scatterplot Matrix (Pairplot) for a subset of features
# (Using a subset to avoid memory issues)
features_subset = ["Glucose", "BMI", "Age", "Pregnancies"]
sns.pairplot(df[features_subset + ["Outcome"]], hue="Outcome", diag_kind="hist")
plt.suptitle("Scatterplot Matrix (Pairplot) for Selected Features", y=1.02)
plt.show()

# Visualization 4: Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Visualization 5: KDE Plot for Glucose Distribution by Outcome
plt.figure(figsize=(8, 6))
sns.kdeplot(data=df, x="Glucose", hue="Outcome", fill=True)
plt.title("Distribution of Glucose Levels by Outcome")
plt.show()
