import requests
from urllib.parse import quote
from config.settings import WIKIPEDIA_BASE_URL, USER_AGENT


def get_wikipedia_page(title: str) -> str | None:
    """
    Verilen başlığa göre Wikipedia sayfasını indirir.
    """
    title = title.strip()
    encoded_title = quote(title.replace(" ", "_"))

    url = WIKIPEDIA_BASE_URL + encoded_title

    headers = {
        "User-Agent": USER_AGENT
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.text
        else:
            print(f"Sayfa bulunamadı ({response.status_code}): {url}")
            return None

    except requests.RequestException as e:
        print(f"İstek hatası: {e}")
        return None
