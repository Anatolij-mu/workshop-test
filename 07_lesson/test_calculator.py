import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(browser):
    calculator = CalculatorPage(browser)
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    calculator.set_delay(45)
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    assert calculator.get_result(46), "Result should be 15 after 45 seconds"
