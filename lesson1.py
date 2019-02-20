#!/usr/bin/env python3
"""
retrieve and print words from a url

usage:
    py lesson1.py <url>
"""

from urllib.request import urlopen
import sys


def fetch_words(url):
    """fetch a list of words from a url.

    Args:
        url: the url of a utf-8 text document

    Returns:
        a list of strings containing the words from the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """print items 1 per line

        Args:
            an iterable series of printable items
        """
    for word in items:
        print(word)


def main(url):
    """print each wprd from a text document from a url

        Args:
            url: the url of a utf-8 text document
        """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # the 0th arg is the module filename
