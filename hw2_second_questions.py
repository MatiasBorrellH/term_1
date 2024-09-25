#### Exercise 4

def has_experience_as(cvs, job_title):
    """Takes parameters "A list of CV's", "A string (job_title)",
    returns a list of strings representing the usernames of every user
    that has worked as job_title."""
    
    usernames = []
    for cv in cvs:
        if job_title in cvs['jobs']:
            usernames.append(cv['user'])
    return usernames
cvs =[{'user': 'john',
       'jobs': ['analyst', 'engineer']},
      {'user': 'jane',
       'jobs': ['finance', 'software']}]
has_experience_as(cvs, "finance")

#### Exercise 5
def job_counts(cvs):
    job_count = {}
