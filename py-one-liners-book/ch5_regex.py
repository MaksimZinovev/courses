import logging
import re
from pprint import pformat

from utils.one_item_per_line import item_per_line


def test_asterisk():
    """ Match the text that begins and ends with the character 'y'
    and arbitrary number of characters in between.

    """
    text = """ Cryptography is a method of protecting information 
    and communications through the use of codes, so that only 
    those for whom the information is intended can read and process it. 
    The prefix "crypt-" means "hidden" or "vault" -- and the suffix "-graphy" stands for "writing."
    """

    logging.info(f" result: {re.findall('y.*y', text)}")


def test_zero_or_one_regex():
    """ Applies to the regex immediately in front of it.

    """
    text = """ Block, blockchain, blocked.
    """

    logging.info(f" result: {re.findall('block?', text)}")


def test_non_greedy_matching():
    """ Searches for a minimal number of arbitrary  characters.

    """
    text = """peter piper picked a peck of pickled pepper    """

    logging.info(f" non-greedy result: {re.findall('p.*?e.*?r', text)}")
    logging.info(f" greedy result: {re.findall('p.*e.*r', text)}")


def test_scrape_occurencies_smartly():
    """ Searches word 'crypto' followed by up to 30 arbitrary characters, followed by the word 'coin'.
        Important: case sensitive!
        Important: should start from word Bit!
    """
    text = """Bitcoin, Litecoin, Ethereum, and other cryptocurrencies don't just fall out of the sky. 
    Like any other form of money, it takes work to produce them. And that work comes in the form of mining.
    But let's take a step back. Satoshi Nakamoto, the founder of Bitcoin, ensured that there would 
    ever only be 21 million Bitcoins in existence. He (or they) reached that figure by calculating that 
    people would discover, or "mine," a certain number of blocks of transactions each day. Every four years, 
    the number of Bitcoins released in relation to the previous cycle gets reduced by 50%, along with the 
    reward to miners for discovering new blocks. At the moment, that reward is 12.5 Bitcoins. 
    Therefore, the total number of Bitcoins in circulation will approach 21 million but never actually 
    reach that figure. This means Bitcoin will never experience inflation. The downside here is that a 
    hack or cyberattack could be a disaster because it could erase Bitcoin wallets with little hope of 
    getting the value back."""

    pattern1 = re.compile("Bit(.{1,40})coin")
    logging.info(f'result: {pattern1.match(text)}')

    pattern2 = re.compile("Lite(.{1,240})and")
    logging.info(f'result: {pattern2.match(text)}')


"""
Basic Regex expressions:
    - the dot regex .  matches arbitrary character
    - the asterisk regex <pattern>* matches an arbitrary number of the regex <pattern>. 
      This includes zero matching instances.
    - the at-least--one regex <pattern>+ can match an arbitrary number of  <pattern> but must match
      at least one instance.
    - the zero-or-one regex <pattern>?  matches either zero or one instance of <pattern>.
    - the nongreedy asterisk regex *? matches as few arbitrary characters as possible to match the overal regex.
    - the regex <pattern>{m} matches exactly m copies of <pattern>.
    - the regex <pattern>{m,n} matches between m and n copies of <pattern>.
    - the regex <pattern1 | pattern2> matches either <pattern1> or <pattern2>.
    - the regex <pattern1><pattern2> matches <pattern1> and then <pattern2>.
    - the regex (<pattern>) matches <pattern> and then <pattern2>. The parentheses group regular expressions so you
      can control the order of execution
    
"""


def test_match_search_findall_compared():
    """ Compare results of re.match(), re.search() and re.findall()	"""
    text = """November is the eleventh month of the year in the Julian and 
    Gregorian Calendars, the fourth and last of four months to have a length of 
    30 days and the fifth and last of five months to have a length of fewer than 31 days
    - re.match() looks for the pattern ONLY at the beginning of the string,
    - re.search() searches for the first occurence of the regex anywhere in the string,
    - re.findall() retreives all  matched patterns
    """
    regex = 'month'

    logging.info(f're.match(): {re.match(regex, text)}')
    logging.info(f're.search(): {re.search(regex, text)}')
    logging.info(f're.match(): {re.findall(regex, text)}')

    """
    output:
    17:55:40 INFO re.match(): None
    17:55:40 INFO re.search(): <re.Match object; span=(25, 30), match='month'>
    17:55:40 INFO re.match(): ['month', 'month', 'month']
    """


