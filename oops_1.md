https://www.geeksforgeeks.org/python/python-oops-concepts/

## Overview
* class, object, init, class variable, instance variables, update variables


### Class
* A class is a blue print for an object (instance)
* A class defines the attributes that the object can have
* A class is created using the `class` keyword
* Attributes are variables that belong to a class
* Attributes can be accessed using the dot `.` operator

```python
class homosapien:
    def __init__(self, firstname, lastname, age, citizen, height, weight, aadhar):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.citizen = citizen
        self.height = height
        self.weight = weight
        self.aadhar = aadhar
``` 

### Object
* An object is an instance of a class
* An object contains its own data
* An object consists of `state`, `behaviour`, `identity`
* `object = name_of_a_class(attributes)`

```python
sapien_1 = homosapien('Varun')
```

### self
* `self` parameter lets us access the attributes and methods of the object

### `__init__`
* The `__init__` method is automatically called when an object is created.
* This helps us access the attributes and methods of the object.

### Class variable
* A class variable is like a global variable. All the instances of a class share the same value for this variable unless explicitly overridden. 
* A class variable is declared outside all methods in a class. 
* A class variable can be accessed using `classname.class_variable`.

### Instance variable
* An instance variable is like a local variable. 
* This variable is specific to the instance. 
* The instance variable is declared inside the `__init__` method.

### Updating variables
* `class_name.variable = new_value` affects all instances
* `object_name.variable = new_value` affects only the corresponding object

### Inheritance
* A child class can acquire properties and methods from its parent class.
* Types - `single`, `multiple`, `multilevel`, `hierarchial`, `hybrid`
* `Single inheritance` - a child inherits from its parent
* `Multiple inheritance` - a child inherits from two parents
* `Multilevel inheritance` - child1(parent) -> child2(child1) i.e., child2 extends child1 inheriting from child1 and parent

### Polymorphism
* poly = many, morphism = behaviours
* A function/method can have different behaviours
* **Compile-time Polymorphism** - Method overloading (not dorectly supported in python)
* **Runtime Polymorphism** - Method overriding, Duck typing, Operator overloading
    * **Method overriding** - A subclass redefines a method from its parent class
    * **Duck Typing** - If an object implements the required method, it works regardless of its type.
    * **Operator Overloading** - Special methods (`__add__`, `__sub__`, etc.) redefine how operators behave for user-defined objects.
