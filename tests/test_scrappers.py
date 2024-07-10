import pytest

from app.scrapper import Scrapper


@pytest.mark.parametrize(
    "attr",
    ["article_numbers", "run", "url_pattern"]
)
def test_scrapper_has_attribute(attr):
    scrapper = Scrapper("url_pattern")
    assert hasattr(scrapper, attr)
