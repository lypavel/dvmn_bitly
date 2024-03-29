# Bitly URL shortener

A simple console utility that allows you to shorten long links using the bit.ly service, as well as view the number of clicks on already shortened links.

### How to install

To use the program, you will need a personal token to access the Bitly API. How to get it is described in detail in the [Bitly API documentation](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-).

After getting the token, create an `.env` file in the same directory as `main.py` and put the following line there:
```
BITLY_TOKEN="<your_bitly_token>"
```
where `<your_bitly_token>` is your token.


Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Usage

```
python3 main.py <user_url>
```

- If `<user_url>` is a normal link, it will be shortened to a `https://bit.ly/xxxxxxx` form.
- If `<user_url>` is a short link of the form `https://bit.ly/xxxxxxx`, the number of clicks on it will be shown.
- Otherwise you will get an error message.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).

***

# Сокращение ссылок с помощью Битли

Простая консольная утилита, позволяющая сокращать длинные ссылки с помощью сервиса Bitly, а также просматривать количество переходов по уже сокращённым ссылкам.

### Как установить

Для использования программы вам потребуется персональный токен для доступа к Bitly API. О том, как его получить, подробно написано в [документации к Bitly API](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-).

После получения токена создайте файл `.env` в одной директории с `main.py` и поместите туда следующую строку:
```
BITLY_TOKEN="<your_bitly_token>"
```
где `<your_bitly_token>` это ваш токен.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Использование

```
python3 main.py <user_url>
```

- Если `<user_url>` является обычной ссылкой, то она будет сокращена до вида `https://bit.ly/xxxxxxx`.
- Если `<user_url>` уже является короткой ссылкой вида `https://bit.ly/xxxxxxx`, будет показано количество переходов по ней.
- Во всех остальных случаях вы получите сообщение об ошибке.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).