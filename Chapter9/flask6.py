from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
	thing = request.values.get('thing')
	height = request.values.get('height')
	color = request.values.get('color')
	return render_template('home.html',thing=thing, height=height, color=color)

app.run(host='192.168.56.101' ,port=5000,debug=True)

