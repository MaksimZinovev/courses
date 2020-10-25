
import logging


def test_ar_operators():
    x, y = 5, 2
    logging.info(f'x//y = {x//y}')
    # output  2

    logging.info(f'x % y  = {x % y}')
    # output  1


def test_strings():
    logging.info(f'join = {",".join(["F", "B", "I"])}')
    # output:  FBI

def test_keyword_is():
    x = y = 3
    logging.info(f'x is y = {x is y}')
    # output: True

    logging.info(f' [3] is [3] = {[3] is [3]}')
    # output: False


def test_collection():
    # all data types in collection must be hashable
    # cannot create set of lists (unhashable)
    hero = "Harry"
    logging.info(f'hash = {hash(hero)}')
    # output: -4532425695302681083

    # set
    set_example = {1, 3, 4, 6}