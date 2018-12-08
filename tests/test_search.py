import pytest

from ..search import Search

def test_builtLinkAmazon():
    tmpSearch = Search()
    tmpSearch.setEngine("amazon")
    tmpSearch.setDomain("com")
    tmpSearch.setQuery(["testing", "Amazon", "query"])
    assert tmpSearch.buildLink() == "http://www.amazon.com/s/keywords=testing%20Amazon%20query"

def test_builtLinkTwitter():
    tmpSearch = Search()
    tmpSearch.setEngine("twitter")
    tmpSearch.setDomain("com")
    tmpSearch.setQuery(["testing", "Twitter", "search"])
    assert tmpSearch.buildLink() == "http://www.twitter.com/search?q=testing%20Twitter%20search"

def test_builtLink():
    tmpSearch = Search()
    tmpSearch.setQuery(["test", "default"])
    assert tmpSearch.buildLink() == "http://www.google.ca/search?q=test+default"

def test_setDomain():
    tmpSearch = Search()
    tmpSearch.setDomain("org")
    tmpSearch.setQuery(["test", "domain"])
    assert tmpSearch.buildLink() == "http://www.google.org/search?q=test+domain"