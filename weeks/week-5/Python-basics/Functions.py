def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def is_polindrome(s):
    if s == s[::-1]:
        return True
    else:        return False

def sum_digits(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def caunt_number(n):
    caunt = 0
    while n > 0:
        n = n // 10 
        caunt += 1
    return caunt        


def revers_number(n):
    n1 = str(n)
    revers_n = n1[::-1]
    reslut = ""
    for chr in revers_n:
        if chr == "0":
            continue
        reslut += chr
    return int(reslut)

def moving_zeros(list_number):
    n_count = 0
    i = 0

    while i < len(list_number):
        if list_number[i] == 0:
            n_count +=1
            list_number.pop(i)
        else:
            i +=1 
    list_number += [0] * n_count
    return list_number

print(moving_zeros([2,0,3,4,0,5]))  

# def calculations(list_number):
#     sum_list = sum(list_number)
#     max_list = max(list_number)
#     min_list = min(list_number)
#     if len(list_number):
#   ]


def push_zero(arr):
    for val in arr: 
        if val == 0:   
            arr.remove(0)
            arr.append(0)
    return arr

print(push_zero([0,0,1]))
  


d  

    
    

