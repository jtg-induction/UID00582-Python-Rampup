# Looking at the below code, write down the final values of A0, A1, ...An
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# -
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
# A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
# A8 = list(map(lambda x: x*2, [1,2,3,4]))
# A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])

from functools import reduce # for A7

A0 = dict(zip(('a','b','c','d','e'), (1,2,3,4,5)))
print(A0) # A dictionary with key:value pairs key belongs to (a,b,c...) and value belongs to (1,2,3)

A1 = range(10) 
print(A1) # A range object, will look like this: range(0, 10) and represent an lazy iterable containing values from 0 to 9

A2 = sorted([i for i in A1 if i in A0]) 
print(A2)  # Empty list as i in A0 will check for keys in the dict but all dict keys are characters

A3 = sorted([A0[s] for s in A0])
print(A3) # All the values in A0 dict as 's' will be having all the keys of A0 one by one

A5 = {i:i*i for i in A1}
print(A5) # Dictionary comprehension, will provide key value pairs in dict like i:i*i where i belongs to A1

A6 = [[i, i*i] for i in A1]
print(A6) # List Comprehension, List of lists with each member list having 2 values like i,i*i where i belongs to A1

A7 = reduce(lambda x,y: x+y, [10,23,-45,33])
print(A7)  # Calculated => sum of all members of give iterable = 21

A8 = list(map(lambda x: x*2, [1,2,3,4]))
print(A8)  # list with doubles of given iterable list

A9 = filter(lambda x: len(x) > 3,["I", "want", "to", "learn", "python"])
print(A9) # filter function returns a lazy filter object or iterator, so we'll get that in A9. not any list
