#!/usr/bin/env python3

from functions import greet_programmer, greet, greet_with_default, \
                        add, halve

import io
import sys


def greet_programmer():
    print("Hello, programmer!")

class TestGreetProgrammer:
    '''function greet_programmer()'''

    def test_greet_programmer(self):
        '''prints "Hello, programmer!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_programmer()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello, programmer!\n"

def greet(name):
    print(f"Hello, {name}!")

class TestGreet:
    '''function greet()'''

    def test_greet_programmer(self):
        '''prints "Hello, {name}!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet("Guido")  # Assuming the name "Guido" is passed as an argument
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello, Guido!\n"

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

class TestGreetWithDefault:
    '''function greet_with_default()'''

    def test_greet_with_default(self):
        '''prints "Hello, programmer!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_with_default()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello, programmer!\n"

    def test_greet_with_default_with_param(self):
        '''prints "Hello, {name}!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_with_default("Guido")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello, Guido!\n"

def add(a, b):
    return a + b

class TestAdd:
    '''function add()'''

    def test_add(self):
        '''calculates 45 + 55 = 100'''
        assert add(45, 55) == 100


def halve(number):
    return number / 2

class TestHalve:
    '''function halve()'''

    def test_halve_int(self):
        '''halves integer input'''
        assert halve(100) == 50

    def test_halve_float(self):
        '''halves float input'''
        assert halve(99.0) == 49.5

