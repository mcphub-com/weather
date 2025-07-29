import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/weatherbit/api/weather'

mcp = FastMCP('weather')

@mcp.tool()
def day_forecast(lat: Annotated[Union[int, float], Field(description='Latitude (Degrees) Default: 35.5')],
                 lon: Annotated[Union[int, float], Field(description='Longitude (degrees) Default: -78.5')],
                 units: Annotated[Literal['imperial', 'metric', None], Field(description='I = Imperial, S = Scientific, M = Metric (Default)')] = None,
                 lang: Annotated[Literal['en', 'ar', 'az', 'be', 'bg', 'bs', 'ca', 'cs', 'de', 'fi', 'fr', 'el', 'es', 'et', 'hr', 'hu', 'id', 'it', 'is', 'kw', 'nb', 'nl', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sr', 'sv', 'tr', 'uk', 'zh', 'zh-tw', None], Field(description='Language for weather condition')] = None) -> dict: 
    '''3 hour interval - 5 day forecast for a given lat/lon'''
    url = 'https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly'
    headers = {'x-rapidapi-host': 'weatherbit-v1-mashape.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lon': lon,
        'units': units,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def current_weather_data_of_alocation(lon: Annotated[Union[int, float], Field(description='Longitude Default: 38.5')],
                                      lat: Annotated[Union[int, float], Field(description='Latitude Default: -78.5')],
                                      units: Annotated[Literal['imperial', 'metric', None], Field(description='I = Imperial, S = Scientific, M = Metric (Default)')] = None,
                                      lang: Annotated[Literal['en', 'ar', 'az', 'be', 'bg', 'bs', 'ca', 'cs', 'de', 'fi', 'fr', 'el', 'es', 'et', 'hr', 'hu', 'id', 'it', 'is', 'kw', 'nb', 'nl', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sr', 'sv', 'tr', 'uk', 'zh', 'zh-tw', None], Field(description='Language')] = None) -> dict: 
    '''Returns the current (most recent) weather observation of a given location'''
    url = 'https://weatherbit-v1-mashape.p.rapidapi.com/current'
    headers = {'x-rapidapi-host': 'weatherbit-v1-mashape.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lon': lon,
        'lat': lat,
        'units': units,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hour_minutely_forecast(lat: Annotated[Union[int, float], Field(description='Default: 35.5')],
                           lon: Annotated[Union[int, float], Field(description='Default: -78.5')],
                           units: Annotated[Literal['metric', 'imperial', None], Field(description='metric (Default), imperial')] = None) -> dict: 
    '''Retrieve a 60 minute "Nowcast" for precipitation, and snowfall'''
    url = 'https://weatherbit-v1-mashape.p.rapidapi.com/forecast/minutely'
    headers = {'x-rapidapi-host': 'weatherbit-v1-mashape.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lon': lon,
        'units': units,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hour_forecast(lat: Annotated[Union[int, float], Field(description='Latitude Default: 38.5')],
                  lon: Annotated[Union[int, float], Field(description='Longitude Default: -78.5')],
                  lang: Annotated[Literal['en', 'ar', 'az', 'be', 'bg', 'bs', 'ca', 'cs', 'de', 'fi', 'fr', 'el', 'es', 'et', 'hr', 'hu', 'id', 'it', 'is', 'kw', 'nb', 'nl', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sr', 'sv', 'tr', 'uk', 'zh', 'zh-tw', None], Field(description='Language for weather description')] = None,
                  hours: Annotated[Union[str, None], Field(description='Limit number of forecast hours')] = None,
                  units: Annotated[Literal['imperial', 'metric', None], Field(description='I = Imperial, S = Scientific, M = Metric (Default)')] = None) -> dict: 
    '''Returns a forecast for up to 120 hours in the future (default 48 hours)'''
    url = 'https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly'
    headers = {'x-rapidapi-host': 'weatherbit-v1-mashape.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lon': lon,
        'lang': lang,
        'hours': hours,
        'units': units,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def severe_weather_alerts(lat: Annotated[Union[int, float], Field(description='Latitude Default: 38.5')],
                          lon: Annotated[Union[int, float], Field(description='Longitude Default: -78.5')]) -> dict: 
    '''Get servere weather alerts from local meteorlogical agencies (US, EU, and Isreal supported )'''
    url = 'https://weatherbit-v1-mashape.p.rapidapi.com/alerts'
    headers = {'x-rapidapi-host': 'weatherbit-v1-mashape.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lon': lon,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
