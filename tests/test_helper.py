import pytest

import config

from util.helper import parseDate, getDatesFromFile

@pytest.mark.parametrize("dateIn,expected",
[('02/27/17','2017-02-27'),
 ('June 2, 2018','2018-06-02'),
 ('Jul-13-2016','2016-07-13'),
 ('April 31, 2018', None)])
def test_parseDate(dateIn, expected):
    result = parseDate(dateIn)
    assert result == expected

def test_getDatesFromFile():
    result = getDatesFromFile(config.DefaultConfig.RESOURCE_DATES_FILE)
    assert(result is not None)
    assert(len(result) > 0)
