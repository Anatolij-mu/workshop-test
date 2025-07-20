from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/dynamicid")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    sleep(2)

    print("Действие выполнено успешно!")

finally:

    driver.quit()
