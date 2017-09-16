#!/usr/bin/env python3

"""Use fibonacci function with module import
    The module reuse the fibonacci function and print the nth fibonacci number
"""
   
from sequences import fibonacci

def main(local_argv):
    """Main function
    This block of code will run only as a standalone function. If it is loaded
    as a module by another program, this will not run. 
    """
    try:
        n = local_argv[1]
    except IndexError:
        print("Enter an argument")
    else:
        result = fibonacci(int(n))
        print(result[-1])
        return result[-1]

if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv)
