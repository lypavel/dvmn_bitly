import requests as rq
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

def shorten_link(url: str, headers: dict) -> str | None:
    api_url = "https://api-ssl.bitly.com/v4/shorten"

    payload = {
        "long_url": url
    }

    response = rq.post(api_url, headers=headers, json=payload)

    response.raise_for_status()

    return response.json().get("link")

def count_clicks(link: str, headers: dict) -> int | None:
    parsed_link = urlparse(link)
    bitlink = link = f"{parsed_link.netloc}{parsed_link.path}"
    api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    
    response = rq.get(api_url, headers=headers)

    response.raise_for_status()

    return response.json().get("total_clicks")

def is_bitlink(url: str, headers: dict) -> bool:
    parsed_link = urlparse(url)
    bitlink = f"{parsed_link.netloc}{parsed_link.path}"
    bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"

    response = rq.get(bitly_url, headers=headers)

    return response.ok


if __name__ == "__main__":

    load_dotenv()

    HEADERS = {
            "Authorization": f"Bearer {os.environ["BITLY_TOKEN"]}"
    }

    user_url = input("Введите ссылку: ")

    if is_bitlink(user_url, HEADERS):
        try:
            clicks_count = count_clicks(user_url, HEADERS)
        except rq.exceptions.HTTPError as http_error:
            print(http_error)
        else:
            print(f"Количество переходов: {clicks_count}")
    else:
        try:
            shortened_link = shorten_link(user_url, HEADERS)
        except rq.exceptions.HTTPError as http_error:
            print(http_error)
        else:
            print(f"Сокращённая ссылка: {shortened_link}")