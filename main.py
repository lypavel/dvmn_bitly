import requests as rq
import os
import argparse
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
    bitlink = f"{parsed_link.netloc}{parsed_link.path}"
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


def create_parser() -> None:
    parser = argparse.ArgumentParser(
        description="\
            Программа сокращает вашу длинную ссылку с помощью Bitly \
            и выводит статистику кликов по уже сокращённой ссылке. \
        "
    )
    parser.add_argument("user_url", help="Ваша ссылка")

    return parser


def main() -> None:
    load_dotenv()

    headers = {
        "Authorization": f"Bearer {os.environ["BITLY_TOKEN"]}"
    }

    parser = create_parser()
    args = parser.parse_args()
    user_url = args.user_url

    if is_bitlink(user_url, headers):
        clicks_count = count_clicks(user_url, headers)
        print(f"Количество переходов по ссылке битли: {clicks_count}")
    else:
        shortened_link = shorten_link(user_url, headers)
        print(shortened_link)


if __name__ == "__main__":
    try:
        main()
    except rq.exceptions.HTTPError as http_error:
        exit(f"Невозможно получить информацию от сервера:\n{http_error}")
