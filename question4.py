# The power of one line - 
# Given a dictionary, switch position of key and values in the dict, i.e.,  The function's body shouldn't have more than one statement.
# f({
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3",
#     "key4": "value4",
#     "key5": "value5"
# }) 
# should return {
#     "value1": "key1",
#     "value2": "key2",
#     "value3": "key3",
#     "value4": "key4",
#     "value5": "key5"
# }

def dict_swapper(dict):
    # Dictionary Comprehension
    return {value: key for key,value in dict.items()}

dict = {}
dict['key1'] = "value1"
dict['key2'] = "value2"
dict['key3'] = "value3"
dict['key4'] = "value4"
dict['key5'] = "value5"

print("Swapped dictionary: ", dict_swapper(dict))
