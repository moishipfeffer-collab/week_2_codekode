# exercise 1 

"""
1. Pure, the funktion is doing one thing and the same output
2. Not pure, printing to the screen, side efect
3. Not pure, the "cart" is changing
4. Pure, the cart is not changing
 """

# exercise 2 

def add_price(total, price):
    return total + price 

# exercise 3

TAX = 1.17
def apply_tax(prices):
    total = []
    for price in prices:
        total.append(price * TAX)
    return total

# exercise 4 

def calculate_total(prices):
    total = 0 
    for price in prices:
        total += price 
    return total 
def show_total(prices):
    total = calculate_total(prices)
    print(total)

# exercise 5 

def top_three(numbers:list):
    return sorted(numbers,reverse=True)[:3]

