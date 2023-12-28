import calendar
import datetime


def get_start_and_end_of_current_month():
    today = datetime.datetime.today()

    starting_date = today.replace(
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )
    end_date = today.replace(
        day=calendar.monthrange(today.year, today.month)[1],
        hour=23,
        minute=59,
        second=59,
        microsecond=999999,
    )
    return starting_date, end_date
