#### Exercise 1

def triple(x):
    """Triples the value of x"""
    
    return x*3
print(triple(5))


#### Exercise 2
def subtract(a,b):
    """Substracts the value of b from the value of a"""
    
    return a-b
print(subtract(3,6))


#### Exercise 3
def dictionary_maker(tuple_list):
    """Takes a list of tuples and creates a dictionary"""
    
    my_dict = {}
    for key, value in tuple_list:
        my_dict[key] = value
    return my_dict

tuple_list = [(2,3), (1,2), (3,4), ("oho", "yap")]
dictionary_maker(tuple_list)