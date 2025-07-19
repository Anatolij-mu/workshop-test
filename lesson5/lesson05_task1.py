from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    driver.get("http://uitestingplayground.com/classattr")

    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()

    alert = driver.switch_to.alert
    alert.accept()

    print("Скрипт успешно выполнен")

finally:
    driver.quit()
