from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    ajax_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton")))
    ajax_button.click()

    success_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))

    print("Текст из зеленой плашки:", success_message.text)

except TimeoutException:
    print("Элемент не появился в течение заданного времени")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
finally:
    driver.quit()
