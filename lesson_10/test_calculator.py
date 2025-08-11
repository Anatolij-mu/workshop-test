import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import allure


@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка работы калькулятора с задержкой")
@allure.description(
    "Тест проверяет корректность вычислений с установленной задержкой")
def test_calculator(browser):
    with allure.step("Открытие страницы калькулятора"):
        calculator = CalculatorPage(browser)
        browser.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    with allure.step("Установка задержки вычислений"):
        calculator.set_delay(45)

    with allure.step("Ввод выражения 7 + 8"):
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')

    with allure.step("Запуск вычисления"):
        calculator.click_button('=')

    with allure.step("Проверка результата"):
        result = calculator.get_result(46)  # Получаем текст результата
        assert result == "15", f"Ожидался результат '15', получено '{result}'"
