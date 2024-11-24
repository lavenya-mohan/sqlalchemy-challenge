from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt

#################################################
# Database Setup
#################################################

# Directly specify the absolute path to the SQLite database
db_path = r"C:\Users\lavyh\Downloads\Starter_Code (7)\Starter_Code\Resources\hawaii.sqlite"
engine = create_engine(f"sqlite:///{db_path}")

Base = automap_base()
Base.prepare(autoload_with=engine)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latest_date = dt.datetime.strptime(latest_date, "%Y-%m-%d")
    one_year_ago = latest_date - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations_list = [station[0] for station in results]
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latest_date = dt.datetime.strptime(latest_date, "%Y-%m-%d")
    one_year_ago = latest_date - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= one_year_ago).all()
    tobs_data = {date: tobs for date, tobs in results}
    return jsonify(tobs_data)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_summary(start, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if end:
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    else:
        results = session.query(*sel).filter(Measurement.date >= start).all()

    temp_data = {"Min Temp": results[0][0], "Avg Temp": results[0][1], "Max Temp": results[0][2]}
    return jsonify(temp_data)

if __name__ == "__main__":
    app.run(debug=True)
