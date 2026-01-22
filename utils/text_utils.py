def extract_city_from_question(question: str) -> str:
    """
    Sorudan şehir adını basitçe çıkarmaya çalışır.
    """
    question = question.lower().strip()

    # çok basit yaklaşım: ilk kelime
    city = question.split()[0]

    # özel ekleri temizle
    city = city.replace("un", "").replace("ün", "").replace("ın", "").replace("in", "")

    return city.capitalize()
