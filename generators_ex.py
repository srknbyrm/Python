def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()
print(g)

# value = next(g)
# print(value)
#
# value = next(g)
# print(value)

# for i in g:
#     print(i)

print(sorted(g))


def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(5)
value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))


# without a generator, the complete sequence has to be stored here in a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys

print(sys.getsizeof(firstn(1000000)), "bytes")


# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

import sys

print(sys.getsizeof(firstn(1000000)), "bytes")


def fibonacci(limit):
    a, b = 0, 1  # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib))


# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))
print('end main')