"""Provide common functions for testing."""
import json


def get_event(filespec):
    """Reads a JSON file and returns the event"""
    with open(filespec, "r") as f:
        event = json.load(f)
        return event
