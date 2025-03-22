# Weather App

## Overview
The Weather App provides real-time weather updates based on the user's entered location. The app dynamically changes the background to reflect day or night based on the user's time zone. It is built using Django and Python and fetches weather data through a REST API.

## Features
- **Location-Based Weather Reports**: Users can enter a city name to view real-time weather details.
- **Dynamic Background**: The app changes the background based on whether it is day or night in the selected location.
- **Weather Details**: Displays temperature, feels-like temperature, condition, humidity, and location.
- **Responsive UI**: Ensures a user-friendly experience across different devices.

## Technologies Used
- **Django**: Backend framework for handling requests and rendering templates.
- **Python**: Core programming language for backend logic.
- **REST API**: Fetches live weather data.
- **JSON**: Handles data from the API response.
- **HTML, CSS, JavaScript**: For the frontend interface.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Rajat652000/wetherapp.git
   cd weatherapp
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Obtain an API key from a weather data provider (e.g., OpenWeatherMap).
   - Create a `.env` file and add:
     ```
     WEATHER_API_KEY=your_api_key_here
     ```
5. Run database migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Open a web browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
- Enter a city name in the search bar.
- View real-time weather details.
- Observe background changes depending on the time of day.

## Future Improvements
- Add support for more weather details like wind speed and UV index.
- Implement geolocation-based weather updates.
- Improve UI/UX with animations and additional themes.

## Contributing
Feel free to contribute by submitting issues or pull requests.

---
Developed by Rajat Kumar verma
