#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    _name = None
    _breed = None

    def __init__(self, new_name = None, new_breed = None):
        # new_name: what the caller is trying to set the name to
        # self._name: the actual name of the person
        # self.name: A property which has validation before actually setting _name
        if new_name is not None:
            self.name = new_name
        
        if new_breed is not None:
            self.breed = new_breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)



Dog(new_name="")

your_output = "Name must be string between 1 and 25 characters.\nBreed must be in list of approved breeds."

expected_output = "Name must be string between 1 and 25 characters."

your_output == expected_output