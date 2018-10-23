COURSE OBJECTIVES
1.Explore Core Programming concepts and be able to broadly define them.

2.Break down a problem into programmable steps and write in pseudocode.

3.Understand how to work with user stories and requirements.

4.Understand how to get input and display output in python

5.Implement a simple python program using variables, functions and lists.

Python Documentation
https://docs.python.org/3/index.html

--------------------------------------

INPUT --> PROCESSING --> OUTPUT

--------------------------------------

VARIABLES
-Variables store inputs
-All data types are Objects, some are immutable
-Variables names should be meaningful

OPERATIONS
-Process operations on variables to process input operations
-Basic operations include mathematical and string manipulation
-When variables of different types are operated on the end result is cast to one of the types

FUNCTIONS
-use to encapsulate parts of program and make it accessible to re-use from other parts
-Makes it easier for humans to understand
-Functions are defined once and can be called multiple times
-When you pass argument to function parameters it uses the "pass by" object protocol instead of either "pass by reference" or "pass by value". Reference to object is what's passed but immutable objects remain immutable while other objects can be modified in the body of the function.

BASIC EXAMPLE

        def my_function():
          print("Hello from a function")

          my_function()

-function is defined using keyword "def"
-call function using function name followed by parenthesis

PARAMETERS
Information can be passed to functions as parameter.Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

        def my_function(fname):
          print(fname + " Refsnes")

        my_function("Emil")
        my_function("Tobias")
        my_function("Linus")

Default Parameter Value
        def my_function(country = "Norway"):
          print("I am from " + country)

        my_function("Sweden")
        my_function("India")
        my_function()
        my_function("Brazil")


RETURN VALUES
To let a function return a value, use the return statement

        def my_function(x):
          return 5 * x

        print(my_function(3))
        print(my_function(5))
        print(my_function(9))
