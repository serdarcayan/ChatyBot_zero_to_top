def build_population_response(city: str, population: str | None) -> str:
    if population:
        return f"Wikipedia’ya göre {city} nüfusu yaklaşık {population} civarındadır."
    else:
        return f"{city} için nüfus bilgisi bulunamadı."
