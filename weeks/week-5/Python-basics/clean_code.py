#1
def chake_users_over_18_and_active(users):
    users_over_18 = []
    for user in users:
        if user[1] > 18 and user[2] == "active":
            users.append(user[0])
    return users_over_18 

#2
def valid_user_email(user_email):
    if user_email:
        return True
    else:
        print ("Invalid user")
        

def valid_stock(stock, quantity):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
    else:
        return True    


def has_discount(quantity):
    return quantity >= 10 

def Confirmed_order(valid_stock,valid_user_email):
    pass

def price_before_discount(quantity, product_price):
    price = product_price * quantity
    return price

def price_after_discount(price, quantity):
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price    

def print_order(user_email, product_name, quantity, final_price, order_status="confirmed"):
      print(f"Order {order_status}: {user_email} bought {quantity}x {product_name} for ${final_price}")
    


def main():
    user_email = ""
    product_name = ""
    product_price = 0
    stock = 0
    quantity = 0
    if valid_user_email(user_email) and valid_stock(stock):
        price = price_before_discount(quantity, product_price)
        if has_discount(quantity):
            price = price_after_discount(quantity, price)
        
        display_order = print_order(user_email, product_name, quantity, final_price, order_status="confirmed")
        print(display_order) 




              


