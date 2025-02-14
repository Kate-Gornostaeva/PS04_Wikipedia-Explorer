from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

# Стек для хранения истории переходов
history_stack = []

def search_wikipedia(query):
    """Переходит на страницу Википедии по запросу."""
    browser.get(f'https://ru.wikipedia.org/wiki/{query}')
    time.sleep(3)  # Подождите, чтобы страница полностью загрузилась

def list_paragraphs():
    """Выводит параграфы текущей статьи группами по 20 с запросом на продолжение."""
    try:
        # Получите все параграфы статьи
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        total_paragraphs = len(paragraphs)
        start_index = 0
        group_size = 20  # Количество параграфов для вывода за один раз

        while start_index < total_paragraphs:
            # Выводим группу параграфов
            for i in range(start_index, min(start_index + group_size, total_paragraphs)):
                print(f"{i + 1}: {paragraphs[i].text}\n")

            start_index += group_size

            # Если есть еще параграфы, спрашиваем пользователя
            if start_index < total_paragraphs:
                continue_input = input("Продолжать? (д/н): ").strip().lower()
                if continue_input != 'д':
                    break  # Прекращаем вывод, если пользователь ввел не "д"
            else:
                print("Все параграфы статьи выведены.")
    except Exception as e:
        print(f"Ошибка при получении параграфов: {e}")

def choose_related_page():
    """Предлагает пользователю выбрать одну из связанных страниц."""
    try:
        # Получите все ссылки на связанные страницы (внутренние ссылки)
        links = browser.find_elements(By.CSS_SELECTOR, 'a[href^="/wiki/"]')

        # Фильтрация ссылок, исключая служебные страницы
        filtered_links = [
            link for link in links
            if not link.get_attribute('title') or not any(
                word in link.get_attribute('title') for word in ["Обсуждение", "Правка", "Категория"]
            )
        ]

        if filtered_links:
            print("Выберите одну из связанных страниц:")
            for i, link in enumerate(filtered_links[:20]):  # Ограничим до 10 ссылок для удобства
                print(f"{i + 1}: {link.text}")

            choice = int(input("Введите номер страницы для перехода: ")) - 1
            if 0 <= choice < len(filtered_links):
                # Сохраняем текущий URL в стек перед переходом
                history_stack.append(browser.current_url)
                related_link = filtered_links[choice].get_attribute('href')
                browser.get(related_link)
                time.sleep(3)  # Подождите, чтобы страница полностью загрузилась
                return True  # Успешный переход
            else:
                print("Неверный выбор.")
                return False
        else:
            print("Нет связанных страниц.")
            return False
    except Exception as e:
        print(f"Ошибка при выборе связанной страницы: {e}")
        return False


def handle_article():
    """Обрабатывает действия пользователя на текущей странице."""
    while True:
        print("\nВыберите действие:")
        print("1: Листать параграфы текущей статьи")
        print("2: Перейти на одну из связанных страниц")
        print("3: Вернуться на предыдущую страницу")
        print("4: Выйти из программы")

        action = input("Введите номер действия: ")

        if action == '1':
            list_paragraphs()
        elif action == '2':
            if choose_related_page():
                handle_article()  # Рекурсивно обрабатываем новую страницу
        elif action == '3':
            if history_stack:
                previous_url = history_stack.pop()  # Извлекаем последний URL из стека
                browser.get(previous_url)  # Возвращаемся на предыдущую страницу
                time.sleep(3)  # Подождите, чтобы страница полностью загрузилась
            else:
                print("Нет предыдущей страницы для возврата.")
        elif action == '4':
            print("Программа завершена. До свидания!")
            browser.quit()
            exit()  # Завершение программы
        else:
            print("Неверный выбор. Попробуйте снова.")

def main():
    """Основная функция программы."""
    while True:
        initial_query = input("Введите запрос для поиска в Википедии: ")
        search_wikipedia(initial_query.replace(" ", "_"))  # Заменяем пробелы на подчеркивания
        handle_article()  # Обрабатываем действия на текущей странице


if __name__ == "__main__":
    main()
