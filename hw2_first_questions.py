'''
# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
'''
# Creating triple function
def triple(x):
    return x * 3

'''
# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
'''
# Creating substract function
def substract(a, b):
    return (b-a)

'''
# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly
'''

# Creating dictionary_maker function
def dictionary_maker(tuple_list):
    # Checking if the dtype input are list of lenght 2  
    # Checking if inside the list are tuples.
    if isinstance(tuple_list, list) and len(tuple_list) == 2 and \
        isinstance(tuple_list[0], tuple) and \
        isinstance(tuple_list[1], tuple):
            # Returning the values of the tuples in dict format.
        return {tuple_list[0][0] : tuple_list[0][1], tuple_list[1][0] : tuple_list[1][1]}
    else:
        print("You didn't input the correct data type.")
        

# Testing my function.
tuple_list1 = [('foo', 1), ('bar',3)]

result = dictionary_maker(tuple_list1)
print(result)