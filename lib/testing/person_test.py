#!/usr/bin/env python3

from person import Person

import io
import sys

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person".'''
        guido = Person(new_name='Guido', new_job='Sales')
        assert(type(guido) == Person)
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(new_name="", new_job="Sales")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(new_name=123, new_job='Sales')
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(new_name="What do Persons do on their day off? Can't lie around - that's their job.",
               new_job='Sales')
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person("Guido")
        assert(guido.name == "Guido")

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters'''
        guido = Person(new_name="guido van rossum")
        assert(guido.name == "Guido Van Rossum")

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(new_job="Benevolent dictator for life")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Job must be in list of approved jobs.\n")

    def test_job_in_list(self):
        '''saves job if in job list.'''
        guido = Person(new_job="ITC")
        assert(guido.job == "ITC")
