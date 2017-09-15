#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Aly and Seong
# Course: CS510 Fall 2017
###

"""Fibonacci program
This module includes a function fibonacci(n) that returns the first n Fibonacci numbers in a list.
"""

def fibonacci(n):
    """ fibonacci function
    Args: 
        n (int): the number for the n numbers of fibonacci 
    Returns:
        a list of finobacci numbers  
    """
    result = [1] # fibonacci number starts from 1
    t1 = 1
    t2 = 1

    if n > 0:
        for _ in range(n-1):
            result.append(t2)
            t3 = t1 + t2
            t1 = t2
            t2 = t3
    
        return(result)

    else:
        raise ValueError("Enter a positive number, please")


