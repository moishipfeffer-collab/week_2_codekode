
# exercose 1 

def double(number):
    return number * 2

def apply_to_all(numbers, action):
    new_numbers = []
    for num in numbers:
        new_numbers.append(action(num))
    return new_numbers

# exersice 2 

prices = [20, 75, 120, 45, 90]
expensive = list(filter(lambda p: p > 50,prices))
add = list(map(lambda p: p + 10, prices))

# exercose 3 

words = ["banana", "fig", "cherry", "kiwi"]
students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]
sorted_words = sorted(words, key= lambda w: len(w))
longest = max(words, key=len)
sorted_students = sorted(students, key=lambda s: len(s[0]),reverse=True)
sorted_names = list(map(lambda s: s[0], sorted_students))

# exercise 4 

def make_discount(percent):
    def calc_price(price):
        return price * (100 - percent) / 100
    return calc_price
ten_off = make_discount(10)
half_price = make_discount(50)

# exersice 5 

"""
1. The problem is that you are calling the funktion without a param
2. you need to just write the funk object and call it inside the funktion"""