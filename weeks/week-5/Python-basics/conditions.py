def status_age(age):
    if age < 0 or age > 120:
        return "Invalid age"
    elif 0 < age <= 12:
        return "Child"
    elif 13 <= age <= 17:
        return "Teen"
    else:        return "Adult"


def english_letter(char):
    if char.isalpha() and char.isascii():
        return "English letter"
    else:
        return "Not an English letter"



def entry(age, has_vip_card):
    if age < 18:
        return
    elif age >= 18 and has_vip_card:
        return "welcome"
    
def validate_password(password, input_password):
    if password == input_password:
        return "Access Granted"
    elif len(password) > len(input_password):
        return "Password is too short"
    else:
        return "Wrong password"



def check_point_position(x: float, y: float):
    if 10 < x < 50 and 20 < y < 80:
        return "Inside the rectangle"
    elif (x == 10 or x == 50) and 20 <= y <= 80 or (y == 20 or y == 80) and 10 <= x <= 50:
        return "On the edge"
    else:
        return "Outside the rectangle"
    
 
name = input("Enter your name: ")
if name:
    greeting = f"Hello, {name}!"
else:
    greeting = "Hello, Anonymous!"    
print(greeting)



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
positive_count = (num1 > 0) + (num2 > 0) + (num3 > 0)
print (positive_count)


score = int(input("Enter your score"))
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F"))
print(grade)




