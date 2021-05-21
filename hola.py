from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("template.html", nombre="Uriel")

@app.route('/intereses')
def intereses():
	return render_template("intereses.html")
	
@app.route('/reflexion')
def reflexion():
	return render_template("reflexion.html")

if __name__ == "__main__":
	app.run(debug=True)