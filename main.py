from search.wikipedia_search import get_wikipedia_page
from parser.info_extractor import extract_plain_text, extract_population
from responder.response_builder import build_population_response
from utils.text_utils import extract_city_from_question


def main():
    question = input("Sorunuzu yazın: ")

    city = extract_city_from_question(question)

    html = get_wikipedia_page(city)
    if not html:
        print("İlgili sayfa bulunamadı.")
        return

    text = extract_plain_text(html)

    population = extract_population(text)

    response = build_population_response(city, population)

    print(response)


if __name__ == "__main__":
    main()
