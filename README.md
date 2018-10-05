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

### Example
```
*** Settings ***
Library  CSVLib

*** Test Cases ***
Test CSV
	${singlelist}=		Read CSV As Single List		test.csv
	log to console		${singlelist}

	${list}=		read csv as list		test.csv
	log to console		${list}

	${dict}=		read csv as dictionary		test_dict.csv		Animal		Legs		,
	log to console		${dict}

	${value}=		create list			Legs			Eyes
	${dictWList}=		read csv as dictionary		test_dict1.csv		Animal		${value}	,
	log to console		${dictWList}
```