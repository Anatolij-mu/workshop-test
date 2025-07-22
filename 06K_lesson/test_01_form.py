import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


@pytest.fixture
def driver():

    service = Service(executable_path="06K_lesson/msedgedriver.exe")
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_fill_form(driver):

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_class = driver.find_element(
        By.ID, "zip-code").get_attribute("class")
    assert "alert-danger" in zip_code_class

    fields_to_check = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "company"
    ]

    for field_id in fields_to_check:
        field_class = driver.find_element(
            By.ID, field_id).get_attribute("class")
        assert "alert-success" in field_class
