"""
Tests
"""

import pytest
import datetime
from ..src.analyzer import FileAnalyzer

FILENAME = ["input-file-10000.txt"]
INIT_TSMP = "1565647204351"
END_TSMP = "1565733598341"
HOSTS = ["Aaronjosh"]


@pytest.fixture(scope="module")
def analyzer() -> FileAnalyzer:
    return FileAnalyzer(
        filename=FILENAME,
        init_timestamp=INIT_TSMP,
        end_timestamp=END_TSMP,
        hosts=HOSTS,
    )


def test_data_types(analyzer: FileAnalyzer):
    """
    Test data types correctly loaded
    """
    assert isinstance(analyzer.filename, list)
    assert type(analyzer.init_timestamp) is datetime.datetime
    assert type(analyzer.end_timestamp) is datetime.datetime
    assert isinstance(analyzer.hosts, list)


def test_data_output_for_analyzer(analyzer: FileAnalyzer):
    """
    Check output for given inputs.
    """
    analyzer.start()
    assert len(analyzer.output[HOSTS[0]]) == 11
    assert "Ayania" in analyzer.output[HOSTS[0]]
    assert "Host" not in analyzer.output[HOSTS[0]]
