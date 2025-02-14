# Wikipedia Explorer

**Wikipedia Explorer** — это консольная программа на Python, которая позволяет искать информацию на Википедии, листать параграфы статей и переходить на связанные страницы. Программа использует Selenium для автоматизации браузера и взаимодействия с сайтом Википедии.

## Возможности

- Поиск статей на Википедии по запросу пользователя.
- Листание параграфов статьи с возможностью вывода групп по 20 параграфов.
- Переход на связанные страницы с фильтрацией служебных ссылок (например, "Обсуждение", "Правка").
- Возврат на предыдущую страницу с использованием истории переходов.
- Удобный интерфейс для взаимодействия через консоль.

## Установка

1. Убедитесь, что у вас установлен Python 3.7 или выше.
2. Установите необходимые зависимости:

   ```bash
   pip install selenium
   
3. Скачайте ChromeDriver, совместимый с вашей версией Google Chrome, и укажите путь к нему в переменной окружения CHROMEDRIVER_PATH.
- Скачать ChromeDriver можно с официального сайта.
- Установите переменную окружения:

```bash
export CHROMEDRIVER_PATH=/path/to/chromedriver
```

(Для Windows используйте set вместо export.)

## Использование
Запустите программу:

```bash
python wikipedia_explorer.py
```

Введите запрос для поиска на Википедии.

Выберите действие:
1: Листать параграфы текущей статьи.

2: Перейти на одну из связанных страниц.

3: Вернуться на предыдущую страницу.

4: Выйти из программы.

Следуйте инструкциям на экране.

## Пример работы
Введите запрос, например, "Python".

Программа откроет статью о Python на Википедии.

Выберите "1", чтобы листать параграфы статьи.

Выберите "2", чтобы перейти на связанную страницу, например, "Программирование".

Выберите "3", чтобы вернуться на предыдущую страницу.

Выберите "4", чтобы завершить программу.

 ## Структура проекта
wikipedia_explorer.py — основной файл программы.

README.md — документация проекта.

## Зависимости
Selenium — для автоматизации браузера.

ChromeDriver — драйвер для управления браузером Google Chrome.

## Лицензия
Этот проект распространяется под лицензией MIT. См. файл LICENSE для получения дополнительной информации.
