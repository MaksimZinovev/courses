import re

import logging
from pprint import pformat
from typing import List


def item_per_line(items: List[str])-> str:
    """Format string so that each  """

    return '\n'+"\n".join(items)


article = [
    "http://blog.finxter.com/frequently-asked-questions/",
    "http://blog.finxter.com/about/",
    "http://blog.finxter.com/",
    "https://blog-finxter-com/",
    ]

if __name__ == '__main__':
    print(item_per_line(article))
