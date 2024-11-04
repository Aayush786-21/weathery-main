from flask import Flask, render_template, jsonify, request
from barsha import get_weather

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homie.html')

@app.route('/get_weather')
def get_weather_route():
    city = request.args.get('city', 'Kathmandu')  # Default is Kathmandu
    weather, temperature = get_weather(city)
    if weather and temperature is not None:  # Ensure both values are not None
        return jsonify({'success': True, 'weather': weather, 'temperature': temperature})
    else:
        return jsonify({'success': False, 'message': 'Could not retrieve weather data'}), 404

if __name__ == '__main__':
    app.run(debug=True)
