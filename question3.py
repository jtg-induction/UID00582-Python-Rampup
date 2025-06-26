# Question: Given a list of dicts, write a program to sort the list according to a key given in input.
# E.g. 
# Input f([
#     {"fruit": "orange", "color": "orange"},
#     {"fruit": "apple", "color": "red"},
#     {"fruit": "banana", "color": "yellow"},
#     {"fruit": "blueberry", "color": "blue"}
# ], "fruit")
# Should Output
# [
#     {"fruit": "apple", "color": "red"},
#     {"fruit": "banana", "color": "yellow"},
#     {"fruit": "blueberry", "color": "blue"},
#     {"fruit": "orange", "color": "orange"}
# ]
# AND 
# Input f([
#     {"fruit": "orange", "color": "orange"},
#     {"fruit": "apple", "color": "red"},
#     {"fruit": "banana", "color": "yellow"},
#     {"fruit": "blueberry", "color": "blue"}
# ], "color")
# Should Output
# [
#     {"fruit": "blueberry", "color": "blue"},
#     {"fruit": "orange", "color": "orange"},
#     {"fruit": "apple", "color": "red"},
#     {"fruit": "banana", "color": "yellow"}
# ]

def sort_list(list, key):
    output = []
    
    try:
        output = sorted(list, key=lambda item: item.get(key)) 
    except:
        print("Provided data is invalid")
        exit(1)

    return output

given_list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
given_key = "fruit"

print("output: ", sort_list(given_list, given_key))