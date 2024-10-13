#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    APPROVED_JOBS = APPROVED_JOBS

    def __init__(self, name = None, job = None):
        # Validate name
        self._name = None
        if name is not None:
            self.name = name  # Use property setter to validate

        # Validate job
        self._job = None
        if job is not None:
            self.job = job  # Use property setter to validate

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
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in Person.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value
            