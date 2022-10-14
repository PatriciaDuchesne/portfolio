import requests
import os


def get_data():
    parameters = {
        "lat": 45.5017,
        "lon": -73.5673,
        "appid": os.environ['OWM_API_KEY'],
        "exclude": "current,minutely,alerts",
        "units": "metric"
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    return response.json()


def translate_moon_code(code):
    if code == 0 or code == 1:
        return "Today is a New Moon."
    elif code < 0.25:
        return "The Moon today is a waxing crescent."
    elif code == 0.25:
        return "Today is the First Quarter Moon."
    elif code < 0.5:
        return "The Moon is waxing gibbous."
    elif code == 0.5:
        return "Today is the Full Moon."
    elif code < 0.75:
        return "The Moon is waning gibbous."
    elif code == 0.75:
        return "Today is the Last Quarter Moon."
    elif code < 1:
        return "The Moon today is a waning crescent."

    raise ValueError("invalid moon code")


def pick_moon_icon(code):
    if code == 0 or code == 1:
        return "icon01.png"
    elif code < 0.1:
        return "icon02.png"
    elif code < 0.2:
        return "icon03.png"
    elif code == 0.25:
        return "icon04.png"
    elif code < 0.3:
        return "icon05.png"
    elif code < 0.4:
        return "icon06.png"
    elif code < 0.5:
        return "icon07.png"
    elif code < 0.6:
        return "icon08.png"
    elif code < 0.7:
        return "icon09.png"
    elif code == 0.75:
        return "icon10.png"
    elif code < 0.8:
        return "icon11.png"
    elif code < 0.9:
        return "icon12.png"
    elif code < 1:
        return "icon12.png"


def _check_cloud_cover(clouds):
    if not clouds:
        return "The sky will be clear and the Moon will be visible tonight."
    else:
        cloud_average = sum(clouds) / len(clouds)
        if cloud_average < 25:
            return "The sky will be clear and the Moon will be visible tonight."
        elif cloud_average < 50:
            return "The sky will be cloudy, but the Moon might be visible tonight."
        else:
            return "The sky will be too cloudy, the Moon will not be visible tonight."


def check_moon_visibility(moonrise, moonset, sunrise, sunset, cloud_cover, moon_phase_code):
    if moon_phase_code == 0 or moon_phase_code == 1:
        return "The Moon will not be visible."
    if sunset < moonrise < sunrise:
        return _check_cloud_cover(cloud_cover)
    elif moonrise < sunset < moonset:
        return _check_cloud_cover(cloud_cover)
    else:
        return "The Moon will not be visible tonight."
