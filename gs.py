from googlesearch import search
import time
import os

# Ścieżka do zapisania pliku
base_path = r"C:/Users/monik/OneDrive/Pulpit/Programowanie/WWW"
output_file = os.path.join(base_path, "sekcje_dodatkowe.md")

# Lista sekcji/instrumentów do wyszukania
sekcje = [
    "Flet, obój", "Klarnet", "Saksofon", "Trąbka", "Eufonium, fagot", "Waltornia",
    "Tuba, kontrabas, bas", "Puzon", "Perkusja, kotły, mallets", "Color Guard",
    "Mażoretki, werble, tamburmajorki", "Props"
]

with open(output_file, "w", encoding="utf-8") as file:
    file.write("# Dodatkowe informacje o sekcjach Grandioso\n\n")

    for sekcja in sekcje:
        query = f"{sekcja} instrument muzyczny"
        file.write(f"## {sekcja}\n\n")
        
        print(f"🔎 Wyszukiwanie: {query}...")

        try:
            results = search(query, num_results=3, lang="pl")
            for link in results:
                file.write(f"- [Więcej informacji]({link})\n")
            file.write("\n---\n\n")
        except Exception as e:
            print(f"Błąd podczas wyszukiwania dla {sekcja}: {e}")

        time.sleep(1)  # Krótka przerwa, aby uniknąć blokady Google

print(f"✅ Plik został zapisany w: {output_file}")
