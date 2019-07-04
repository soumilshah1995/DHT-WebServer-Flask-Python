from flask import render_template, url_for, request
import Adafruit_DHT
pin = 17
sensor = Adafruit_DHT.DHT11


from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    temperature, humidity = sensor_1()
    return render_template("sensor.html",temperature=temperature, humidity=humidity)

def sensor_1():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return temperature, humidity


if __name__ == "__main__":
    app.run(debug=True)
