# dog.py

class Dog:
    # define the constructor
    def __init__(self, name):
        self._name = name

    # encapsulation of instane variable
    def setName(self, name):
        self._name = name
    def getName(self):
        return self._name

    # add some behavior
    def bark(self):
        print('bark '*3) 