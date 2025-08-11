from selenium.webdriver.common.by import By
import allure


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver):
        """
        Инициализация класса CheckoutPage.

        :param driver: WebDriver - экземпляр веб-драйвера для
        взаимодействия с браузером
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить поле First Name значением '{first_name}'")
    def fill_first_name(self, first_name: str) -> None:
        """
        Заполняет поле First Name.

        :param first_name: Имя для заполнения
        :type first_name: str
        :return: None
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    @allure.step("Заполнить поле Last Name значением '{last_name}'")
    def fill_last_name(self, last_name: str) -> None:
        """
        Заполняет поле Last Name.

        :param last_name: Фамилия для заполнения
        :type last_name: str
        :return: None
        """
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    @allure.step("Заполнить поле Zip Code значением '{zip_code}'")
    def fill_zip_code(self, zip_code: str) -> None:
        """
        Заполняет поле Zip Code.
        :param zip_code: Почтовый индекс для заполнения
        :type zip_code: str
        :return: None
        """
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> None:
        """
        Нажимает кнопку Continue для перехода
        к следующему шагу оформления заказа.

        :return: None
        """
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """
        Получает текст с итоговой суммой заказа.

        :return: Текст с итоговой суммой
        :rtype: str
        """
        return self.driver.find_element(*self.total_label).text
