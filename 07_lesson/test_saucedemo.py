import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_total_price(driver):
    # Открываем сайт и авторизуемся
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    main_page.add_backpack()
    main_page.add_bolt_tshirt()
    main_page.add_onesie()
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_zip_code("12345")
    checkout_page.click_continue()

    total = checkout_page.get_total()
    assert total == "Total: $58.29"
