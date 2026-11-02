# exercise 1 

def format_receipt(items):
    def line(name,price):
        return name.ljust(10) + str(price)
    items_list = []
    for name,price in items:
        items_list.append(line(name,price))
    return "\n".join(items_list)

# print(format_receipt([("Milk", 6), ("Bread", 9)]))

# exercise 2

def make_greeter(greeting):
    def greet(name):
        return f"{greeting} {name}"
    return greet

# hello = make_greeter("Hello")
# shalom = make_greeter("Shalom")
# print(hello("Dana"))
# print(shalom("Avi"))

# exercise 3 

"""show: outer
show: changed
"""

# exercise 4 

def make_counter(step):
    total = 0
    def add():
        nonlocal total
        total += step
        return total
    return add 

# by_two = make_counter(2)
# by_ten = make_counter(10)
# print(by_two(), by_two())
# print(by_ten())
# print(by_two())

# exercise 5 

"""
1. UnboundLocalError, becouse python thinks it is a variable in the 
funktion and it dosent have eny value in it
2. global is on the file not in eny funktion, and nonelocal is in a 
funktion "above" the current one """
