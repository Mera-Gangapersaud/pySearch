import pytest

from ..search import Search

def test_builtLinkAmazon():
    tmpSearch = Search()
    tmpSearch.setEngine("amazon")
    tmpSearch.setQuery(["testing", "Amazon", "query"])
    assert tmpSearch.buildLink() == "http://www.amazon.ca/s/keywords=testing%20Amazon%20query"
