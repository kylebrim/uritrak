import math
from flask import Flask, redirect, url_for, render_template

patients = [['324009725', 'Kyle', 'Brim', '21 Aug 1997', 'Male',
			 '177 lbs', 'McKinney, TX'],
			['123001234', 'Yazan', 'Abuashour', '1 Jan 1990',
			 'Non-binary', '365 lbs', 'Compton, CA'],
			['456009898', 'Lauren', 'Yamthe', '31 Oct 1969',
			 'Female', '112 lbs', 'Houston, TX'],
			['909009009', 'Haani', 'Tai', '25 Dec 2000',
			 'Gender Fluid', '225 lbs', 'New York, NY'],
			['123009999', 'Hannah', 'McKinley', '31 Oct 2020',
			 'Mustang', '7 lbs', 'Tampa, FL'],
			['888008888', 'Michael', 'Guillen', '29 Feb 1999',
			 'Often', '800 lbs', 'City, ST']]
length = len(patients)

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", id=patients, l=length)

@app.route("/<id>")
def id_page(id):
	return render_template("patient.html", id=patients[int(id)], sp=id)

if __name__ == "__main__":
	app.run(debug=True)

