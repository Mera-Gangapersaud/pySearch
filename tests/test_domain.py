import pytest

from ..search import Search

def test_setDomain():
    tmpSearch = Search()
    tmpSearch.setDomain("org")
    tmpSearch.setQuery(["test", "domain"])
    assert tmpSearch.buildLink() == "http://www.google.org/search?q=test+domain"
