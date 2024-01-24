import requests as rq
import os
from urllib.parse import urlparse, ParseResult
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
        "Authorization": f"Bearer {os.environ["TOKEN"]}"
    }

def shorten_link(url: str, headers: dict) -> str | rq.exceptions.HTTPError | None:
    api_url = "https://api-ssl.bitly.com/v4/shorten"

    payload = {
        "long_url": url
    }

    response = rq.post(api_url, headers=headers, json=payload)
    try:
        response.raise_for_status()
    except rq.exceptions.HTTPError as http_error:
        return http_error

    return response.json().get("link")

def count_clicks(link: str, headers: dict) -> int | str | rq.exceptions.HTTPError:
    parsed_link = parse_url(link)
    bitlink = link = f"{parsed_link.netloc}{parsed_link.path}"
    api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    
    response = rq.get(api_url, headers=headers)
    try:
        response.raise_for_status()
    except rq.exceptions.HTTPError as http_error:
        return http_error

    return response.json().get("total_clicks")

def parse_url(url: str) -> ParseResult:
    return urlparse(url)

def is_bitlink(url: str, headers: dict) -> bool:
    parsed_link = parse_url(url)
    bitlink = f"{parsed_link.netloc}{parsed_link.path}"
    bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"

    response = rq.get(bitly_url, headers=headers)

    return response.ok


if __name__ == "__main__":
    user_url = input("Введите ссылку: ")

    if is_bitlink(user_url, HEADERS): 
        print(f"Количество переходов: {count_clicks(user_url, HEADERS)}")
    else: 
        print(f"Сокращённая ссылка: {shorten_link(user_url, HEADERS)}")