# 📈 Торговый бот для Telegram

Бот для анализа рыночных данных с интеграцией в Telegram

## ⚙️ Технические требования
- Python 3.12
- Хромдрайвер для Selenium
- Доступ к Telegram API

## 🛠 Установка

### 1. Установите зависимости:

pip install -r requirements.txt

# Установка библиотек
```bash
pip install -r requirments.txt
```

# Создание файла .env
в .env создайте две переменные
в файле test.env показан пример

    TOKEN="Ваш токен"
    ADMIN1=Телеграм айди админа


# Начало
Пользователь вводит команду /start
![img.png](Utils/img/img1.png)

После пользователь ждёт подтверждения
![img.png](Utils/img/img2.png)

# Действие Админа
Админу приходит такое сообщение
![img.png](Utils/img/img3.png)

Подтверждает и ставит статус нужный
![img.png](Utils/img/img4.png)

после пользователю поступает сообщение
![img.png](Utils/img/img5.png)

иначе 
![img.png](Utils/img/img6.png)


# Пользование
Предлагают нужную волюту
![img.png](Utils/img/img7.png)
Выбор интервала
![img.png](Utils/img/img8.png)
Идет Сбор данных и выдача 
![img.png](Utils/img/img9.png)