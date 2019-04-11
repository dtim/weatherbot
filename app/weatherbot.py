from flask import Flask
from forecast import ForecastService


fs = ForecastService(user_agent="dtim.weatherbot")
app = Flask(__name__)


@app.route('/')
def index():
    return "Server works!"


@app.route('/weather')
def say_hello():
    weather = fs.weather("St. Petersburg")
    if weather:
        return weather
    else:
        return "{}"
