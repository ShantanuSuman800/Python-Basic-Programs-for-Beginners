#Python Program to Form a Dictionary from an Object of a Class
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = MyClass('John', 25)

# converting object of MyClass to dictionary
dict_obj = dict(obj.__dict__)

print(dict_obj)