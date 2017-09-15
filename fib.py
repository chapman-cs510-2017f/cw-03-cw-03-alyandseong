#!/usr/bin/env python3
from sequences import fibonacci

def main(local_argv):
    """Main function
    This block of code will run only as a standalone function. If it is loaded
    as a module by another program, this will not run. 
    """
    n = local_argv[1]
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