def test_find_all_hyperlinks_that_contain_words():
    """ Find all hyperlinks that point to finxter.com and the strings 'Blog' and 'FAQ'
    - use pattern '.*?' to math an arbitrary number of characters non-greedily
    """

    page = """ 
          <a id="blogNav" href="https://blog.finxter.com/pricing/" target="_blank" class="w3-bar-item w3-button input" title="Pricing">
        <i class="fa fa-book fa-fw w3-margin-right"></i>
        Pricing
      </a>
      
      <a id="blogNav" href="https://blog.finxter.com/" target="_blank" class="w3-bar-item w3-button input" title="Blog">
        <i class="fa fa-cube fa-fw w3-margin-right"></i>
        Blog
      </a>
      <a id="acadNav" href="https://academy.finxter.com/" target="_blank" class="w3-bar-item w3-button input" title="Jobs">
        <i class="fa fa-dollar fa-fw w3-margin-right"></i>
        Academy
      </a>
      <a id="faqNav" href="https://blog.finxter.com/frequently-asked-questions/" target="_blank" class="w3-bar-item w3-button input" title="FAQ">
        <i class="fa fa-question fa-fw w3-margin-right"></i>
        FAQ
      </a>
      <a id="aboutNav" href="https://blog.finxter.com/about/" target="_blank" class="w3-bar-item w3-button input" title="About">
        <i class="fa fa-gears fa-fw w3-margin-right"></i>
    """

    logging.info(f'links found: {re.findall("(<a.*?finxter.com.*?(Blog|FAQ).*?>)", page)}')


def test_find_all_occurencies_of_dollar_amounts_with_optional_decimal_values():
    """ Find all occurrences of dollar amounts with optional decima lvalues.
    - escaped '\$' (because '$' is a special regex character)
    - escaped '\.' (because '.' is a special regex character)
    """
    report = """
    $5,000.00 
    $3244.35
    $2,342,235.00

    $1.00
    $123.00
    $1.23
    
    
    1.00
    23.00
    0.23
    """
    dollars = [x[0] for x in re.findall("(\$[0-9,0-9]+(\.[0-9]*)?)", report)]
    logging.info('\n' + '\n'.join(dollars))


def test_find_valid_urls_starts_with_http():
    """ Find all occurrences that
    - start with http://
    - are valid urls only: should be at least one top-level domain
    """

    article = """
    http://blog.finxter.com/frequently-asked-questions/
    http://blog.finxter.com/about/
    http://blog.finxter.com/
    https://blog-finxter-com/
    
    """
    logging.info("stale links:")
    logging.info('\n'+"\n".join(re.findall('http://[a-z0-9_\-.]+[a-z0-9_\-/]+', article)))


def test_validate_time_format():
    """ Check that string has the time format XX:XX where X is the number from 0 to 9.
    For now, it can accept wrong time formats such as 12:86
    """

    inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

    input_ok = lambda x: re.fullmatch('[0-9]{2}:[0-9]{2}', x) is not None

    for x in inputs:
        logging.info(input_ok(x))


def test_validate_time_format_smarter():
    """ Check that string has the time format XX:XX where X is the number from 0 to 9.
    Such inputs as 99:99 should not be considered valid.
    """

    inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

    input_ok = lambda x: re.fullmatch('([01][0-9]|2[0-3]):[0-5][0-9]', x) is not None

    for x in inputs:
        logging.info(input_ok(x))


def test_detect_words_that_contain_duplicate_characters():
    """ Demonstrate how to reuse parts you've already matched - named groups.
    Syntax:
    (?P<name>...)
    """

    text = """November is the eleventh month of the year in the Julian and 
        Gregorian Calendars, the fourth and last of four months to have a length of 
        30 days and the fifth and last of five months to have a length of fewer than 31 days
        - re.match() looks for the pattern ONLY at the beginning of the string,
        - re.search() searches for the first occurence of the regex anywhere in the string,
        - re.findall() retreives all  matched patterns
        """
    duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)
    logging.info("\n" + pformat(duplicates))

# Page 10
