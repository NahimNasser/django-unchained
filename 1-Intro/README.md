Session 1: Intro to Python
==============================================
Description:
------------
This session will discuss pythonic syntax, structure, and principles. Useful built-in functions, and data structures critical for use with django will be covered. We will be using the python interactive interpreter for a portion of this lesson.

Outline:
--------
* Intro to Python: Why Python?
* Data Structures: Strings, Integers, Floats, Dictionaries, Lists, Tuples, Sets. Talk about differences and use cases.
* Statements and Functions: if, while, for, lambda, filter, sorted, map, dir, help, pdb
* something to code in class
* something to take home.

Python's built-in types:
------------------------
http://en.wikipedia.org/wiki/Python_(programming_language)#Typing

Statements and Functions:
----------------

### Dissection of a python function

```python

def spam(name, firstword='hello', secondword='world', *args, **kwargs):
	'''Prints a string with two words and a name

    Args:
        name: The name of the user
        firstword: The first word in the sequence, defaulting to 'hello'
        secondword: The second word in the sequence, defaulting to 'world'

    Returns:
        A tuple containing all three strings

    Raises:
        NameError: Only occurs when user named Vimal attempts to use this function
    '''

    if name=='Vimol':
    	raise NameError('VI')

    spam_tuple = (firstword, secondword, name)
	print "%s %s %s" % spam_tuple

	return spam_tuple

```

#### Function Arguments

The first thing you will notice about the arguments is that python is **dynamically typed**. Type checking is performed at run-time as opposed to compile time.

Now lets look at each argument, and the special properties and syntax of each one:

* *name* is a mandatory argument
* *firstword* and *secondword* are both **default argument values**, this means that the argument is optional, and a default value is assumed when no value is specified
* *args* is an **arbitrary argument list**, this means that our function can be called with an arbitrary number of arguments
* *kwargs* is a dictionary containing all keyword arguments except our formal parameters specified.
