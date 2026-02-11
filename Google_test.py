from selenium import webdriver

# Инициализация WebDriver (для Chrome)
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Открытие страницы
driver.get("https://www.example.com")

# Нахождение элемента по имени и ввод текста
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium")

# Нажатие кнопки поиска
search_box.submit()

# Закрытие браузера
driver.quit()