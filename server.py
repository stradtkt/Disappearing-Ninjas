from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html')

@app.route('/ninja')
def ninjas():
  return render_template('ninjas.html')

@app.route('/ninja/orange')
def michelangelo():
  return render_template('michelangelo.html')

@app.route('/ninja/red')
def raphael():
  return render_template('raphael.html')

@app.route('/ninja/purple')
def donatello():
  return render_template("donatello.html")

@app.route('/ninja/blue')
def leonardo():
  return render_template('leonardo.html')

@app.errorhandler(404)
def myview(e):
  return render_template('404.html')

app.run(debug=True)