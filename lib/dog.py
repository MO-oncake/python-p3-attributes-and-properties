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
    APPROVED_BREEDS = APPROVED_BREEDS

    def __init__(self, name = None, breed = None):
        # Validate name
        self._name = None
        if name is not None:
            self.name = name  # Use property setter to validate

        # Validate breed
        self._breed = None
        if breed is not None:
            self.breed = breed  # Use property setter to validate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            print("Name must be string between 1 and 25 characters.")
        elif not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value.title()

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in Dog.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value
