from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Настройка Firefox
options = Options()
driver = webdriver.Firefox(service=Service(), options=options)

try:
    # 1. Переход на страницу
    driver.get("http://uitestingplayground.com/textinput")

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    updated_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "updatingButton").text == "SkyPro"
    )
    button_text = driver.find_element(By.ID, "updatingButton").text

    print("Текст кнопки:", button_text)

except Exception as e:
    print("Произошла ошибка:", e)
    driver.save_screenshot("error.png")
    print("Скриншот ошибки сохранен как error.png")

finally:
    driver.quit()
