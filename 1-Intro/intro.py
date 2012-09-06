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

    #String methods such as capitalize() can be found here: http://docs.python.org/library/stdtypes.html#string-methods
    spam = "%s %s, %s" % (firstword.capitalize(), secondword, name)

    return spam