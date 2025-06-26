# Something fishy there - 
# Find output of following:
# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l) 

# f(2)
# f(3,[3,2,1])
# f(3)

def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    
    print(l)

f(2)            # output: [0,1]
f(3, [3,2,1])   # output: [3,2,1,0,1,4]
f(3)            # output: [0,1,0,1,4] => Not something expected, 
'''As here 'l' is a default argument and it will be created only once in the whole program execution and
that is when the function is defined. Each time it is modified, it will be changed in the same context and because 
it is mutable, it will retain the changes, hence in last function call here, the list has been changed in 
the first call and for the last function call l's initial value will be [0,1] which will be used for the 
function call execution of f(3)'''