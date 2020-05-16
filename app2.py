import numpy as np

import sqlalchemy
from datetime import datetime
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect
from flask import Flask, jsonify
	

# engine = create_engine("sqlite:///Resources/hawaii.sqlite")
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

passenger = Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station
	
		# session = Session(engine)	
		# inspector = inspect(engine)
		# inspector.get_table_names()

# print(type(Measurement.date))
#print(Measurement.date)
#data_setup = datetime(Measurement.date)
	
# Flask Setup
app = Flask(__name__)
	
# Query for the dates and temperature observations from the last year.
@app.route("/")
def home():
	return(
	"/api/v1.0/precipitation<br/>"
	"/api/v1.0/stations<br/>"
	"/api/v1.0/tobs<br/>"
	)




# @app.route("/api/v1.0/precipitation")
# def precipitation():
# 	session = Session(engine)
# 	result_date = session.query(Measurement.date).all()
# 	result_prcp = session.query(Measurement.prcp).all()
# 	date = list(np.ravel(result_date))
# 	prcp = list(np.ravel(result_prcp))


#  Convert the query results to a Dictionary.
	first_dict = []
	for temps in result_date and temps in result_prcp:
		temps_dict = {}
		temps_dict["date"] = temps[0]
		temps_dict["tobs"] = temps[1]
		first_dict.append(temps_dict)
		first_result = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>="2016-08-23").all()
	#  Return the JSON representation of your dictionary.
	return jsonify(first_dict)
	

# * `/api/v1.0/stations`
#   * Return a JSON list of stations from the dataset.	
@app.route("/api/v1.0/stations")
def stations():
	session = Session(engine)
	second_result = session.query(Station.station, Station.name).all()
	session.close()

	second_dict = list(np.ravel(second_result))
	# Convert the query results to a Dictionary.
	second_dict = []
	for station in second_result:
		station_dict = {}
		station_dict["station"] = station[0]
		station_dict["name"] = station[1]
		second_dict.append(station_dict)

	#  Return the JSON representation of your dictionary.
	return jsonify(second_dict)
	

# * `/api/v1.0/tobs`
# * Return a JSON list of Temperature Observations (tobs) for the previous year.
	
@app.route("/api/v1.0/tobs")
def tobs():
	session = Session(engine)

	third_result = session.query(Measurement.date, Measurement.tobs).\
		filter(Measurement.date>="2016-08-23").\
		filter(Measurement.date<="2017-08-23").\
		filter(Measurement.station=='USC00519281').all()
	session.close()

	#  Convert the query results to a Dic
	# Convert the query results to a Dictionary.
	third_dict = []
	for temps in third_result:
		temp_dict = {}
		temp_dict["date"] = temps[0]
		temp_dict["tobs"] = temps[1]
		third_dict.append(temp_dict)
		

	# #  Return the JSON representation of your dictionary.
	return jsonify(third_dict)
		

	
# * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
	

@app.route("/api/v1.0/<date>")
def start(date):
	session = Session(engine)

	forth_result = session.query((Measurement.date, func.avg(Measurement.tobs), func.max(Measurement.tobs), func.min(Measurement.tobs)).\
	filter(Measurement.date)>=date).all()
	session.close()

#  Convert the query results to a Dictionary.
	fourth_dict = []
	for s in forth_result:
		start_dict = {}
		start_dict["Date"] = s.Date
		start_dict["Avg"] = s.func.avg(Measurement.tobs)
		start_dict["Min"] = s.func.min(Measurement.tobs)
		start_dict["Max"] = s.func.max(Measurement.tobs)
		fourth_dict.append(start_dict)

#  Return the JSON representation of your dictionary.
	return jsonify(fourth_dict)
		
		
# return jsonify(temp_dates)
if __name__ == '__main__':
	app.run(debug=True)


	

