# ========= String Looping=========
for letter in "Codecademy":
    print(letter)

# Empty lines to make the output pretty
print()
print()

# ========= Dictionaries=========
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % stock[key])

total = 0
for key in prices:
    print(prices[key] * stock[key])
    total += prices[key] * stock[key]

print("Total: %s" % total)


# ========= Making a Purchase =========

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# Write your code below!
def compute_bill(food):
    totl = 0
    for key in food:
        if stock[key] > 0:
            totl += prices[key]
            stock[key] -= 1
    return totl


print("Total: %s " % compute_bill(shopping_list))
print("Stock: %s " % stock)

