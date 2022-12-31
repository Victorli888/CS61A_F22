a = [1,2,3]
b = [7,8,9]
c = [a,4,5,6,b]

# How would you flatten a such that it is now a pure list
def flatten(s):

    # write out your base case
    print(f"Flattening...")
    if not s:
        print(f"I am not s {s}")
        return []
    elif type(s[0]) is list:
        print(f"{s[0]} & {s[1:]}")
        return flatten(s[0]) + flatten(s[1:])
    else:
        print(f"{s[0]} & {s[1:]}")
        return [s[0]] + flatten(s[1:])


print(flatten(c))