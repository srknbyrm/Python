import json
data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "swimming", "singing"],
    "age": 28,
    "children": [
        {
            "firstName": "Alex",
            "age": 5
        },
        {
            "firstName": "Bob",
            "age": 7
        }
    ]
}

print(data)
print(type(data))

json_data = json.dumps(data)  # dumps for string

print(json_data)
print(type(json_data))

json_data = json.loads(json_data)
print(json_data)
print(type(json_data))


json_data2 = json.dumps(data, indent=4, separators=("; ", "= "), sort_keys=True)
print('Indent and separator ex:')
print(json_data2)

with open('person.json', 'w') as f:
    json.dump(data, f, indent=4)  # you can also specify indent etc...


with open('person.json', 'r') as f:
    person = json.load(f)
    print(type(person))
    print(person)


class User:
    # Custom class with all instance variables given in the __init__()
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends


class Player:
    # Other custom class
    def __init__(self, name, nickname, level):
        self.name = name
        self.nickname = nickname
        self.level = level


def encode_obj(obj):
    """
    Takes in a custom object and returns a dictionary representation of the object.
    This dict representation also includes the object's module and class names.
    """

    #  Populate the dictionary with object meta data
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)

    return obj_dict


def decode_dct(dct):
    """
    Takes in a dict and returns a custom object associated with the dict.
    It makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in dct:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = dct.pop("__class__")

        # Get the module name from the dict and import it
        module_name = dct.pop("__module__")

        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)

        # Get the class from the module
        class_ = getattr(module, class_name)

        # Use dictionary unpacking to initialize the object
        # Note: This only works if all __init__() arguments of the class are exactly the dict keys
        obj = class_(**dct)
    else:
        obj = dct
    return obj


# User class works with our encoding and decoding methods
user = User(name="John", age=28, friends=["Jane", "Tom"], balance=20.70, active=True)

userJSON = json.dumps(user, default=encode_obj, indent=4, sort_keys=True)
print(userJSON)

user_decoded = json.loads(userJSON, object_hook=decode_dct)
print(type(user_decoded))

# Player class also works with our custom encoding and decoding
player = Player('Max', 'max1234', 5)
playerJSON = json.dumps(player, default=encode_obj, indent=4, sort_keys=True)
print(playerJSON)

player_decoded = json.loads(playerJSON, object_hook=decode_dct)
print(type(player_decoded))

