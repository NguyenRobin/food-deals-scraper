import requests
import json
from my_products import my_favorite_products


def fetch_willys_week_deals(page_number):
    url = f"https://www.willys.se/search/campaigns/offline?q=2194&type=PERSONAL_GENERAL&page={page_number}&size=20"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result = data['results']
        return result


def scrape_willys_week_deals():
    print("Scraping Willys")
    with open('data.json') as file:
        data = json.load(file)

    new_store = {
        "name": "Willys",
        "address": "Björkgatan 4, 753 27 Uppsala",
        "id": 2194,
        "products": []
    }

    current_page_number = 0

    while True:
        result = fetch_willys_week_deals(current_page_number)

        if (len(result) > 0):
            for product in result:
                product_title = product['name'].lower()

                if any(item in product_title for item in my_favorite_products):
                    start_date_deal = product['potentialPromotions'][0]['startDate']
                    end_date_deal = product['potentialPromotions'][0]['endDate']
                    savePrice = product['potentialPromotions'][0]['savePrice']
                    price = product['priceNoUnit']
                    manufacturer = product['manufacturer']
                    image = product['image']['url']
                    compare_price = product['potentialPromotions'][0]['comparePrice']
                    original_price = product['priceNoUnit']

                    new_store["products"].append({
                        "title": product_title,
                        "price": price,
                        "manufacturer": manufacturer,
                        "image": image,
                        "compare_price": compare_price,
                        "original_price": original_price,
                        "save_price": savePrice,
                        "start_date_deal": start_date_deal,
                        "end_date_deal": end_date_deal})

            current_page_number += 1
        else:
            print("All products have been scraped")
            break

    if not data['stores']:
        data['stores'].append(new_store)

    else:
        for store in data['stores']:
            if store['name'].lower() == new_store['name'].lower():
                print('WILLYS hittad & uppdaterad')
                store['products'] = new_store['products']
                break
        else:
            print(
                'Finns butiker. Men inte Willys. Så vi lägger till den')
            data['stores'].append(new_store)

    with open("data.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
