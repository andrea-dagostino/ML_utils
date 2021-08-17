import pandas as pd

def create_date_features(dataframe):
    """This function extracts time-related features from a 'date' column

    Args:
        dataframe (pd.DataFrame): the pandas dataframe object with the 'date' column
    Returns:
        dataframe [pd.DataFrame]: a pandas dataframe with the additional engineered columns.
    """
    try:
        dataframe["date"] = dataframe.date.apply(lambda x: pd.Timestamp(x))
    except:
        pass
    dataframe["month"] = dataframe.date.dt.month
    dataframe["day_of_month"] = dataframe.date.dt.day
    dataframe["day_of_year"] = dataframe.date.dt.dayofyear
    dataframe["week_of_year"] = dataframe.date.dt.isocalendar().week
    dataframe["day_of_week"] = dataframe.date.dt.dayofweek + 1
    dataframe["year"] = dataframe.date.dt.year
    dataframe["is_wknd"] = dataframe.date.dt.weekday // 4
    dataframe["is_month_start"] = dataframe.date.dt.is_month_start.astype(int)
    dataframe["is_month_end"] = dataframe.date.dt.is_month_end.astype(int)
    dataframe["quarter"] = dataframe.date.dt.quarter

    return dataframe


def ts_to_date(ts:int) -> str:
    """Utility function that converts a timestamp to a readable date.

    Args:
        ts (int): UNIX timestamp.

    Returns:
        str: the string-formatted date
    """
    date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    return date


def date_to_ts(date:str) -> int:
    """Utility function that converts a string-formatted date to a UNIX timestamp.

    Args:
        date (str): the string-formatted date

    Returns:
        int: UNIX timestamp.
    """

    ts = int(time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))
    return ts