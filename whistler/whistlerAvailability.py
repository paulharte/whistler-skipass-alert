import datetime
from typing import List

from whistler.scraper import WhistlerScraper, WHISTLER_AVAILABILITY_PAGE


def find_open_dates(dates_to_check: List[datetime.date]) -> List[datetime.date]:
    print("Executing scrape of %s" % WHISTLER_AVAILABILITY_PAGE)
    scraper = WhistlerScraper(headless=True)
    free_dates = []
    for date in dates_to_check:
        month_name = date.strftime("%B")
        if scraper.check_day_is_open(date.day, month_name):
            free_dates.append(date)
    if free_dates:
        print("Found open dates!!! %s" % free_dates)
    else:
        print("No free dates found")
    return free_dates


def formDateFoundMessage(free_dates: List[datetime.date]) -> str:
    if len(free_dates) ==1:
        return "Hey, the following date is free in Whistler: %s" % free_dates[0].strftime("%d-%b")
    else:
        date_part = ','.join(map(lambda x: x.strftime("%d-%b"), free_dates))
        return "Hey, the following dates are free in Whistler: %s" % date_part
