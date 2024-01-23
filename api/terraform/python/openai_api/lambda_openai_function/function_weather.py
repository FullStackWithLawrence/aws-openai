# -*- coding: utf-8 -*-
"""OpenAI API example function: https://platform.openai.com/docs/guides/function-calling"""
import json


def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    if "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    if "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    return json.dumps({"location": location, "temperature": "unknown"})


def weather_tool_factory():
    """Return a list of tools that can be called by the OpenAI API"""
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    return tools
