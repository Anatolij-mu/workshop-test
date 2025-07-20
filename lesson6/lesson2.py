from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

try:

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
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    button_text = driver.find_element(By.ID, "updatingButton").text

    print(button_text)

finally:

    driver.quit()
