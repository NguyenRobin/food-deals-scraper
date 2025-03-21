
from features.willys import scrape_willys_week_deals
from features.ica import scrape_ica_week_deals
import time


def main():
    scrape_willys_week_deals()
    scrape_ica_week_deals()


# Entry point for the program to start
if __name__ == "__main__":
    main()
