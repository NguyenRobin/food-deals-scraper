from bs4 import BeautifulSoup
import requests
import json


# willys björkgatan id 2194
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
                    print(f"Name: {product_name}")
                    print(f"Price: {price}")
                    print(f"Manufacturer: {manufacturer}")
                    print(f"Image: {image}")
                    print(f"Compare Price: {compare_price}")
                    print(f"Original Price: {original_price}")
                    print(f"Save Price: {savePrice}")
                    print(f"Start Date Deal: {start_date_deal}")
                    print(f"End Date Deal: {end_date_deal}")
                    print("\n\n")

            current_page_number += 1
        else:
            print("All products have been scraped")
            break


def main():
    scrape_willys_week_deals()


# Entry point for the program to start
if __name__ == "__main__":
    main()
