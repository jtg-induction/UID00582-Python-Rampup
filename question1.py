# Question: Implement selection sort algorithm in python. 
#           The function accepts a list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]


# Function to impolement selection sort
def selection_sort(arr): 
    size = len(arr)

    # Logic of selection sort
    for i in range(size):

        # Assume the current element is the smallest in the list
        min_index = i

        # Find the minimum element in the remaining list
        for j in range(i+1, size):
            if(arr[j] < arr[min_index]):
                min_index = j

        # We have the minimum element now, swap it with the previously assumed minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # return the sorted array
    return arr


# Code to take input and provide the output
arr = None
try:
    arr = list(map(int, input("Enter the list of numbers space separated: ").split()))
except:
    print("Please provide the integers in proper format. Exiting...")
    exit(1)

sorted_arr = selection_sort(arr)
print("Sorted array: ", sorted_arr)
