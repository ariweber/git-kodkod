#exe 1
# num_is_even = int(input("Enter a number: "))
# print(num_is_even % 2 == 0)

# #exe 2
# a = 7
# b = 6
# a = b + a
# b = a - b
# a = a - b   
# print(a, b)

#exe 3
num_int = 321
first_num = num_int // 100
second_num = (num_int % 100) // 10
third_num = num_int % 10
print(first_num + second_num + third_num)

#exe 4 
weight = 7.1
hight = 0.76
bmi = (weight / (hight ** 2))
print(f"{bmi: .2f}")
