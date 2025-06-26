# Every other sub-list
# Given a list and 2 indices as input, 
# return the sub-list enclosed within these 2 indices. It should contain every second element.
# E.g.
# Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
# Return [5, 11, 17, 23]

def list_slice(list, start, end):
    return list[start: end+1: 2]

arr = []
start = 0
end = 0

try:
    arr = list(map(int, input("Enter space separated numbers: ").split()))
    start = int(input("Enter the starting index: "))
    end = int(input("Enter the ending index(inclusive): "))
except:
    print("Please provide valid input. Exiting...")
    exit(1)

if(start > end or start < 0 or end >= len(arr)):
    print("Provided starting and ending indexes are invalid. Exiting...")
    exit(1)

print("Sliced list:", list_slice(arr, start, end))