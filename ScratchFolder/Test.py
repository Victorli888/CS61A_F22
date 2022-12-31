from operator import sub
test_input = ["ApplePie","CherryPie","PeachPie"]
b = [1,2,3]
c = [8,9]
a = [0,b,4,5,6,7,c]



print(a)
# How would you flatten a such that it is now a pure list
def flatten(s):

    # write out your base case
    print(f"Flattening...")
    if not s:
        return []
    elif type(s[0]) is list:
        return flatten(s[0]) + flatten(s[1:])
    else:
        return [s[0]] + flatten(s[1:])


print(flatten(a))