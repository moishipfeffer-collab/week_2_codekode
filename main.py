
# exercise 1

import prices as p 

def main():
    price = p.apply_discount(200,10)
    print("apter discount:", price)
    vat = p.add_vat(price)
    print("eith vat:", vat)
# main()

# exercise 2

from prices import add_vat
import prices
import prices as p

# print(add_vat(100))
"""
import just one funktion if this is all you need,
import the module need all of it, it helps us nowing witch funktion is from 
witch nodule by the "module.punktion"
import with as alias for comfort, or if you somthing you did with the same name"""

# exercise 3 

import math
import random 
print(math.sqrt(81))
print(round(math.pi,2))
random.seed(1)
print(random.randint(1,6))

# exercise 4 

"""It will print olso the "helpers loaded" becouse you import the file,
avoid it by "if __name__ == __"main"__: """

# exercise 5

import temperature as t
cities = ["Eilat", "Haifa", "Jerusalem"]
temperatures = [35, 22, 9]
for i in range(len(cities)):
    temp = temperatures[i]
    print(f"{cities[i]}: {temp} C / {t.c_to_f(temp)} F - {t.describe(temp)}")
    