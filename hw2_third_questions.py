##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

# Parameters of the function: 1) a dictionary with the weekly case data, 2) the name of the country
def total_registered_cases(data, country):
    # if the country exists in the dictionary, the function will sum all cases in the specified country
    if country in data:
        return sum(data[country])
    # if the country doesn´t exists in the dictionary, the function will return a message
    else: 
        return f"{country} doesn´t exists in the data"

data = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}
# Example for Spain:
total_registered_cases(data, "Spain")

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had.

# Parameters of the function: 1) The data structure described above.
def total_registered_cases_per_country(data):
    # Creation of an empty dictionary to store the total number of cases per country.
    total_cases_per_country = {}
    # Iterate over each country (key) and its list of cases (value)
    for country, cases in data.items():
        # Add the list of cases to obtain the total number of registered cases per country
        total_cases_per_country[country] = sum(cases)
    # The function will return the new dictionary with the total number of cases per country
    return total_cases_per_country
total_registered_cases_per_country(data)

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

# Parameters of the function: 1) The data structure described above.
def country_with_most_cases(data):
    # Create variables to store the maximum number of cases and the country with the higher number of cases
    cases_max = 0
    country_max = "xxx"
    # As Ex 8), iterate over each country (key) and its list of cases (value)
    for country, cases in data.items():
        # Add the list of cases to obtain the total cases
        total_cases = sum(cases)
        # Compare if the current total number of cases is greater than the maximum recorded
        if total_cases > cases_max:
            cases_max = total_cases 
            # If this happens, the new variable for the country will be replaced with the name of the respective country
            country_max = country
    # The function will return the country with most covid cases
    return country_max
