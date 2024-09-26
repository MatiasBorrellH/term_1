##Ex 7
def total_registered_cases(data, country):
    for country in data:
        return sum(data[country])
data = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}
total_registered_cases(data, "Spain")

##Ex 8
def total_registered_cases_per_country(data):
    total_cases_by_country = {}
    for country, cases in data.items():
        total_cases_by_country[country] = sum(cases)
    return total_cases_by_country
total_registered_cases_per_country(data)

##Ex 9:
def country_with_most_cases(data):
    return data