# Task 1: Read datasheet
import pandas as pd
import matplotlib.pyplot as plt
LFDataOri = pd.read_csv("owid-covid-data.csv")

# Task 2: Display some appropriate information about the datasheet
print(LFDataOri.head())
print(LFDataOri.info())
print(LFDataOri.describe())
print("Data shape: ", LFDataOri.shape)

# Task 3: Processing
LFDataOri = (LFDataOri.dropna(thresh=len(LFDataOri)*0.4)
        .drop(columns=LFDataOri.columns[LFDataOri.columns.str.contains('smoothed')])
        .assign(date=pd.to_datetime(LFDataOri['date']))
        .set_index('date'))
print(LFDataOri.info())
print(LFDataOri.describe())
print("Preprocessed dataset shape: ", LFDataOri.shape)

# Task 4: Plotting
plt.rcParams['figure.figsize'] = [15, 10]

# a. Daily new cases per million on a worldwide basis
fig, axes = plt.subplots(2, 2)
LFDataOri.resample('M')['new_cases_per_million'].mean().plot(ax=axes[0, 0])
axes[0, 0].set_title('Monthly Average of New Cases per Million (Worldwide)')
LFDataOri.resample('Q')['new_cases_per_million'].sum().plot(kind='bar', ax=axes[0, 1])
axes[0, 1].set_title('Quarterly Sum of New Cases per Million (Worldwide)')

# b. Daily new deaths per million on a worldwide basis
LFDataOri.resample('M')['new_deaths_per_million'].mean().plot(ax=axes[1, 0])
axes[1, 0].set_title('Monthly Average of New Deaths per Million (Worldwide)')
LFDataOri.resample('Q')['new_deaths_per_million'].sum().plot(kind='bar', ax=axes[1, 1])
axes[1, 1].set_title('Quarterly Sum of New Deaths per Million (Worldwide)')

plt.tight_layout()
plt.show()

# c. Total cases per million on a quarterly basis
plt.figure()
LFDataOri.resample('Q')['total_cases_per_million'].sum().plot(kind='bar')
plt.title('Quarterly Sum of Total Cases per Million (Worldwide)')

# d. Total deaths per million on a quarterly basis
plt.figure()
LFDataOri.resample('Q')['total_deaths_per_million'].sum().plot(kind='bar')
plt.title('Quarterly Sum of Total Deaths per Million (Worldwide)')

# Task 5: Country-wise daily development of new cases per million
countries = ['USA', 'India', 'Brazil', 'Russia', 'France', 'China']
df_countries = (LFDataOri[LFDataOri['iso_code'].isin(countries)]
                .pivot_table(index='date', columns='iso_code', values='new_cases_per_million'))
df_countries.plot()
plt.title('Daily Development of New Cases per Million')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

# Task 6:
# a. Group by iso_code and continent
grouped_by_continent = LFDataOri.groupby('continent')

# Calculate daily new cases per million for each continent
new_cases_per_million_by_continent = grouped_by_continent['new_cases_per_million'].sum()

# Plot the data
plt.figure()
new_cases_per_million_by_continent.plot(kind='bar', figsize=(10, 6))
plt.title('Daily New Cases per Million by Continent')
plt.xlabel('Continent')
plt.ylabel('New Cases per Million')

# b. Calculate total cases per million for each continent
total_cases_per_million_by_continent = grouped_by_continent['total_cases_per_million'].sum()

# Plot the data
plt
