import requests
import json


with open('data.json') as file:
    data = json.load(file)


def fetch_willys_week_deals(page_number):
    url = f"https://www.willys.se/search/campaigns/offline?q=2194&type=PERSONAL_GENERAL&page={page_number}&size=20"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result = data['results']
        return result


def scrape_willys_week_deals():
    my_favorite_products = ['entrecôte', 'lammracks', 'ryggbiff', 'nocco', 'torkpapper',
                            'köttfärs', 'kyckling', 'rostas', 'lax', 'ägg', 'kaffe', 'smör', 'oxfilé', 'tomat', 'keso', 'vindruvor', 'druvor', 'ikaffe', 'kaffefilter', 'turkisk yoghurt', 'cola', 'bryggkaffe', 'jordgubbar', 'blåbär']

    store = {
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
                product_name = product['name'].lower()

                if any(item in product_name for item in my_favorite_products):
                    start_date_deal = product['potentialPromotions'][0]['startDate']
                    end_date_deal = product['potentialPromotions'][0]['endDate']
                    savePrice = product['potentialPromotions'][0]['savePrice']
                    price = product['priceNoUnit']
                    manufacturer = product['manufacturer']
                    image = product['image']['url']
                    compare_price = product['potentialPromotions'][0]['comparePrice']
                    original_price = product['priceNoUnit']

                    store["products"].append({
                        "name": product_name,
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
        print("Listan är tom! så vi lägger till Willys")
        data['stores'].append(store)
    else:
        for current in data['stores']:
            if current['name'].lower() == store['name'].lower():
                print(current['name'], 'hittad och ändrar')
                current['products'] = store['products']
                break
            else:
                print('No store found')
    print(data)
    with open("data.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
