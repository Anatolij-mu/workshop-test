# Тестовый проект с Allure отчетами

Этот проект содержит автоматизированные тесты для веб-приложений с использованием Selenium WebDriver и генерацией отчетов Allure.

Установка:

1.  Установите зависимости:
   
   pip install -r requirements.txt
Убедитесь, что у вас установлен браузер Chrome и соответствующая версия ChromeDriver

Запуск тестов
Для запуска тестов с генерацией Allure отчетов выполните:

pytest --alluredir=allure_results
  
Просмотр отчетов
После выполнения тестов сгенерируйте отчет:

allure serve allure_results
Отчет откроется автоматически в вашем браузере по умолчанию

Структура проекта
calculator_page.py - Page Object для страницы калькулятора

cart_page.py - Page Object для страницы корзины

checkout_page.py - Page Object для страницы оформления заказа

login_page.py - Page Object для страницы авторизации

main_page.py - Page Object для главной страницы

test_calculator.py - Тесты для калькулятора

test_total_price.py - Тесты для проверки итоговой суммы заказа