def mean_absolute_error(y_true, y_pred):
    """
    This function calculates MAE
    :param y_true: list of real numbers, true values
    :param y_pred: list of real numbers, predicted values
    :returns: mean absolute error
    """
    # initialize error at 0
    error = 0
    # loop over all samples in the true and predicted lists
    for yt, yp in zip(y_true, y_pred):
        # calculate absolute error and add to error
        error += np.abs(yt - yp)
    # return mean abs error
    return error / len(y_true)


def mean_squared_error(y_true, y_pred):
    """
    This function calculates MSE
    :param y_true: list of real numbers, true values
    :param y_pred: list of real numbers, predicted values
    :returns: mean squared error
    """
    # initialize error at 0
    error = 0
    # loop over all samples in the true and predicted lists
    for yt, yp in zip(y_true, y_pred):
        # calculate squared error and add to error
        error += np.abs(yt - yp) ** 2
    # return mean squared error
    return error / len(y_true)


def mean_squared_log_error(y_true, y_pred):
    """
    This function calculates MSLE
    :param y_true: list of real numbers, true values
    :param y_pred: list of real numbers, predicted values
    :returns: mean squared logarithmic error
    """
    # initialize error at 0
    error = 0
    # loop over all samples in the true and predicted lists
    for yt, yp in zip(y_true, y_pred):
        # calculate squared log error and add to error
        error += (np.log(1 + yt) - np.log(1 + yp)) ** 2
    # return squared log error
    return error / len(y_true)


def mean_percentage_error(y_true, y_pred):
    """
    This function calculates MPE.
    It is the same thing as Mean Absolute Percentage Error (MAPE)
    :param y_true: list of real numbers, true values
    :param y_pred: list of real numbers, predicted values
    :returns: mean percentage error
    """
    # initialize error at 0
    error = 0
    # loop over all samples in the true and predicted lists
    for yt, yp in zip(y_true, y_pred):
        # calculate percentage error and add to error
        error += (yt - yp) / yt
    # return mean percentage error
    return error / len(y_true)


def r2(y_true, y_pred):
    """
    This function calculates R2 score
    :param y_true: list of real numbers, true values
    :param y_pred: list of real numbers, predicted values
    :returns: r2 score
    """
    # clculate the mean of true values
    mean_true_value = np.mean(y_true)
    # initialize numerator with 0
    numerator = 0
    # initialize denominator with 0
    denominator = 0
    # loop over all true and predicted values
    for yt, yp in zip(y_true, y_pred):
        # update numerator
        numerator += (yt - yp) ** 2
        # update denominator
        denominator += (yt - mean_true_value) ** 2
    # calculate the ratio
    ratio = numerator / denominator
    # return 1 - ratio
    return 1 - ratio