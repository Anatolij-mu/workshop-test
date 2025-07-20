from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
driver = webdriver.Firefox(service=Service(), options=options)

try:

    driver.get("http://uitestingplayground.com/ajax")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    wait = WebDriverWait(driver, 15)
    message = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    ).text

    print("Текст из плашки:", message)

except Exception as e:
    print("Произошла ошибка:", e)

    driver.save_screenshot("error_screenshot.png")
    print("Скриншот ошибки сохранен как error_screenshot.png")

finally:
    driver.quit()
