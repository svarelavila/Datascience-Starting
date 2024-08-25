def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object
    Returns an iterator that produces those iterable elements
    for which function(element) is true.
    If the function is None, returns elements that are true.
    """
    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
