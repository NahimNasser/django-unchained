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

    spam_tuple = (firstword.capitalize(), secondword, name)
    print "%s %s, %s" % spam_tuple

    return spam_tuple