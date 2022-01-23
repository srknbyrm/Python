def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

# 3, 4, 5 are combined into args
# six and seven are combined into kwargs
foo(1, 2, 3, 4, 5, six=6, seven=7)
print()

# omitting of args or kwargs is also possible
foo(1, 2, three=3)

def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, c=3, d=4)
# not allowed:
# foo(1, 2, 3, 4)

# arguments after variable-length arguments must be keyword arguments
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(8, 9, 10, last=50)

def foo(a, b, c):
    print(a, b, c)


# list/tuple unpacking, length must match
my_list = [4, 5, 6] # or tuple
foo(*my_list)

# dict unpacking, keys and length must match
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)

# my_dict = {'a': 1, 'b': 2, 'd': 3} # not possible since wrong keyword

def foo1():
    x = number # global variable can only be accessed here
    print('number in function:', x)

number = 0
foo1()

# modifying the global variable
def foo2():
    global number # global variable can now be accessed and modified
    number = 3

print('number before foo2(): ', number)
foo2() # modifies the global variable
print('number after foo2(): ', number)


def hoo(**kwargs):
    print(kwargs)

a = {'key':'value'}
hoo(**a)
hoo(data='serkan')
