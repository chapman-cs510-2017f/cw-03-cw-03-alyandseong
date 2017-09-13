#!/usr/bin/env python3
import sys

def fibonacci(n):
    result = []
    t1 = 1
    t2 = 1

    if n > 1:
        result.append(1)
        for i in range(n-1):
            result.append(t2)
            t3 = t1 + t2
            t1 = t2
            t2 = t3
    
        return(result)

    else:
        return("Sorry, provide a positive number")

