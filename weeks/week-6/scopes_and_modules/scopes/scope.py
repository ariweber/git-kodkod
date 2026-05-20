#1


from numpy import inner


count = 0

def bump():
    global count
    count += 1

def value():
    global count
    return count  
#2
def make_counter():
    count = 0

    def bump():
        nonlocal count
        count += 1
        print(count)
    return bump


x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)
outer()
print(x)

# local
# enclosing
# global

lst = [1, 2, 3] #list is a built-in function, but we can reassign it to a variable
print(list(range(5)))


