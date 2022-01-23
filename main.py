from getpass import getpass

# For Large Numbers U can Use Separator
number1 = 10_000_000_000
number2 = 10_000_000

print(number1)
print(f"{number1:,}")

# By using with u dont have to close the connection
# with open("test.txt") as f:
#     file_content = f.read()

letters = ["S", "E", "R", "K", "A", "N"]
for index, letter in enumerate(letters, start=1):
    print(index, letter)

# Zip func allows loop over multiple list
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
heroes_two = ["Spiderman", "Superman", "Deadpool", "Batman"]

for name, hero, hero_2 in zip(names, heroes, heroes_two):
    print(f"{name} is {hero} - {hero_2}")

for value in zip(names, heroes, heroes_two):
    print(value)
# output
# ('Peter Parker', 'Spiderman', 'Spiderman')
# ('Clark Kent', 'Superman', 'Superman')
# ('Wade Wilson', 'Deadpool', 'Deadpool')
# ('Bruce Wayne', 'Batman', 'Batman')

# Unpacking

a, b = (1, 2)
# When you don't want to use another item just write underscore (_)
a, _ = (1, 2)

print(a)
print(b)

# Error a, b, c = (1, 2, 3, 4, 5)
a, b, *c = (1, 2, 3, 4, 5)
print(c)
# c will be [3, 4, 5]

a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)
print(_)
# underscore will be [3, 4, 5]

a, b, *c, d = (1, 2, 3, 4, 5)
print(c)  # c will be [3, 4]
print(d)  # d will be 5

# user_name = input("Username: ")
# password = getpass("Password: ")  # to hide password

# if user_name == "Serkan" and password == "123":
#     print("Logged in")

# python -m main will run python code if you re not in same folder with virtual env
# smpt module python -m smpt
# from datetime import datetime
# dir(datetime) it will give attr and methods


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(f"1 count in tuple: {my_tuple.count(1)}")

my_tuple_2 = tuple(my_tuple)

my_tuple_3 = my_tuple

my_tuple += (5, 1)

print(my_tuple)
print(my_tuple_3)
print(my_tuple_2)

my_dict = {"name": "serkan"}
my_dict_2 = my_dict
my_dict_3 = dict(my_dict)  # or my_dict.copy()
my_dict["last_name"] = "bayram"

print(my_dict_2)
print(my_dict_3)

# sets no duplicate
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {5, 1, 6, 7, 8}

list_to_set = [1, 1, 1]
new_set = set(list_to_set)
print(new_set)  # output will be 1

union_set = set_1.union(set_2)
print(union_set)

intersect_set = set_1.intersection(set_2)
print(intersect_set)

difference_set = set_2.difference(set_1)
print(difference_set)

# set_1.update(set_2)
# print(set_1)
#
# set_1.difference_update(set_2)
# print(set_1)
#
# set_1.intersection_update(set_2)
# print(set_1)

print(set_1.issubset(set_2))

string = 'serkan'
print(string.count('s'))
print(string.capitalize())
print(string.upper())
print(string.lower())
print(string.find('n'))  # it will return the index of character

string_2 = 'serkan bayram'
list_of_string = string_2.split()
print(list_of_string)

string_2 = 'serkan,bayram'
list_of_string = string_2.split(',')  # s-e-r-k-a-n-,-b-a-y-r-a-m
print(list_of_string)

new_string = '-'.join(string_2)
print(new_string)

# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = 'aaaaabbbbbbbxxx'
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))
print(my_counter.keys())
print(my_counter.values())
print(my_counter.elements())

Point = namedtuple('Point', 'x,y')  # it will create a class
pt = Point(1, 2)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

for key, value in ordered_dict.items():
    print(f'Key: {key} Value: {value}')

d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d['c'])

deque_instance = deque()
deque_instance.append(5)
deque_instance.append(5)
deque_instance.appendleft(1)
print(deque_instance)
deque_instance.extend([1, 2, 3])
print(deque_instance)
deque_instance.rotate(1)
print(deque_instance)
deque_instance.rotate(2)
print(deque_instance)
deque_instance.rotate(-1)
print(deque_instance)

# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator

a = [1, 2]
b = [3, 4]
prod = product(a, b)
prod_2 = product(a, b, repeat=2)
print(list(prod))
print(list(prod_2))

a = [1, 2, 3]
perm = permutations(a)
print(f'Permutations of {a}: ', list(perm))

com = combinations(a, 2)
print(f'Combination of {a}: ', list(com))

com_wr = combinations_with_replacement(a, 2)
print(f'Combination with replacement of {a}: ', list(com))

acc = accumulate(a)
print(f'Accumulation of {a}: ', list(acc))

acc = accumulate(a, operator.mul)
print(f'Multiple Accumulation of {a}: ', list(acc))


def smaller_than_three(x):
    return x < 3


smaller_than_3 = lambda x: x < 3

group_by = groupby(a, key=smaller_than_3)

for key, value in group_by:
    print(key, list(value))

# infinite iterators
from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 20:
        break

a = [1, 2, 3, 4]
for i in cycle(a):
    print(i)
    if i == 2:
        break

for i in repeat(1, 4):
    print(i)

# lambda functions
# lambda arguments: expression
print('LAMBDA FUNCTIONS')

add_five = lambda x: x + 5
print(add_five(10))

mult = lambda x, y: x * y
print(mult(2, 5))

points2D = [(1, 2), (11, 22), (5, -1)]
sorted_points2D = sorted(points2D, key=lambda x: x[1])  # it will sort accordinng to y values
sorted_points2D_2 = sorted(points2D, key=lambda x: x[0] + x[1])  # it will sort accordinng to summation of values

# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

# or list comprehension

c = [x * 2 for x in a]
print(list(c))

# filter(func, seq)
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# reduce(func, seq)
from functools import reduce

a = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x * y, a)
print('Reduce Result: ', b)

# Errors and Exceptions
print('Errors and Exceptions')
# x = -5
# assert (x > 0), 'x is less than 0'

try:
    x = 5 / 1
    b = x + 1
except ZeroDivisionError as ex:
    print('Error', ex)
except TypeError as ex:
    print('Error', ex)
else:
    print('No Error')
finally:
    print('cleaning up')  # Will work every condition


class ValueTooHighError(Exception):
    def __init__(self, message_param, value_param):
        self.message = message_param
        self.value = value_param


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value too high', x)


try:
    test_value(200)
except ValueTooHighError as e:
    print(e.message, e.value)



