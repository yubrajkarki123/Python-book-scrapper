import requests
from bs4 import BeautifulSoup
import json

url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to load page")
        return []
    
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.find_all("article", class_="product_pod")
    
    all_books = []
    for book in books:
        title = book.h3.a['title']
        price_string = book.find('p', class_='price_color').text.strip()
        currency = price_string[0]
        price = float(price_string[1:])
        
        all_books.append({
            "title": title,
            "currency": currency,
            "price": price
        })
    
    return all_books

# Call function
books = scrape_books(url)

# Save as JSON
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=4, ensure_ascii=False)

print("Books saved to books.json")
