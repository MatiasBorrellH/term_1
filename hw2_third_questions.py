'''
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
'''


# Trial data to test the function.
trial_dict ={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
            'Italy': [6, 8, 1, 7]}

# Defining my function.
def total_registered_cases(covid_dict: dict, country_name: str):
    # Checking if the country is inside my dict
    if country_name in covid_dict:
        # Doing a sum of each element of the list related to the country_name key value.
        total = sum(covid_dict[country_name])
        return total
    # Raising a message if the country is not inside the dictionary.
    else:
        print('Try with another country.')


# Testing my function
total_registered_cases(trial_dict, 'Spain')

'''
# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#
'''

# Creating total_registered_cases_per_country function
def total_registered_cases_per_country(covid_dict):
    # Creating a blank dictionary to store each pair of country:total_number_of_cases
    sum_list = {}
    # Looping inside my covid_dict, my iterable entry is a key value.
    for entry in covid_dict:
        # Adding entries to my dict sum_list with each Country:sum_of_cases pair.
        sum_list[entry] = sum(covid_dict[entry])
        # Doing a lambda function to return the entries of sum_list sorted by value.
    return dict(sorted(sum_list.items(), key=lambda item: item[1], reverse=True))

# Testing my function.
total_registered_cases_per_country(trial_dict)

'''
#9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases
'''

# Defining country_with_most_cases function.
def country_with_most_cases(covid_dict):
    # creating sum_dict using the last total_registered_cases_per_country function.
    sum_dict = total_registered_cases_per_country(covid_dict)
    # Finding the entry with the max value using a lambda function.
    max_entry = max(sum_dict.items(), key=lambda item: item[1])
    # Returning the entry with the max value.
    return max_entry

# Testing my function.
country_with_most_cases(trial_dict)