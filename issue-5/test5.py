from year import what_is_year_now
import pytest
import json
from unittest.mock import patch


def test_year_ymd():
    exp_year = 2021
    with patch.object(json, 'loads', return_value={'currentDateTime': '2021-12-01T17:31Z'}):
        year = what_is_year_now()
    assert exp_year == year


def test_year_dmy():
    exp_year = 2021
    with patch.object(json, 'loads', return_value={'currentDateTime': '01.12.2021T17:31Z'}):
        year = what_is_year_now()
    assert exp_year == year


def test_year_exception():
    with patch.object(json, 'loads', return_value={'currentDateTime': '20211201'}):
        with pytest.raises(ValueError):
            _ = what_is_year_now()
