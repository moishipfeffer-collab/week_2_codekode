# exercise 1 

def make_greeting(name, greeting="Hello", punct="!"):
    return f"{greeting}, {name}{punct}"

# print(make_greeting("Dana"))
# print(make_greeting("Avi", "Good morning"))
# print(make_greeting("Noa", punct="?"))

# exercise 2 

def average(*numbers):
    if not numbers:
        raise ValueError("need at least one number")
    return sum(numbers) / len(numbers)

# print(average(80, 90))
# print(average(70, 80, 90, 100))
# try:
#     average()
# except ValueError as error:
#     print("error:", error)

# exercise 3 

def format_profile(name, **details):
    print_out = f"{name}:"
    for key,value in details.items():
        print_out  += f" {key}={value} "
    return print_out

# print(format_profile("Dana", age=24, city="Haifa"))
# print(format_profile("Avi"))

# exercise 4 

products = [("Laptop", 3500), ("Mouse", 80), ("Desk", 900)]
sorted_products = sorted(products, key= lambda p: p[1], reverse=False)
for product in sorted_products:
#     print(product[0],product[1])
# print(f"most expensive: {max(products)})

# exercise 5 

"""
1. In the second call the funktion will return "milk" and "bread" becouse python 
remembers the first call
2. the fixed function is:
"""
def add_item(item):
    if cart is None:
        cart = []
    cart.append(item)
    return cart 
    


