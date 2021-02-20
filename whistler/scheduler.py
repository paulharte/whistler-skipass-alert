import datetime
import time
from typing import List

from whistler.tweeter.secrets import extract_secrets
from whistler.tweeter.twitterAlerts import TwitterAlerter
from whistler.whistlerAvailability import find_open_dates, formDateFoundMessage

DEFAULT_INTERVAL_MINUTES = 10


def run_schedule(twitter_handle: str, dates: List[datetime.date], minute_interval=DEFAULT_INTERVAL_MINUTES):
    twitter_alerter = TwitterAlerter(extract_secrets())
    while True:
        free_dates = find_open_dates(dates)
        if free_dates:
            msg = formDateFoundMessage(dates)
            print("sending notification! %s" % msg)
            twitter_alerter.send_dm(twitter_handle, msg)
            print("shutting down successfully ")
            return
        time.sleep(minute_interval * 60)

