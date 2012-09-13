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


Setup:
------
1. Clone the git repo
2. Make sure python is installed (type python in the command line, it should open up an interpreter)
3. Navigate to the 1-Intro directory
4. Run ```python -m unittest test_intro``` in your powershell(windows) or terminal(mac) to ensure everything is configured correctly
5. open up test_intro.py and intro.py in your favourite editor, and begin the workshop



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
        A string containing the name, firstword, and second word

    Raises:
        NameError: Only occurs when user named Vimal attempts to use this function
    '''

    if name == 'Vimol':
        raise NameError('VI')

    #String methods such as capitalize() can be found here: http://docs.python.org/library/stdtypes.html#string-methods
    spam = "%s %s, %s" % (firstword.capitalize(), secondword, name)
    return spam
```

### Function Arguments

The first thing you will notice about the arguments is that python is **dynamically typed**. Type checking is performed at run-time as opposed to compile time.

Now lets look at each argument, and the special properties and syntax of each one:

* *name* is a mandatory argument
* *firstword* and *secondword* are both **default argument values**, this means that the argument is optional, and a default value is assumed when no value is specified
* *args* is an **arbitrary argument list**, this means that our function can be called with an arbitrary number of arguments
* *kwargs* is a dictionary containing all keyword arguments except our formal parameters specified.

In your terminal, navigate to the 1-Intro directory, and type **python**

Lets import some code, so you dont have to write it all in the interpreter:
```python
import intro
```

Note any calls to any functions in intro.py must be prefixed with **intro.**

If you make changes to your intro.py file, instead of closing and reopening the python interpreter, you can simply type

```python
reload(intro)
```

*NOTE: We're using out of the box caveman tools to give you an understanding of how things work, more advanced tools will be introduced later*

Try the following calls to spam:

```python
spam('Alex')
spam(name='Alex')
spam('Alex', 'Hey', 'Globe')
spam(firstword='Hey', name='Alex', secondword='Globe')
spam('Alex', 'Hey', 'Globe', 'WTF?')
spam(firstword='Hey', name='Alex', secondword='Globe', crazyvar='WTF?')
```

####The Magic of Lambda Functions

Here's a rather simple function 

```python
def magic(x):
    return x*2

print magic(2)
```

Here's how we could accomplish the same thing with a lambda function

```python
magic = lambda x: x*2
nameless = magic

print magic(2)
print nameless(2)
```

Lambda Functions (or Anonymous Functions) are functions that are not bound to a name--- and are frequently used with other built in functions such as map() and filter()

####Built-in python functions - Map

Built-in python functions can be the difference between 10+ LOC vs 1. It is extremely useful to be aware of the various built-in function.

For the full list, check out: 
http://docs.python.org/library/functions.html

Heres a regular function without using built in functions:
(Yes i know, really terrible code)

```python
# Given a list, we want to multiply each integer in the list by two
sample = [1, 2, 3, 4, 5]

def multiply_list_by_2(sample_list):
    # For each number in sample_list
    newlist = []
    for number in sample_list:
        newlist.append(number * 2)
    return newlist
```

Now that you've seen that, lets use a lambda function in conjunction with map().

The map function is defined as follows: "Apply function to every item of iterable and return a list of the results."

The one liner using map():
```python
newlist = map(lambda x: x * 2, sample)
```

The one liner using list comprehensions (faster in this case):
http://docs.python.org/tutorial/datastructures.html#list-comprehensions
```python
newlist = [x * 2 for number in sample]
```

Now you're probably thinking, when should I use *Map()*, and when should I use a *List Comprehension*?

HOMEWORK: You can find a good discussion here:
http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map

#### Unit testing in python:
* Open up test_intro.py in your text editor
* run ```python -m unittest test_intro```

Lets create a breakpoint in our code, and walk through a debugging flow.
