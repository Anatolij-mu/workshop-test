from selenium.webdriver.common.by import By
import allure


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver):
        """
        Инициализация класса CartPage.

        :param driver: WebDriver - экземпляр веб-драйвера для взаимодействия
        с браузером
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку Checkout на странице корзины.

        :return: None
        """
        self.driver.find_element(*self.checkout_button).click()
