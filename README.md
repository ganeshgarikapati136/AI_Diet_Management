# AI Diet Management System

A Flask-based web application that provides personalized diet recommendations based on user parameters and preferences.

## Features

- Personalized diet plans based on:
  - Age
  - Weight
  - Height
  - Fitness goals
  - Dietary preferences
  - Health conditions/diseases

## Project Structure

```
AI_Diet_Management/
├── app.py              # Main Flask application
├── diet_model.py       # Diet recommendation logic
├── static/            # Static files (images)
│   ├── Brown rice with lean meat.avif
│   ├── Dark chocolate, nuts.avif
│   └── Grilled fish, leafy greens.avif
└── templates/         # HTML templates
    ├── error.html    # Error page template
    ├── index.html    # Home page template
    └── result.html   # Results page template
```

## Prerequisites

- Python 3.x
- Flask
- Internet connection (required for application to run)

## Dependencies

- Flask: Web framework
- Requests: For internet connectivity check

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install flask requests
```

## Running the Application

1. Open a terminal in the project directory
2. Run the following command:
```bash
python app.py
```
3. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Fill in the required information on the home page:
   - Name
   - Age
   - Weight
   - Height
   - Fitness goal
   - Dietary preferences (optional)
   - Health conditions (optional)

2. Submit the form to receive your personalized diet plan

## Notes

- The application requires an active internet connection to run
- The server runs in debug mode by default
- The application is accessible on port 5000