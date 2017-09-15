#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Testing fibonacci sequence
This module contains three test functions to keep the fibonacci function safe from errors.
"""

import sequences

def test_fibonacci():
    """test the first five fibonacci numbers"""
    
    result = sequences.fibonacci(5)
    correct = [1, 1, 2, 3, 5]
    assert result == correct


def test_fibonacci2():
    """test the thousandth fibonacci number"""

    result = sequences.fibonacci(1000)[-1] # return integer type
    correct = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    assert result == correct
 

def test_fibonacci3():
    """test if the fibonacci list starts from 1."""

    result = sequences.fibonacci(10)[0]
    correct = 1
    assert result == correct






