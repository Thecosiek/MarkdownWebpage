import os
import requests
from bs4 import BeautifulSoup

# URL strony do zescrapowania
URL = "http://grandioso.pl/sekcje/"

# Pobranie zawartości strony
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Znalezienie wszystkich linków do sekcji
sections = soup.find_all("a", class_="wp-block-button__link")

# Znalezienie pierwszego obrazka
image_tag = soup.find("img")
image_url = image_tag["src"] if image_tag else None

# Ścieżki do zapisu
output_dir = "C:/Users/monik/OneDrive/Pulpit/Programowanie/WWW"
output_md = os.path.join(output_dir, "sekcje.md")
output_img = os.path.join(output_dir, "obrazek.jpg")

# Tworzenie pliku Markdown
try:
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("# Lista sekcji Grandioso\n\n")
        
        if image_url:
            f.write(f"![Obrazek](./obrazek.jpg)\n\n")  # Dodajemy obrazek do markdowna
        
        for section in sections:
            title = section.text.strip()  # Nazwa sekcji
            link = section["href"]  # URL do sekcji
            
            f.write(f"## [{title}]({link})\n\n")
            f.write("---\n\n")
    
    print(f"Plik sekcje.md został zapisany w: {output_md}")

except Exception as e:
    print(f"Błąd zapisu pliku: {e}")

# Pobieranie i zapisywanie obrazka
if image_url:
    try:
        img_data = requests.get(image_url).content
        with open(output_img, "wb") as img_file:
            img_file.write(img_data)
        print(f"Obrazek został zapisany jako: {output_img}")
    except Exception as e:
        print(f"Błąd pobierania obrazka: {e}")
