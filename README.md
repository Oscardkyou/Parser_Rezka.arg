# Проект "Интеллектуальный Парсер Информации о Фильмах"

## Обзор

Данный проект предназначен для умного и быстрого сбора данных о кинофильмах с заданного веб-сайта. Скрипт эффективно извлекает данные о названиях фильмов и соответствующих им изображениях, сохраняя всю полученную информацию в формате JSON для последующей удобной обработки и использования.

## Технологический стек

- **Python**: Основной язык программирования проекта.
- **BeautifulSoup**: Мощная библиотека для парсинга HTML и XML документов.
- **Requests**: Библиотека для отправки HTTP-запросов.
- **lxml**: Высокопроизводительная библиотека для обработки XML и HTML.

## Установка и Настройка

### Шаг 1: Клонирование репозитория
Клонируйте репозиторий, используя следующую команду:
```sh
git clone ссылка_на_ваш_репозиторий

Шаг 2: Установка виртуального окружения

Создайте и настройте виртуальное окружение с помощью команды:

sh

python -m venv env

Шаг 3: Активация виртуального окружения

Активируйте виртуальное окружение с помощью следующей команды:

    Для Windows:

sh

.\env\Scripts\activate

    Для Linux/MacOS:

sh

source env/bin/activate

Шаг 4: Установка зависимостей

Установите все необходимые зависимости, выполнив команду:

sh

pip install -r requirements.txt

Использование

Перед запуском убедитесь, что файл .env корректно настроен с нужными переменными окружения (URL, DOMEN).

Затем, запустите скрипт следующей командой:

sh

python main.py

Результаты парсинга будут сохранены в файле core/json/content.json.
