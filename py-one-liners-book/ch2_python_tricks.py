
import logging
from pprint import pprint, pformat

# find top earners
def test_top_earners():
    empl = {"Alice": 100001,
            "Tom": 99817}
    top_earners = [(k, v) for k, v in empl.items() if v >= 100000]

    logging.info(f'top_earners = {top_earners}')
    # output: [('Alice', 100001)]


# find words with high information value
def test_find_words():

     text = """ Python and other languages like Java, C#, 
     and even C++ have had lambda functions added to their 
     syntax, whereas languages like LISP or the ML family 
     of languages, Haskell, OCaml, and F#, use lambdas as 
     a core concept.
     Python lambdas are little, anonymous functions, subject 
     to a more restrictive but more concise syntax than regular 
     Python functions.
     """

     w = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]
     logging.info(f'w = {w}')
     # w = [['Python', 'other', 'languages', 'like', 'Java,'], ...


# open file and output line by line
def test_reading_file():
    nl = "\n"
    filename = 'ch2_python_tricks.py'
    logging.info(f'{nl.join([line.strip() for line in open(filename)])}')


import pytest
import logging


# mark strings containing particular word
def test_string_contains():
    text = ["Python and other languages like Java, C#",
            "and even C++ have had lambda functions added to their",
            "syntax, whereas languages like LISP or the ML family ",
            "of languages, Haskell, OCaml, and F#, use lambdas as ",
            "a core concept.",
            " Python lambdas are little, anonymous functions, subject" ,
            "to a more restrictive but more concise syntax than regular",
            "Python functions"]

    mark = map(lambda s: ('lambdas' in s, s), text)

    logging.info("\n".join(map(str, mark)))
    logging.info(mark)

    """
     - ‪join() method takes an iterable. 
     - map() returns iterator which is also an iterable.‬
     - iterator is also an iterable, but not every iterable is an iterator.
    """

""" output: 
    INFO(False, 'Python and other languages like Java, C#')
    (False, 'and even C++ have had lambda functions added to their')
    (False, 'syntax, whereas languages like LISP or the ML family ')
    (True, 'of languages, Haskell, OCaml, and F#, use lambdas as ')
    (False, 'a core concept.')
    (True, ' Python lambdas are little, anonymous functions, subject')
    (False, 'to a more restrictive but more concise syntax than regular')
    (False, 'Python functions')
    
    11:40:22 INFO <map object at 0x10729eeb0>
    """




# find query in text and return its immediate environment
def test_function():

    text = """ Python and other languages like Java, C#, 
    and even C++ have had lambda functions added to their 
    syntax, whereas languages like LISP or the ML family 
    of languages, Haskell, OCaml, and F#, use lambdas as 
    a core concept.
    Python lambdas are little, anonymous functions, subject 
    to a more restrictive but more concise syntax than regular 
    Python functions.
    """
    find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1
    logging.info(f"searched text with context: {find(text,'LISP')}")


# slicing
def test_slices():
    # x[start:stop:step]
    s = 'Eat more fruits'
    logging.info(f"s: {s}")
    logging.info(f"s[0:3]: {s[0:3]}")
    logging.info(f"s[0:3]: {s[3:0]}")
    logging.info(f"s[:5]: {s[:5]}")
    logging.info(f"s[:100]: {s[:100]}")
    logging.info(f"s[4:8:2]: {s[4:8:2]}")
    logging.info(f"s[::3]: {s[::3]}")
    logging.info(f"s[::-1]: {s[::-1]}")
    logging.info(f"s[6:1:-1]: {s[6:1:-1]}")


#  slice assignment
def test_assignment():

    visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
                'Safari', 'corrupted', 'Safari', 'corrupted',
                'Chrome', 'corrupted', 'Firefox', 'corrupted']
    # replace every other string with the string immediately in front of it
    visitors[1::2] = visitors[::2]
    print('\n')
    for k, n in enumerate(visitors):
        print(visitors[k:(k+4)]) if k % 4 == 0 else None


#  extract token from url
def test_unpack_tuple():

    url = "https://m31.earthfiler.com/reset/6a4f7d587435d9355d3026b7459d329499a2b31b"
    print(url.split('/')[-1:] if "reset" in url else 'not found')


# use generator expression to find companies that pay below minimum wage
def test_gen_expression():

    # generator expressions work exactly like list  comprehensions but without creating  list in memory
    companies = {'CoolCompany': {'Alice': 33, 'Bob' : 28, 'Frank' : 29},
                 'CheapCompany': {'Ann': 4, 'Lee': 28, 'Crisi': 7},
                 'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}
                 }
    illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]
    logging.info(f" illegal: {illegal}")


# formatting databases with the zip() function
def test_zip_function():
    column_names = ['name', 'salary', 'job']
    db_rows = [('Alice', 180000, 'data scientist'),
               ('Bob', 99000, 'manager'),
               ('Frank', 87000, 'CEO')]
    db = [dict(zip(column_names, row)) for row in db_rows]

    print()
    logging.info(f'\n {pformat(db)}')


# summary comment
def test_zip():
    zipped = [(1, 4), (2, 5), (3, 6)]
    l1, l2 = zip(*zipped)
    logging.info(f" l1: {l1}")
    logging.info(f" l2: {l2}")

