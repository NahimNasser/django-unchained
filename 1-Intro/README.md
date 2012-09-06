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
[Table of Python Types](http://en.wikipedia.org/wiki/Python_(programming_language)#Typing)

Statements and Functions:
----------------

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
