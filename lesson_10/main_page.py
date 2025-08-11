from selenium.webdriver.common.by import By
import allure


class MainPage:
    """Page Object для главной страницы интернет-магазина."""

    def __init__(self, driver):
        """
        Инициализация главной страницы.

        Args:
            driver: WebDriver - экземпляр драйвера для управления браузером
        """
        self.driver = driver
        self.item_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.item_bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.item_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить рюкзак в корзину")
    def add_backpack(self) -> None:
        """Добавляет товар 'Sauce Labs Backpack' в корзину."""
        self.driver.find_element(*self.item_backpack).click()

    @allure.step("Добавить футболку Bolt в корзину")
    def add_bolt_tshirt(self) -> None:
        """Добавляет товар 'Sauce Labs Bolt T-Shirt' в корзину."""
        self.driver.find_element(*self.item_bolt_tshirt).click()

    @allure.step("Добавить комбинезон в корзину")
    def add_onesie(self) -> None:
        """Добавляет товар 'Sauce Labs Onesie' в корзину."""
        self.driver.find_element(*self.item_onesie).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        self.driver.find_element(*self.cart_icon).click()
