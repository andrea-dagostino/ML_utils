import json
import datetime
import os
from pathlib import Path


def log_prediction(response) -> None:
    """This function logs model performance served through an API.

    Args:
        response (dict): the response model of your API.
    """
    today = datetime.datetime.today().strftime("%Y%m%d")
    fname = f"./performance/log_{today}.json"

    a = []
    if not os.path.isfile(fname):
        a.append(response)
        with open(fname, mode="w") as f:
            f.write(json.dumps(a, indent=4))
    else:
        with open(fname) as feedsjson:
            feeds = json.load(feedsjson)

        feeds.append(response)
        with open(fname, mode="w") as f:
            f.write(json.dumps(feeds, indent=4))
