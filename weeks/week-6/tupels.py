def sum_numbers(tupel_of_numbers: tuple) -> int:
    """Returns the sum of all numbers in the tuple."""
    total = 0
    for num in tupel_of_numbers:
        total += num
    return total
    

def maximum_number(tupel_of_numbers: tuple) -> int:
    """Returns the maximum number in the tuple."""
    if tupel_of_numbers:
        max_num = tupel_of_numbers[0]
        for num in tupel_of_numbers:
            if num > max_num:
                max_num = num
        return max_num 
    else:
        return None    
    


def amount_of_value_in_tuple(v: object, tupel_of_values: tuple) -> int:
    """Returns the count of how many times the value appears in the tuple."""
    count = 0
    for value in tupel_of_values:
        if value == v:
            count += 1
    return count


def reverse_tuple(tupel_of_values: tuple) -> tuple:
    """Returns a new tuple with the values in reverse order."""
    reversed_tuple = ()
    for index in range(len(tupel_of_values)-1, -1, -1):
        reversed_tuple += (tupel_of_values[index],)
    return reversed_tuple


def swap_pairs(tuple_numbrs: tuple) -> tuple:
    new_tupel_numbers = ()
    for i in range (1, len(tuple_numbrs),2):
        new_tupel_numbers += tuple_numbrs[i], tuple_numbrs[i-1]
    return new_tupel_numbers    
    

print(swap_pairs( (1, 2, 3, 4, 5, 6)))

def min_max_tuple_numbers(tuple_number: tuple) -> int:
    min_element = tuple_number[0]
    max_elment = tuple_number[0]
    for val in tuple_number:
        if val > max_elment:
            max_elment = val
        elif val < min_element:
            min_element = val
    return min_element, max_elment  


print(min_max_tuple_numbers((4, 1, 7, 3, 5)))


def merge_and_sort(tuple1: tuple, tuple2: tuple):
    lst = list(tuple1 + tuple2)
    
    i = 1
    while i < len(lst):
        if lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i = 1  
        else:
            i += 1
            
    return tuple(lst)

print(merge_and_sort((3, 1, 4), (1, 5, 9)))




def frequency_table(tuple_item: tuple) -> tuple:
    lst = []
    for item in tuple_item:
        tuple_count = (item, amount_of_value_in_tuple(item, tuple_item))
        if tuple_count in lst:
            continue
        else:
            lst.append(tuple_count)
            
    return tuple(lst)  

def rotate_tuple(t: tuple, k: int) -> tuple:
    if not t:  
        return t
    
    n = len(t)
    k = k % n 
    
    return t[-k:] + t[:-k]








   
