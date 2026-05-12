# #1
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     elif i == 7:
#         break
#     print(i)    

# #2
# while True:
#     user_password = input("Enter your password: ")
#     if user_password == "1234":
#         print("welcome")
#         break
#     else:
#         print("try again")

#3
# while True:
#     user_product = input("Enter the product you want to purchase: ")
#     if user_product == "done":
#         break
# print(f"You have selected: {user_product}")


# #4 
# for row in range(3):
#     for col in range(3):
#         if col == 2:
#             break
#         print(f"Row: {row}, Column: {col}")

# #5rm -rf node_modules package-lock.json
# letter  = str(input("Enter a letter: "))
# Score_letters = 0
# for i in letter:
#     chr = i.upper()
#     if chr in "AEIOU":

#         Score_letters += 1
# print(f"Score: {Score_letters}")    


for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{result}", end="  ")
    print()