# News API Web App

This is a simple web application built with Flask that retrieves and displays news headlines using the NewsAPI. The application has two routes: the home route and the BBC route. The home route displays top headlines from Al Jazeera English, while the BBC route displays top headlines from BBC News.

## Setup
1. Install Flask and the NewsAPI library.
2. Sign up on the [NewsAPI website](https://newsapi.org/) to obtain an API key.
3. Replace `"your-key"` with your NewsAPI key in the script.

## Usage
1. Run the script using a Python interpreter: `python app.py`.
2. Access the home route by visiting `http://localhost:5000/` in your web browser. This page will display the top headlines from Al Jazeera English.
3. Access the BBC route by visiting `http://localhost:5000/bbc` in your web browser. This page will display the top headlines from BBC News.

## Requirements
- Python 3.x
- Flask
- NewsAPI

## Files
- `app.py`: The main script that defines the Flask application and the routes.
- `base.html`: The HTML template for the home route that displays the headlines.
- `bbc.html`: The HTML template for the BBC route that displays the headlines.

Feel free to customize the HTML templates (`base.html` and `bbc.html`) to suit your needs, such as adding CSS styles or additional content.

Note: Make sure to keep your API key secure and avoid sharing it publicly.

Enjoy exploring the news headlines with this News API web app!
