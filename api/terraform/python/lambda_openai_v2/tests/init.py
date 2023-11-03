import json


def get_event(filespec):
    with open(filespec, "r") as f:
        event = json.load(f)
        return event
