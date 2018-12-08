import pytest

from ..search import Search

def test_builtLinkTwitter():
    tmpSearch = Search()
    tmpSearch.setEngine("twitter")
    tmpSearch.setQuery(["testing", "Twitter", "search"])
    assert tmpSearch.buildLink() == "http://www.twitter.com/search?q=testing%20Twitter%20search"
