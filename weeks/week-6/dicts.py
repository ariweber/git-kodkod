#1
def sum_of_values(dict_number: dict) -> int:
    total = 0
    for val in dict_number.values():
        total += val
    return total

#2
def Key_maximum_valu(dict_number: dict) -> str:
    kay = ""
    max_val = None
    for k, v  in dict_number.items():
        if not max_val or v > max_val:
            max_val = v
            kay = k 
    return kay    
    

#3
def count_characters(string: str) -> dict:
    dict_count = {}
    for letter in string:
        if letter not in dict_count:
            dict_count[letter] = 1
        else:
            dict_count[letter] += 1  
    return dict_count          


#4
def invert_dictionary(dict_invert: dict) -> dict:
    new_dict = {}
    for k, v in dict_invert.items():
        new_dict[v] = k
    return new_dict

#5
def merge_two_dictionaries(dict1: dict, dict2: dict) -> dict:
    new_dict = {}
    new_dict.update(dict1)
    new_dict.update(dict2)  
    return new_dict

print(merge_two_dictionaries({"a": 1, "b": 2}, {"b": 20, "c": 30} ))   

#6
def filter_by_value(dict_valu: dict, threshold: int) -> dict:
    dict_over_threshold = {}
    for k, v in  dict_valu.items():
        if v > threshold:
            dict_over_threshold[k] = v
    return dict_over_threshold

#7
def group_first_lette(list_words: list) -> dict:
    dict_first_letter = {}
    for word in list_words:
        dict_first_letter[word[0]] = word
    return dict_first_letter

print(group_first_lette( ["apple", "ant", "banana", "berry", "cherry"]))    

#8
def word_frequency(string: str) -> dict:
    count_dict = {}
    words = string.split()
    
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
            
    return count_dict

print(word_frequency("the cat sat on the mat"))

#9
def common_keys(dict1, dict2):
    common = []
    for k in dict1:
        if k in dict2:
            common.append(k)
    return common     

#10
def most_frequent_value(dict_count: dict):
    max_count = 0
    most_frequent = None
    for v in dict_count.values():
        if v > max_count:
            max_count = v
            most_frequent = v
    return most_frequent

