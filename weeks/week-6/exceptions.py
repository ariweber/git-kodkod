from sys import exception

#1
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None 

#2    
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"
#3    
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing" 

#4
def  parse_ints(values):
    int_values = []
    for v in values:
        try:
            int_values.append(int(v))
        except ValueError:
            continue
    return int_values 

#5
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError("Age cannot be negative")
    return age

#6
def  retry(func, n):
    for i in range(n):
        try:
            return func()
        except Exception as e:
            last_exception = e
    raise last_exception

#7        
def count_errors(funcs):
    count_error = 0
    for func in funcs:
        try:
            func()
        except Exception:
            count_error += 1
    return count_error

#8
def load_config(path):
    try:
        with open(path, 'r') as f:
            line = f.readline()
            data = int(line)
            return data
    except:
        raise RuntimeError ("Failed to load config") from exception






        
