from flask import Flask

app = Flask(__name__)

links = """<br>
<a href="/">index</a><br>
<a href="/admin">index_admin</a><br>
<a href="/garage">index_garage</a><br>
<a href="/garage_edit">garage_edit</a><br>
<a href="/garage_search">garage_search</a><br>
<a href="/garage_spurlunking">garage_spurlunking</a><br> """

#### Main Index ####
@app.route("/")
def index():
	return "#### Main Index ####" + links


#### Admin Index ####
@app.route("/admin")
def index_admin():
	return "#### Admin Index ####" + links


#### Main Garage ####
@app.route("/garage")
def index_garage():
	return "#### Main Garage ####" + links


#### Garage Edit ####
@app.route("/garage_edit")
def garage_edit():
	return "#### Garage Edit ####" + links


#### Garage Search ####
@app.route("/garage_search")
def garage_search():
	return "#### Garage Search ####" + links


#### Garage spurlunking ####
@app.route("/garage_spurlunking")
def garage_spurlunking():
	return "#### Garage spurlunking ####" + links