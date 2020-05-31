# ========= Lists and Functions =========

n = [1, 3, 5]
# Do your multiplication here
n[1] = n[1] * 5
n.append(4)
# n.pop(index) will remove the item at index from the list and return it to you
n.pop(0)
# n.remove(item) will remove the actual item if it finds it
n.remove(4)
print(n)


def my_function(x):
    return x * 3


number = 2
print(my_function(number))

# ========= Functions =========

m = 5
n = 13


def add_function(x, y):
    return x + y


print(add_function(m, n))

#  ========= Lists and Functions =========
print("============")
n = "Hello"


def string_function(s):
    return s + "world"


print(string_function(n))

#  ========= Lists and Functions =========

n = [1, 2, 3, 4]

print("============")


# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst


print(list_extender(n))

#  ========= Lists and Functions =========

print("============")
n = [3, 5, 7]


def print_list(x):
    for i in range(0, len(x)):
        print(x[i])


print_list(n)

#  ========= Lists and Functions =========
print("============")
n = [3, 5, 7]


def double_list(n):
    for i in range(0, len(n)):
        n[i] = n[i] * 2
    return n


print(double_list(n))

#  ========= Range =========

print("====== Range ======")


def my_function(x):
    for i in list(range(0, len(x))):
        x[i] = x[i]
    return x


print(my_function(list(range(3))))

#  ========= Range =========

print("====== Range ======")

n = [3, 5, 7]


# this method uses indexes to loop through
# the list, making it possible to also modify the list if needed.

def total(numbers):
    result = 0
    for i in list(range(len(numbers))):
        result += numbers[i]
    return result


print("Result: %d" % total(n))

#  ========= Strings and Lists  =========

print("====== Strings and Lists ======")

n = ["Michael", "Lieberman"]


# Add your function here

def join_strings(words):
    result = ""
    for l in list(range(len(words))):
        result += words[l]
    return result


print(join_strings(n))

#  ========= Strings and Lists  =========

print("====== Strings and Lists ======")

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


# Add your function her
def flatten(lists):
    results = []
    for numbers in lists:
        for item in numbers:
            results.append(item)
    return results


print("Flatten: %s" % flatten(n))
