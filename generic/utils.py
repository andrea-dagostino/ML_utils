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
