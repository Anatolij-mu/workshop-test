import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage
import allure


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    with allure.step("Инициализация браузера"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()


@allure.feature("Проверка общей стоимости заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест проверки итоговой стоимости товаров")
@allure.description(
    "Проверка корректного расчета общей стоимости выбранных товаров")
def test_total_price(driver):
    with allure.step("Открытие сайта и авторизация"):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(driver)
        main_page.add_backpack()
        main_page.add_bolt_tshirt()
        main_page.add_onesie()
        main_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнение информации для оформления"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_first_name("John")
        checkout_page.fill_last_name("Doe")
        checkout_page.fill_zip_code("12345")
        checkout_page.click_continue()

    with allure.step("Проверка итоговой стоимости"):
        total = checkout_page.get_total()
        assert total == "Total: $58.29"
        f"Ожидаемая сумма: $58.29, Фактическая: {total}"
