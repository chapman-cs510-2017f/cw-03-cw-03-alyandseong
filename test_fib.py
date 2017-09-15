#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test fib.py
The module contains one test function to test fib.py.
"""

import fib

def test_function():
    result = fib.main(['fib.py', 100])
    correct = 354224848179261915075
    assert result == correct



