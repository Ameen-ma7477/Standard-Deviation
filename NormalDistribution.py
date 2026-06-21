import pandas as pd #used for data manipulation and analysis
import seaborn as sn #used for data visualization
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

# Print statistical summary
# print(df.height.describe())

# Create histogram with KDE curve
#sn.histplot(df.height, kde=True)

# Display the graph
#plt.show()

mean = df.height.mean()
print(mean)

std_deviation = df.height.std()
print(std_deviation)

print(mean-3*std_deviation)
print(mean+3*std_deviation)

print(df[(df.height < 54.82) | (df.height > 77.91)])

df_no_outliers = df[(df.height >= 54.82) & (df.height <= 77.91)]
print(df_no_outliers.shape)

df['Z_score'] = (df.height - df.height.mean()) / df.height.std()
print(df.head())

print(df[(df.Z_score < -3) | (df.Z_score > 3)])