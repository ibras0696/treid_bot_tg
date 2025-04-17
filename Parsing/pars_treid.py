
import json
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import fake_useragent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


async def parse_trade_json(value: str, timeframe: str):
    '''
    Функция парсит рынок нужных валют и возвращает в виде словаря.

    :param value: Валюта
    :param timeframe: Временной интервал
    :return: {'data': {'indicators': {'rezume': '_Currencies_Strong_Buy', 'buy': 7, 'sell': 0}, 'averages': {'rezume': '_Currencies_Strong_Buy', 'buy': 12, 'sell': 0}, 'lastUpdateTime': '2025-02-10 15:53:22', 'timeframe': '1m'}}
    '''

    # Фейковый User-Agent для имитации реального пользователя
    user_agent = fake_useragent.UserAgent()
    # Основной словарь для возврата данных
    result_dict = {}

    # Настройка опций для Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Режим без графического интерфейса
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'user-agent={user_agent.random}')  # Случайный User-Agent
    prefs = {"profile.managed_default_content_settings.images": 2}  # Отключение загрузки изображений

    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        # Формирование URL для запроса
        url = f'https://api.investing.com/api/financialdata/technical/analysis/{value}/{timeframe}'
        # Переход на сайт
        driver.get(url)

        # Ожидание загрузки страницы и появления элемента <pre>
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.TAG_NAME, 'pre')))

        # Получение HTML-кода страницы
        page_source = driver.page_source

        # Парсинг HTML с помощью BeautifulSoup
        soup = BeautifulSoup(page_source, 'lxml')
        # Преобразование текста внутри <pre> в словарь
        data = json.loads(soup.find('pre').text)

        # Извлечение данных из технических индикаторов
        indicators_rezume = data['indicators']['summary']['value']  # Резюме индикаторов
        indicators_buy = data['indicators']['summary']['buy']  # Количество сигналов на покупку
        indicators_sell = data['indicators']['summary']['sell']  # Количество сигналов на продажу

        # Извлечение данных из скользящих средних
        averages_rezume = data['movingAverages']['summary']['value']  # Резюме скользящих средних
        averages_buy = data['movingAverages']['summary']['buy']  # Количество сигналов на покупку
        averages_sell = data['movingAverages']['summary']['sell']  # Количество сигналов на продажу

        # Получение времени последнего обновления
        lastUpdateTime = data['lastUpdateTime']
        time_format = '%Y-%m-%d %H:%M:%S'

        # Преобразование строки времени в объект datetime
        dt = datetime.strptime(lastUpdateTime, time_format)
        # Корректировка времени (уменьшение на 3 часа)
        new_dt = dt - timedelta(hours=-3)
        # Форматирование времени в нужный формат
        new_last_update = new_dt.strftime('%d-%m-%Y %H:%M:%S')

        # Словарь для перевода терминов с английского на русский
        language_dict = {
            'Sell': 'Продажа',
            'sell': 'Продажа',
            'Buy': 'Покупка',
            'buy': 'Покупка',
            'Neutral': 'Нейтрально',
            'neutral': 'Нейтрально',
            '_Currencies_Strong_Sell': 'Сильная Продажа',
            '_Currencies_Strong_Buy': 'Сильная Покупка',
            '_Currencies_Neutral': 'Сильно Нейтрально',
            '_moving_avarge_tool_sell': 'Среднее Продажа',
            '_moving_avarge_tool_buy': 'Среднее Покупка',
            '_moving_avarge_tool_neutral': 'Среднее Нейтрально',
        }

        # Формирование итогового словаря с данными
        result_dict['data'] = {
            'indicators': {
                'rezume': language_dict.get(indicators_rezume),  # Резюме индикаторов
                'buy': indicators_buy,  # Количество сигналов на покупку
                'sell': indicators_sell  # Количество сигналов на продажу
            },
            'averages': {
                'rezume': language_dict.get(averages_rezume),  # Резюме скользящих средних
                'buy': averages_buy,  # Количество сигналов на покупку
                'sell': averages_sell  # Количество сигналов на продажу
            },
            'lastUpdateTime': new_last_update,  # Время последнего обновления
            'timeframe': data['timeframe']  # Временной интервал
        }
    except Exception as ex:
        # Логирование ошибки и возврат пустого словаря в случае исключения
        print(f'Ошибка: {ex}')
        return {}
    finally:
        # Закрытие драйвера, если он был успешно создан
        if 'driver' in locals():
            driver.quit()

    return result_dict


