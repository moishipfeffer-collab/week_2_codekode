# exercise 1 
"""
The "message is in the funktion skope and the global dosent now it"""
def welcome(name):
    message = "Welcome " + name
    return message

message = welcome("Dana")
# print(message)
# print(message)

# exercise 2 

"""
1: local in first
2: global
3: global
"""

# exercise 3 

"""
UnboundLocalError becouse the funktion can not add to "count" when 
it dose not have a value in it, even if in the global it dose.
the fix is:"""
def add_one(count):
    count += 1
    print (count)
count = 0
# add_one(count)

# exercise 4 

"""
1. typeerror, becouse the lokal "list" overided the built-in list
2. the fix is:"""
_list = [1,2,3]
numbers = list(range(5)) 

# exercise 5 

def add(cart: list,price):
    return cart.append(price)
def total(cart):
    total_list =  sum(cart)
    return total_list

cart = []
add(cart,100)
add(cart,50)

print(cart,total(cart))

