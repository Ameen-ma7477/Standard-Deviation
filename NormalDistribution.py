import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("heights.csv")

# Basic statistics
mean_height = df["height"].mean()
std_height = df["height"].std()

print(f"Mean Height: {mean_height:.2f}")
print(f"Standard Deviation: {std_height:.2f}")

# Calculate 3-sigma boundaries
lower_limit = mean_height - (3 * std_height)
upper_limit = mean_height + (3 * std_height)

print(f"\nLower Limit: {lower_limit:.2f}")
print(f"Upper Limit: {upper_limit:.2f}")

# Detect outliers using the 3-sigma rule
outliers = df[(df["height"] < lower_limit) | (df["height"] > upper_limit)]

print("\nOutliers:")
print(outliers)

# Remove outliers
df_clean = df[
    (df["height"] >= lower_limit) &
    (df["height"] <= upper_limit)
]

print(f"\nDataset Shape After Removing Outliers: {df_clean.shape}")

# Calculate Z-score
df["z_score"] = (
    (df["height"] - mean_height) / std_height
)

print("\nDataset with Z-Score:")
print(df.head())

# Detect outliers using Z-score
z_score_outliers = df[
    (df["z_score"] < -3) |
    (df["z_score"] > 3)
]

print("\nZ-Score Outliers:")
print(z_score_outliers)

# Visualize distribution
sns.histplot(df["height"], kde=True)

plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")

plt.show()
