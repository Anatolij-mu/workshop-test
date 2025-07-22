from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator_with_delay():
    driver = webdriver.Chrome()
    try:
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        driver.get(url)

        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        result = WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )
        assert result, ("Результат 15 не отобразился "
                        "после 45 секунд ожидания")

    finally:
        driver.quit()
