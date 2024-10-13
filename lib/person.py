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
    _name = None
    _job = None

    def __init__(self, new_name = None, new_job = None):
        # new_name: what the caller is trying to set the name to
        # self._name: the actual name of the person
        # self.name: A property which has validation before actually setting _name


        if new_name is not None:
            self.name = new_name

        if new_job is not None:
            self.job = new_job

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)