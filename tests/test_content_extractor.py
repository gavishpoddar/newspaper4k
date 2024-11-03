import pytest
from newspaper.extractors.content_extractor import ContentExtractor
from newspaper.configuration import Configuration
import newspaper.parsers as parsers


@pytest.fixture
def sample_html():
    html_content = """
    <html>
        <body>
            <div>
                <p>Starting node</p>
                <p>Ending node</p>
            </div>
        </body>
    </html>
    """
    return html_content


def test_get_starting_node_xpath(sample_html):
    config = Configuration()
    extractor = ContentExtractor(config)
    doc = parsers.fromstring(sample_html)
    top_node = extractor.calculate_best_node(doc)
    starting_node_xpath = extractor.get_starting_node_xpath(top_node)
    assert starting_node_xpath is not None
    assert starting_node_xpath.startswith("/html")


def test_get_ending_node_xpath(sample_html):
    config = Configuration()
    extractor = ContentExtractor(config)
    doc = parsers.fromstring(sample_html)
    top_node = extractor.calculate_best_node(doc)
    ending_node_xpath = extractor.get_ending_node_xpath(top_node)
    assert ending_node_xpath is not None
    assert ending_node_xpath.startswith("/html")
