from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
driver = webdriver.Firefox(service=Service(), options=options)

try:

    print("Открываем страницу...")
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

    print("Ожидаем завершение загрузки...")
    wait = WebDriverWait(driver, 30)
    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    print(f"Найдено {len(images)} изображений")

    if len(images) < 4:
        raise Exception(f"Загружено недостаточно изображений: {len(images)}/4")

    third_img_src = images[2].get_attribute("src")
    print("Атрибут src 3-й картинки:", third_img_src)

    if not third_img_src:
        raise Exception("Атрибут src третьей картинки пустой")

except Exception as e:
    print("Ошибка:", str(e))
    driver.save_screenshot("error.png")
    print("Скриншот сохранен как error.png")

finally:
    driver.quit()
