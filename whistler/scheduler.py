import datetime
import time
from typing import List

from whistler.scraper import WhistlerScraper

INTERVAL_MINUTES = 5


def find_open_dates(dates_to_check: List[datetime.date]) -> List[datetime.date]:
    print("Executing scrape")
    scraper = WhistlerScraper(headless=True)
    free_dates = []
    for date in dates_to_check:
        month_name = date.strftime("%B")
        if scraper.check_day_is_open(date.day, month_name):
            free_dates.append(date)
    if free_dates:
        print("Found open dates!!! %s" % free_dates)
    return free_dates


def run():
    dates = [datetime.date(2021, 4, 19), datetime.date(2021, 4, 20)]

    while True:
        free_dates = find_open_dates(dates)
        if free_dates:
            #TODO: add twitter message or other notification here
            print("sending notification!")
            break
        time.sleep(INTERVAL_MINUTES * 60)


if __name__ == "__main__":
    run()
