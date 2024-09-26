''' 
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#

# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.
'''


# Trial data to test my function
trial_data=[{'user': 'john', \
            'jobs': ['analyst', 'engineer']},
            {'user': 'jane', \
            'jobs': []}]

# Defining the has_experience_as function:
def has_experience_as(cv_list, job_title):
    # Creating an empty list called result.
    result = []
    # Checking the dtypes of the inputs.
    if isinstance(cv_list, list) and isinstance(job_title, str):
        # looping through cv_list to access each dictionary.
        for cv in cv_list:
            # Checking if there a non-empty value associated to the key 'jobs'.
            # Making sure my iterable corresponds to a dict.
            if cv['jobs'] != [] and type(cv) == dict :
                # Adding the value of the 'user' key to my result list.
                result.append(cv['user'])
                # Returning my list with all 'users' with non-empty values in 'jobs' added.
        return(result)
    # Raising an error if you didn't input the right dtype.
    else:
        raise Exception('you input the wrong data type.')
        
# Testing the Function.
test = has_experience_as(trial_data, 'enginieer')
print(test)


'''
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.
'''

# Trial data to test my function
trial_data3 = [
    {'user': 'john', 'jobs': ['analyst', 'engineer']},
    {'user': 'jane', 'jobs': ['finance', 'engineer']},
    {'user': 'george', 'jobs': ['analyst', 'developer']},
]

# Defining the job_counts function.
def job_counts(cv_list):
    # Creating an empty dict to store job:count key and values.
    dict_counter = {}
    # Looping throught my input cv_list, my iterable will be a dict.
    for cv in cv_list:
        # Looping throught each value 'jobs'
        for job in cv['jobs']:
            # Adding a +1 to the count if the value is in dict_counter, else creating an entry in dict_counter with value 1.
            if job in dict_counter:
                dict_counter[job] += 1
            else:
                dict_counter[job] = 1
                # Returning my dict_counter.
    return dict_counter

# Trying my function
result = job_counts(trial_data3)
print(result)


# You can also do it using a List and dict comprenhension.
def job_count(cv_list):
    # Getting a list with all the jobs.
    jobs_list = [job for cv in cv_list for job in cv['jobs']]
    # Creating a dictionary that has job:count pairs for the list created before.
    job_counter = {job: jobs_list.count(job) for job in jobs_list}
    
    return job_counter

# Trying my function:
job_count(trial_data3)



# You can also do it more efficiently using the Counter class from the collections library:
from collections import Counter

def job_counts(cv_list):
    dict_counter = Counter()
    
    # Iterate through each CV and update the counter with the jobs
    for cv in cv_list:
        dict_counter.update(cv['jobs'])
    
    return dict_counter

'''
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.
'''

# Defining most_popular_job function.
def most_popular_job(cv_list):
    # Using the job_counts function to get a dict with job:count pairs.
    counter = job_counts(cv_list)
    # Finding the max of the values of the counter dict.
    max_value = max(counter.values())
    # Using a list-Comprenhension to create a list with the keys related to the max value found in the dict counter.
    max_keys = [key for key, value in counter.items() if value == max_value]
    # Returning a tuple with a list of keys that match my max value. The list is transformed into a string because is what the exercise ask to do.
    return (str(max_keys), max_value)

# Trying my function
keys, value = most_popular_job(trial_data3)
print(f"The highest count job is: {keys} with a count of {value} ")