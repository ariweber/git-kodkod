def sum_numbers(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        total += num
    return total

def maximum_number(list_of_numbers):
    if list_of_numbers:
        max_num = list_of_numbers[0]
        for num in list_of_numbers:
            if num > max_num:
                max_num = num
        return max_num 
    else:
        return None


def amount_of_value_in_list(value, list_of_values):
    count = 0
    for v in list_of_values:
        if v == value:
            count += 1
    return count

def reverse_list(list_of_values):
    reversed_list = []
    for i in range(len(list_of_values)-1, -1, -1):
        reversed_list.append(list_of_values[i])
    return reversed_list

def remove_duplicates(list_of_values):
    unique_list = []
    for v in list_of_values:
        if v not in unique_list:
            unique_list.append(v)
    return unique_list

def second_largest(list_of_numbers):
    max_num = list_of_numbers[0]
    second_max = None
    for num in list_of_numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num != max_num and (second_max is None or num > second_max):
            second_max = num
    return second_max


def merge_two_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list



print(merge_two_sorted_lists([1, 3, 5], [2, 4, 6])) 