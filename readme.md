# Weather App

A simple Flask-based web application that fetches and displays live weather information for cities around the world. The weather data is fetched from the OpenWeatherMap API.

## Features

- Enter a city name to get current weather information.
- Displays weather description and temperature.
- Simple and clean user interface.


## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Aayush786-21/weathery.git
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. **Install the required packages**:

    ```bash
    pip install flask requests
    ```

4. **Get an API key** from [OpenWeatherMap](https://openweathermap.org/) and replace the placeholder in `barsha.py`:

    ```python
    api_key = 'your_api_key'  # Get yours api key from openweathermap
    ```

## Usage

1. **Run the Flask application**:

    ```bash
    python turuturu.py
    ```

2. **Open a web browser and go to**:

    ```
    http://localhost:5000/
    ```

3. **Enter a city name** in the input box and click "Get Weather" to see the weather information.

## Files

- **`turuturu.py`**: Main Flask application file that defines routes and renders the HTML template.
- **`barsha.py`**: Module to fetch weather data from the OpenWeatherMap API.
- **`templates/homie.html`**: HTML template for displaying the weather information.

## Example

When you open the application, you will see a page with an input box to enter a city name. Upon entering the city name and clicking "Get Weather", the application will fetch and display the current weather and temperature for the specified city.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

