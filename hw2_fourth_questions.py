'''
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
'''


# importing pandas as pd and my data_load_func form the data_load file
from data_load import data_load_func, pd

# Loading the csv data as a dataframe into a df variable.
df = data_load_func('data\covid.csv')
# Printing the dataframe columns
print(df.columns)
# Printing the entries of the 'Country' Column
print(df['Country'])

# Creating a filtering function to find the entries that are greater than an int value in a certain column.
def filter_func (df: pd.DataFrame, df_column_name: str ,greater_than_value: int):
    df_filtered = df[(df[df_column_name] > greater_than_value)]
    return df_filtered

# Creating a ratio function that creates a new column on a copy of the original data frame with the ratio between two selected columns.
def ratio_func (df, df_column_name_1, df_column_name_2):
    df_ratio = df.copy()
    df_ratio[df_column_name_1 + '_to_' + df_column_name_2 + '_ratio'] = df_ratio[df_column_name_1] / df_ratio[df_column_name_2]
    return df_ratio

# Printing the asked results:
print(ratio_func(filter_func(df, 'Active', 500), 'Deaths', 'Confirmed'))
print(ratio_func(filter_func(df, 'Active', 1000), 'Deaths', 'Confirmed'))
print(ratio_func(filter_func(df, 'Active', 5000), 'Deaths', 'Confirmed'))



