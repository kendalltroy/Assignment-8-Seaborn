# Assignment-8-Seaborn
# Purpose
Uses Python, Seaborn,  and Pandas for two datasets: elementary exercise data and Seaborn's built-in planet dataset. This program demonstrates different plot types across both datasets to uncover patterns visually.

# Classes
Neither project uses custom classes; they are built-in by Seaborn and Python. The main class is a Pandas DataFrame which is utilized to organize datasets for nice visualizations. Attributes include the following:
Exercise data:
id — unique student identifier (integer)
1 min — pulse rate 1 minute into exercise (integer, bpm)
15 min — pulse rate 15 minutes into exercise (integer, bpm)
30 min — pulse rate 30 minutes into exercise (integer, bpm)
diet — student's diet type: low fat or no fat (string)
kind — type of exercise performed: rest, walking, or running (string)

Planet data: 
method — detection method used to discover the planet (string)
number — number of planets discovered in the system (integer)
orbital_period — time for the planet to orbit its star in days (float)
mass — planet mass relative to Jupiter (float)
distance — distance from Earth in light years (float)
year — year the planet was discovered (integer)

# Methods: 
Data Cleaning and Loading: 
pd.read_csv() — loads the exercise CSV file into a DataFrame
sns.load_dataset() — downloads and loads the built-in planets dataset
df.dropna() — removes rows with missing values before plotting
df.rename() — renames columns to cleaner display-friendly labels
df.melt() — reshapes the exercise DataFrame from wide to long format so Seaborn can read it properly
df.groupby() — groups planet data by year and method to count annual discoveries
df.value_counts() — counts how many planets were found by each detection method

Plotting: 
sns.scatterplot() — relational plot showing orbital period vs. planet mass
sns.lineplot() — relational plot showing discovery counts over time
sns.histplot() — distribution plots for orbital period and planet mass
sns.heatmap() — shows all student pulse values across three time points
sns.boxplot() — shows pulse distribution by exercise type and diet
sns.stripplot() — overlays individual data points on top of the boxplot
sns.barplot() — categorical plots for planet discovery counts and average orbital period

Formatting: 
ax.set_title() — sets the plot title
ax.set_xlabel() / ax.set_ylabel() — labels the axes
ax.set_xscale('log') / ax.set_yscale('log') — applies log scale for skewed data
ax.legend() — adds and customizes the legend
ax.grid() — adds reference grid lines
ax.tick_params() — rotates or adjusts axis tick labels
plt.tight_layout() — prevents labels and titles from overlapping
plt.show() — renders and displays each plot

# Limitations:
1. Missing values are dropped using dropna() and are not estimated. This may reduce sample size for some plots.
2. Exercise data is small, so visualizations might not be fully representative
