import calendar
from datetime import datetime
from flask import Flask, render_template

from weather import get_data, translate_moon_code, pick_moon_icon, check_moon_visibility


app = Flask(__name__)


@app.route('/')
def home():
    weather = get_data()

    now = datetime.utcnow()
    unix_now = calendar.timegm(now.utctimetuple())

    moon_phase_code = weather['daily'][0]['moon_phase']
    moonrise = weather['daily'][0]['moonrise']
    moonset = weather['daily'][0]['moonset']
    if moonset < moonrise:
        moonset = weather['daily'][1]['moonset']

    sunrise = weather['daily'][1]['sunrise']
    sunset = weather['daily'][0]['sunset']
    if sunset > moonrise:
        moongazing_start = int((unix_now - sunset) / 3600)
    else:
        moongazing_start = int((unix_now - moonrise) / 3600)

    if sunrise < moonset:
        moongazing_end = int((unix_now - sunrise) / 3600)
    else:
        moongazing_end = int((unix_now - moonset) / 3600)

    cloud_cover = []
    for hour in range(moongazing_start, moongazing_end):
        clouds = weather['hourly'][hour]['clouds']
        cloud_cover.append(clouds)

    return render_template(
        "index.html",
        moon=translate_moon_code(moon_phase_code),
        moon_visibility=check_moon_visibility(moonrise, moonset, sunrise, sunset, cloud_cover, moon_phase_code),
        icon=pick_moon_icon(moon_phase_code),
    )


if __name__ == '__main__':
    app.run(debug=True)
