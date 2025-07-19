import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# Тесты для capitalize
def test_capitalize_positive(utils):
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("123abc") == "123abc"


def test_capitalize_negative(utils):
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# Тесты для trim
def test_trim_positive(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello  ") == "hello  "
    assert utils.trim("text") == "text"


def test_trim_negative(utils):
    assert utils.trim("") == ""
    assert utils.trim(" ") == ""
    with pytest.raises(AttributeError):
        utils.trim(None)


# Тесты для contains
def test_contains_positive(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "Pro") is True
    assert utils.contains("123", "2") is True


def test_contains_negative(utils):
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("", "a") is False
    assert utils.contains(" ", " ") is True
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


# Тесты для delete_symbol
def test_delete_symbol_positive(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("ababab", "a") == "bbb"


def test_delete_symbol_negative(utils):
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol(" ", " ") == ""
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
