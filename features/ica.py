from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json
from my_products import my_favorite_products


def scrape_ica_week_deals():
    print("Scraping ICA")
    with open('data.json') as file:
        data = json.load(file)

    new_store = {
        "name": "ICA Supermarket Torgkassen",
        "address": "Vaksalagatan 30, 753 31 Uppsala",
        "products": []
    }

    session = HTMLSession()

    r = session.get(
        'https://www.ica.se/erbjudanden/ica-supermarket-torgkassen-1003821/')

    r.html.render(sleep=1)

    html_element_array = r.html.find(
        '.offer-card')

    for product in html_element_array:
        soup = BeautifulSoup(product.html, "html.parser")

        title = soup.find(
            "div", class_="offer-card__details-container").find("p", class_="offer-card__title").text.lower()

        if any(item in title for item in my_favorite_products):

            price = soup.find('div', class_='offer-card__image-container').find('div').find(
                'span', class_='sr-only').text

            image = soup.find(
                'div', class_='offer-card__image-container').find('img')['src']
            manufacturer = soup.find(
                'div', class_='offer-card__details-container').find('p', class_='offer-card__text').find('span').text.split('.')[0]
            addition_information = soup.find(
                'div', class_='offer-card__details-container').find('p', class_='offer-card__text').find('span').text.split('.')[1]

            original_price = soup.find(
                'div', class_='offer-card__details-container').find('p', class_='offer-card__text').find_all('span')[1].text.split(' ')[0]

            new_store['products'].append({
                "title": title,
                "price": price,
                "manufacturer": manufacturer,
                "image": image,
                "original_price": original_price,
                "addition_information": addition_information
            })

    if not data['stores']:
        print("Inga butiker. Lägger till ICA Supermarket Torgkassen")
        data['stores'].append(new_store)
    else:
        for store in data['stores']:
            if store['name'].lower() == new_store['name'].lower():
                print('ICA hittad & uppdaterad')
                store['products'] = new_store['products']
                break
        else:
            # Detta block körs om loopen inte avbryts med 'break'
            print(
                'Finns butiker. Men inte ICA. Så vi lägger till den')
            data['stores'].append(new_store)
    with open("data.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
