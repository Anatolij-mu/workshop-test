from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

try:

    options = Options()

    driver = webdriver.Firefox(service=Service(), options=options)

    driver.get("http://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    time.sleep(2)

    flash_message = driver.find_element(By.ID, "flash")
    message_text = flash_message.text.strip()

    print("Сообщение после входа:", message_text.split("\n")[0])

except Exception as e:
    print("Произошла ошибка:", e)

finally:

    if 'driver' in locals():
        driver.quit()
