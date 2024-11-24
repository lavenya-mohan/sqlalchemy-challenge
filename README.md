# sqlalchemy-challenge
-------
# Climate Data Analysis

This project involves analyzing and exploring Hawaii climate data using Python, SQLAlchemy, Pandas, and Matplotlib. The project is divided into two parts:
1. Climate analysis and data exploration using `climate_starter.ipynb`.
2. Development of a RESTful API using `app.py`.

---

## Overview

### Part 1: Climate Data Analysis
This analysis includes:

#### Precipitation Analysis:
- Analyzing the last 12 months of precipitation data.
- Visualizing precipitation trends using Matplotlib.
- Summarizing precipitation data with Pandas.

#### Station Analysis:
- Determining the total number of weather stations.
- Identifying the most active weather station.
- Analyzing temperature data for the most active station.

### Part 2: Climate Data API
A Flask-powered RESTful API (`app.py`) is developed to expose the climate data through the following endpoints:
- **Home Route (`/`)**: Lists all available API routes.
- **Precipitation Data (`/api/v1.0/precipitation`)**: Returns the last 12 months of precipitation data.
- **Weather Stations (`/api/v1.0/stations`)**: Returns a JSON list of all weather stations.
- **Temperature Observations (`/api/v1.0/tobs`)**: Returns temperature observations (TOBS) for the last 12 months.
- **Temperature Summary by Date (`/api/v1.0/<start>`)**: Returns min, avg, and max temperatures from the start date to the end of the dataset.
- **Temperature Summary by Date Range (`/api/v1.0/<start>/<end>`)**: Returns min, avg, and max temperatures for a given date range.

---
## Steps

### Part 1: Climate Data Analysis
1. **Setup**:
   - Connect to the `hawaii.sqlite` database using SQLAlchemy.
   - Reflect the database tables and link them to Python using SQLAlchemy ORM.

2. **Precipitation Analysis**:
   - Retrieve and analyze the last 12 months of precipitation data.
   - Visualize the data and compute summary statistics.

3. **Station Analysis**:
   - Query station details and identify the most active station.
   - Analyze temperature observations (TOBS) for the most active station.
   - Visualize TOBS data as a histogram.

4. **Cleanup**:
   - Close the SQLAlchemy session.

### Part 2: Climate Data API
1. Develop a Flask application (`app.py`) to expose climate data through various endpoints.
2. Use SQLAlchemy ORM queries to fetch data dynamically.
3. Test the API locally using the provided routes.

---



