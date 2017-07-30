from flask import Flask

app = Flask(__name__)

app.run(host='192.168.56.101' ,port=5000,debug=True)

