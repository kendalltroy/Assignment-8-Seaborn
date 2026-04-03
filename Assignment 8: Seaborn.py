import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np
#Question 1
#Load data
df = pd.read_csv('Exercise_Data.csv')

#Rename columns for clarity
df.rename(columns={'1 min': '1 Min', '15 min': '15 Min', '30 min': '30 Min',
                   'diet': 'Diet', 'kind': 'Exercise Type'}, inplace=True)


# Create a heatmap:
pulse_cols = ['1 Min', '15 Min', '30 Min'] #identify pulse columns
heatmap_data = df[['id'] + pulse_cols].set_index('id') #combines pulse columns based on unique id names

fig1, ax1 = plt.subplots(figsize=(8, 10)) #sets figure size and configurations

#creates heatmap with heatmap data with proper labels and cbar
sns.heatmap(
    heatmap_data,
    ax=ax1,
    cmap='YlOrRd',
    annot=True,
    fmt='d',
    linewidths=0.5,
    linecolor='white',
    cbar_kws={'label': 'Pulse (bpm)', 'shrink': 0.6}
)

#sets title, labels, and parameters
ax1.set_title('Student Pulse Rates at 1, 15, and 30 Minutes\nDuring Exercise Session',
              fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Time Point', fontsize=12)
ax1.set_ylabel('Student ID', fontsize=12)
ax1.tick_params(axis='x', rotation=0)
ax1.tick_params(axis='y', rotation=0)

plt.tight_layout()
plt.show()

# Categorical plot

#sets 1 min, 15 min, and 30 min into a single column with their own values for each unique id
df_long = df.melt(
    id_vars=['id', 'Diet', 'Exercise Type'],
    value_vars=pulse_cols,
    var_name='Time Point',
    value_name='Pulse (bpm)'
)

# sets colors
palette = {'low fat': '#4C9BE8', 'no fat': '#E8844C'}

# sets proper order of exercises
exercise_order = ['rest', 'walking', 'running']

# sets figure dimensions and title
fig2, axes = plt.subplots(1, 3, figsize=(14, 6), sharey=True)
fig2.suptitle('Pulse Values by Diet and Exercise Type\nAcross Time Points',
              fontsize=15, fontweight='bold', y=1.02)

#handles data per its respective timeframe
for ax, time_point in zip(axes, pulse_cols):
    subset = df_long[df_long['Time Point'] == time_point] #filters rows to match the current timeframe

#creates a box and whiskers plot with parameters: exercise, diet, exercise order (rest, walking, running)
    sns.boxplot(
        data=subset,
        x='Exercise Type', y='Pulse (bpm)',
        hue='Diet',
        order=exercise_order,
        palette=palette,
        width=0.5,
        linewidth=1.2,
        fliersize=0, #hides outlier dots
        ax=ax
    )
    #shows individual points on top of the box-and-whisker plot
    sns.stripplot(
        data=subset,
        x='Exercise Type', y='Pulse (bpm)',
        hue='Diet',
        order=exercise_order,
        palette=palette,
        dodge=True,
        size=6,
        alpha=0.75,
        linewidth=0.5,
        edgecolor='white',
        ax=ax,
        legend=False #suppresses legend due to a pre-existing one from the box-and-whiskers plot
    )

#exis label formatting
    ax.set_title(f'{time_point}', fontsize=12, fontweight='bold')
    ax.set_xlabel('Exercise Type', fontsize=11)
    ax.set_ylabel('Pulse (bpm)' if ax == axes[0] else '', fontsize=11)
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax.grid(axis='y', linestyle='--', alpha=0.4)

#ensures only 1 legend is created for the whole visualization, not one per panel
    if ax != axes[-1]:
        ax.get_legend().remove()
    else:
        legend = ax.get_legend()
        legend.set_title('Diet')
        legend.get_frame().set_alpha(0.85)

plt.tight_layout()
plt.show()

#Brief insights:
#Heat map:
#The majority of students remain steady throughout the different timeframes. About a third found an increase in bpm around the 15 minute mark.
# those sames students continued to have an increased bpm until the 30 minute mark. This could be due to several reasons.
# The main reason being simply what students were doing what exercise. For example, perhaps only about a third of the students were running while the rest were moving slower or not at all.
#Box Plot:
# By the 30 minute mark, there is a clear difference between the students who are walking/resting and those who are running.
# In fact, even in the diets, there is a large difference as well. Students that are fat-free consistently have higher bpm despite the exercise.
# Additionally, bpm doesn't increase much when resting versus walking. However, bpm sky rocket when running.
# This could mean that running is more efficient when training cardiovascular health than walking.

# Question 2
# Load built-in planets dataset
planets = sns.load_dataset('planets')
# Relational Plot 1: Orbital Period vs. Planet Mass by Detection Method
#configures size
fig1, ax1 = plt.subplots(figsize=(9, 6))

#drops null values and creates x and y data
sns.scatterplot(
    data=planets.dropna(subset=['mass', 'orbital_period']),
    x='mass',
    y='orbital_period',
    hue='method',
    alpha=0.7,
    s=70,
    ax=ax1
)

#configures titles, labels, and legend
ax1.set_title("Orbital Period vs. Planet Mass by Detection Method", fontsize=14, fontweight='bold')
ax1.set_xlabel("Planet Mass (Jupiter Masses)", fontsize=12)
ax1.set_ylabel("Orbital Period (days)", fontsize=12)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend(title='Detection Method', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
ax1.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

# Relational Plot 2: Number of Discoveries per Year by Detection Method
#groups planets discovery methods by year
discoveries_per_year = (
    planets.groupby(['year', 'method'])
    .size()
    .reset_index(name='count')
)
#configures plot dimensions
fig2, ax2 = plt.subplots(figsize=(11, 6))

#sets data for line plot
sns.lineplot(
    data=discoveries_per_year,
    x='year',
    y='count',
    hue='method',
    marker='o',
    markersize=5,
    linewidth=1.8,
    ax=ax2
)

#sets titles and lables
ax2.set_title("Number of Exoplanet Discoveries per Year by Detection Method", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Number of Discoveries", fontsize=12)
ax2.legend(title='Detection Method', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=8)
ax2.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

# Distribution Plot 1: Histogram of Orbital Period
fig3, ax3 = plt.subplots(figsize=(9, 6))

#creates histogram, drops null values, and sets data
sns.histplot(
    data=planets.dropna(subset=['orbital_period']),
    x='orbital_period',
    bins=40,
    color='steelblue',
    edgecolor='white',
    ax=ax3
)

#configures title and labels
ax3.set_title("Distribution of Exoplanet Orbital Periods", fontsize=14, fontweight='bold')
ax3.set_xlabel("Orbital Period (days, log scale)", fontsize=12)
ax3.set_ylabel("Number of Planets", fontsize=12)
ax3.set_xscale('log')
ax3.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

# Distribution Plot 2: Histogram of Planet Mass by Detection Method (top 4 methods)
#determines top methods and planets by greatest value counts
top_methods = planets['method'].value_counts().nlargest(4).index
planets_top = planets[planets['method'].isin(top_methods)].dropna(subset=['mass'])

fig4, ax4 = plt.subplots(figsize=(9, 6))

#creates histogram with proper data (top planets) and x values (by mass)
sns.histplot(
    data=planets_top,
    x='mass',
    hue='method',
    bins=30,
    multiple='stack',
    edgecolor='white',
    ax=ax4
)

#sets proper title and labels
ax4.set_title("Distribution of Planet Mass by Detection Method\n(Top 4 Methods)", fontsize=14, fontweight='bold')
ax4.set_xlabel("Planet Mass (Jupiter Masses, log scale)", fontsize=12)
ax4.set_ylabel("Number of Planets", fontsize=12)
ax4.set_xscale('log')
ax4.legend(title='Detection Method', fontsize=9)
ax4.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

# Categorical Plot 1: Total Discoveries by Detection Method
# counts all methods by number of appearance
method_counts = planets['method'].value_counts().reset_index()
method_counts.columns = ['method', 'count']

fig5, ax5 = plt.subplots(figsize=(10, 6))
#sets barplot with data as number of methods on x-axis and their count as the y-axis
sns.barplot(
    data=method_counts,
    x='method',
    y='count',
    palette='viridis',
    edgecolor='white',
    ax=ax5
)

#sets title and labels
ax5.set_title("Total Exoplanet Discoveries by Detection Method", fontsize=14, fontweight='bold')
ax5.set_xlabel("Detection Method", fontsize=12)
ax5.set_ylabel("Number of Planets Discovered", fontsize=12)
ax5.tick_params(axis='x', rotation=30)
ax5.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

# Categorical Plot 2: Average Orbital Period by Detection Method
fig6, ax6 = plt.subplots(figsize=(10, 6))

#creates barplot with methods on x-axis and orbital period on y-axis
sns.barplot(
    data=planets.dropna(subset=['orbital_period']),
    x='method',
    y='orbital_period',
    palette='magma',
    edgecolor='white',
    errorbar='sd',
    capsize=0.1,
    ax=ax6
)
#sets titles and labels
ax6.set_title("Average Orbital Period by Detection Method\n(with Standard Deviation)", fontsize=14, fontweight='bold')
ax6.set_xlabel("Detection Method", fontsize=12)
ax6.set_ylabel("Average Orbital Period (days)", fontsize=12)
ax6.tick_params(axis='x', rotation=30)
ax6.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

#I think the scatter plot by planet mass, orbital period, and detection method is the most effective.
#This is due to the amount of information that is communicated in just one visualization.
#For instance, it is quickly seen that most planets are discovered by Radial Velocity.
# The graph also clearly shows a positive relationship between planet mass and the length of orbital periods.