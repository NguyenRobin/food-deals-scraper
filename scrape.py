
from features.willys import scrape_willys_week_deals
from features.ica import scrape_ica_week_deals
import datetime


def last_scraped():
    filename = "/Users/robinnguyen/Desktop/web-scraper-inflation-python/last_run.txt"
    with open(filename, "a") as file:
        current_time = datetime.datetime.now()
        file.write(f"Senaste skrapade data: {current_time}\n")


def main():
    scrape_willys_week_deals()
    scrape_ica_week_deals()


# Entry point for the program to start
if __name__ == "__main__":
    main()
    last_scraped()
