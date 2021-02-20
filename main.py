import datetime

from whistler.scheduler import run_schedule


def run():
    dates = [datetime.date(2021, 4, 18), datetime.date(2021, 4, 19), datetime.date(2021, 4, 20)]
    twitter_handle_to_notify = '@paulmharte'
    minute_interval_to_poll = 10
    run_schedule(twitter_handle_to_notify, dates, minute_interval_to_poll)


if __name__ == "__main__":
    run()