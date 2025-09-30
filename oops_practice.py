### class -> objects -> inheritance (single, multiple) -> polymorphism (method overriding)

class homosapien:
    species = 'homosapiens'

    @staticmethod
    def greet():
        return f'Hi Folks. I am learning OOPs in python :)'
    
    def __init__(self, firstname, lastname = None, age=None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

sapien_1 = homosapien('Varun Athithiya')

# Single inheritance
class animal(homosapien):
    def __init__(self, *args, animal_type=None, noise=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.noise = noise
        self.animal_type = animal_type
    
    def make_some_noise(self):
        print(f'My name is {self.__getattribute__('firstname')} {self.__getattribute__('lastname')}. I am a {self.animal_type}. I {self.noise}.')

# creating animal instances
kirtana = animal('Kirtana', 'Shenbagaraj', 23, animal_type='dog', noise='bark')
varun = animal('Varun', 'Athithiya', 31, animal_type='lion', noise='roar')

# kirtana.make_some_noise()
# varun.make_some_noise()

# Multiple inheritance - Inherit from different classes

class machine(animal, homosapien):
    def __init__(self, *args, machine_type=None , **kwargs):
        super().__init__(*args, **kwargs)
        self.machine_type = machine_type
    
    def make_some_noise(self): # Method overriding - modifying the method originally under animal class
        print(f'I have a wonderful {self.noise} !!')
    
bike = machine ('Meteor 350 a.k.a. A K Ayyanar','Royal Enfield', 1, animal_type='beast', noise='engine sound', machine_type='automobile')
print(f'My name is {bike.firstname}')
print(f'My manufacturer is {bike.lastname}')
print(f'I am {bike.age} year old')
print(f'I am a {bike.animal_type}')
bike.make_some_noise()