from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():
    # Настройка опций Chrome для стабильности и маскировки автоматизации
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = None
    try:
        # Инициализация драйвера с автоматической загрузкой актуальной версии
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        wait = WebDriverWait(driver, 15)

        # Шаг 1: Открытие сайта
        print("Открываем сайт...")
        driver.get("https://www.litres.ru")

        # Шаг 2: Закрытие всплывающего окна (если появится)
        try:
            # Универсальные селекторы для кнопок закрытия попапов
            popup_selectors = [
                "button[aria-label*='Закрыть' i]",
                ".popup-close",
                ".close-popup",
                "[data-testid='close-popup']",
                "button.close"
            ]
            for selector in popup_selectors:
                try:
                    close_btn = wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    close_btn.click()
                    time.sleep(0.5)  # Небольшая пауза после закрытия
                    print("Всплывающее окно закрыто.")
                    break
                except (TimeoutException, NoSuchElementException):
                    continue
        except Exception as e:
            print(f"Информация: всплывающее окно не обнаружено или не удалось закрыть ({e})")

        # Шаг 3: Поиск элемента поиска и ввод запроса
        print("Выполняем поиск...")
        try:
            # Основной селектор + резервные варианты
            search_input = wait.until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "input[placeholder*='Поиск' i], input[type='search'], .search-input input"
                ))
            )
            search_input.clear()
            search_input.send_keys("Пушкин")

            # Шаг 4: Нажатие кнопки поиска или отправка формы
            try:
                search_btn = driver.find_element(
                    By.CSS_SELECTOR,
                    "button[type='submit'], .search-button, button[aria-label*='Поиск' i]"
                )
                search_btn.click()
            except NoSuchElementException:
                # Резервный вариант: отправка через Enter
                search_input.send_keys("\ue007")  # Код клавиши Enter

            # Шаг 5: Ожидание загрузки результатов
            print("Ожидание результатов поиска...")
            wait.until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "article.art_item, div[data-testid='art_item'], .search-results article"
                ))
            )
            time.sleep(1)  # Дополнительная пауза для полной отрисовки

            # Шаг 6: Извлечение названий книг
            # Универсальные селекторы для названий (актуально для Литрес 2025-2026)
            book_titles = driver.find_elements(
                By.CSS_SELECTOR,
                "a.art__name__href, .art__name a, [data-testid='art__name'] a, .biblio_book_name a"
            )

            # Фильтрация пустых и дублирующих названий
            unique_titles = []
            for el in book_titles:
                text = el.text.strip()
                if text and text not in unique_titles:
                    unique_titles.append(text)
                    if len(unique_titles) == 5:
                        break

            # Шаг 7: Вывод результатов
            print("\nПервые 5 книг по запросу 'Пушкин':")
            if unique_titles:
                for i, title in enumerate(unique_titles, 1):
                    print(f"{i}. {title}")
            else:
                print("Книги не найдены. Возможные причины:")
                print("- Изменилась структура сайта")
                print("- Требуется ручная проверка CAPTCHA")
                print("- Запрос вернул пустой результат")

        except TimeoutException:
            print("Ошибка: не удалось дождаться элементов поиска или результатов.")
        except Exception as e:
            print(f"Ошибка при работе с поиском: {type(e).__name__}: {e}")

    except WebDriverException as e:
        print(f"Критическая ошибка WebDriver: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {type(e).__name__}: {e}")
    finally:
        # Корректное завершение работы
        if driver:
            print("\nЗавершение работы браузера...")
            driver.quit()
            print("Браузер закрыт.")


if __name__ == "__main__":
    main()