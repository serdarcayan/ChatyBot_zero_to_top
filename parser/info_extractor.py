from bs4 import BeautifulSoup
import re


def extract_plain_text(html: str) -> str:
    """
    Wikipedia HTML içeriğinden sadece anlamlı metni çıkarır.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Gereksiz etiketleri temizle
    for tag in soup(["script", "style", "sup", "table"]):
        tag.decompose()

    paragraphs = soup.find_all("p")

    texts = []
    for p in paragraphs:
        text = p.get_text(strip=True)
        if len(text) > 50:  # çok kısa ve anlamsız paragrafları at
            texts.append(text)

    return "\n".join(texts)


def extract_population(text: str) -> str | None:
    """
    Metin içinden nüfus bilgisini bulmaya çalışır.
    """
    patterns = [
        r"nüfusu\s*(\d{1,3}(?:[.\s]\d{3})+)",
        r"nüfus\s*(\d{1,3}(?:[.\s]\d{3})+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)

    return None
