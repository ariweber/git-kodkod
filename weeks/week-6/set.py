#1
def remove_duplicates(list_of_values):
   return list(set(list_of_values))


#2
def count_unique_elements(list_of_values):
    unique_values = set(list_of_values)
    return len(unique_values)


#3
def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_set = set1.intersection(set2)
    return sorted(common_set)

#4
def elements_in_only_one(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    only_in_first = set1.difference(set2)
    only_in_second = set2.difference(set1)
    return sorted(only_in_first.union(only_in_second))

#5
def is_subset(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.issubset(set_b)

#6
def unique_characters(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
    return True

#7
def first_repeated_element(list_of_values):
    seen = set()
    for value in list_of_values:
        if value in seen:
            return value
        seen.add(value)
    return None

#8
def count_distinct_words(string):
    words = string.lower().split()
    distinct_words = set(words)
    return len(distinct_words)  

#9
def pair_sum_exists(list_of_numbers, target):
    seen = set()
    for num in list_of_numbers:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

#10
def symmetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    only_in_1 = [x for x in set1 if x not in set2]
    only_in_2 = [x for x in set2 if x not in set1]
    
    return sorted(only_in_1 + only_in_2)
ף323א