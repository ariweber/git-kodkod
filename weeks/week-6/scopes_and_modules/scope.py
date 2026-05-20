#  Counter with global. Write a function bump() that increments a module-level variable count by 1,
# and a function value() that returns its current value. After three calls to bump(), value() should
# return 3



from marshal import dump


count = 0

def bump():
    global count
    count += 1

def value():
    global count
    return count


