import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

#Load dataset
iris = load_iris()
X = iris.data
y = iris.target
species = iris.target_names

#Feature names for reference
feature_names = iris.feature_names

#Scatter Plot (Sepal Length vs Sepal Width)
plt.figure()
for i in range(3):
    plt.scatter(X[y == i, 0],  #sepal length
        X[y == i, 1],  #sepal width
        label=species[i])

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Width by Species")
plt.legend()
plt.show()

#Scatter Plot (Petal Length vs Petal Width)
plt.figure()
for i in range(3):
    plt.scatter(
        X[y == i, 2],  #petal length
        X[y == i, 3],  #petal width
        label=species[i])

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Width by Species")
plt.legend()
plt.show()

#Bar Chart (Species Petal Lengths)
#Extract petal lengths (column index 2)
petal_lengths = X[:, 2]

#Compute average petal length for each species
avg_petal_lengths = [np.mean(petal_lengths[y == i]) for i in range(3)]

#Create bar chart
plt.figure()
plt.bar(species, avg_petal_lengths)

plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.title("Average Petal Length by Iris Species")

plt.show()

import pandas as pd

#Load dataset in pandas
df = pd.read_csv('LoanDataset - LoansDatasest.csv')

# Clean currency columns (remove £ and commas)
df['loan_amnt'] = df['loan_amnt'].replace('[£,]', '', regex=True).astype(float)
df['loan_int_rate'] = pd.to_numeric(df['loan_int_rate'], errors='coerce')
df['customer_income'] = df['customer_income'].replace('[£,]', '', regex=True).astype(float)
df['customer_age'] = pd.to_numeric(df['customer_age'], errors='coerce')

#Bar chart past default loans vs current loan status:
#Create count table
counts = pd.crosstab(df['historical_default'], df['Current_loan_status']) #

percentages = counts.div(counts.sum(axis=1), axis=0)

percentages.plot(kind='bar', stacked=True)

plt.xlabel('Historical Default')
plt.ylabel('Proportion')
plt.title('Proportion of Loan Status by Historical Default')
plt.legend(title='Current Loan Status')
plt.show()

#Bar graph: loan intent vs average loan amount
avg_loan_by_intent = df.groupby('loan_intent')['loan_amnt'].mean()

plt.figure()
avg_loan_by_intent.plot(kind='bar')
plt.xlabel('Loan Intent')
plt.ylabel('Average Loan Amount')
plt.title('Average Loan Amount by Loan Intent')
plt.show()

#Histogram: credit history and loan status
# Ensure numeric
df['customer_age'] = pd.to_numeric(df['customer_age'], errors='coerce')
df['cred_hist_length'] = pd.to_numeric(df['cred_hist_length'], errors='coerce')

#Scatter plot
plt.figure()
plt.scatter(df['customer_age'], df['cred_hist_length'])

plt.xlabel('Customer Age')
plt.ylabel('Credit History Length')
plt.title('Customer Age vs Credit History Length')

plt.show()

#Drop missing values
clean_df = df[['customer_age', 'cred_hist_length']].dropna()

x = clean_df['customer_age']
y = clean_df['cred_hist_length']

#Fit line
m, b = np.polyfit(x, y, 1)

plt.figure()
plt.scatter(x, y)
plt.plot(x, m*x + b)

plt.xlabel('Customer Age')
plt.ylabel('Credit History Length')
plt.title('Customer Age vs Credit History Length with Trendline')

plt.show()

#Key Takeaways: Loan status and historical defaults do not have a relationship, contradictory to intuitive belief.
#The stacked bar chart shows most current defaults are not with individuals who have past defaults.
#Loan amount does not vary much according to loan intent. All loan intents are similar in amounts when on the same scale.
#Customer age and credit history have a strong positive relationship, with a few outliers. Most people begin earning credit
#around 20. Also, in older age groups, credit history length varies more than younger age groups. 