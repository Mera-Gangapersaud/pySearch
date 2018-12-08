import pytest

from ..search import Search

def test_builtLink():
    tmpSearch = Search()
    tmpSearch.setQuery(["test", "default"])
    assert tmpSearch.buildLink() == "http://www.google.ca/search?q=test+default"
