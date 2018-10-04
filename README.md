# robotframework-csvlib
CSV library for robotframework written in Python 3


## Quick Keyword Overview
```
Read CSV As Single List 
    Arguments:
        Filepath
        Delimiter (optional)
    Returns:
        A single list with all values.
```
```
Read CSV As List 
    Arguments:
        Filepath
        Delimiter (optional)
    Returns:
        A list containing all rows as lists.
```
```
Read CSV As Dictionary 
    Arguments:
        Filepath
        Name of key column
        Name(s) of value column(s)
        Delimiter (optional)
    Returns:
        A dictionary with the key column a key and the value column(s) as value. 
        If there are multiple value columns the value will be a list containing all values.
```
