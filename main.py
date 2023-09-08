from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def render_home():
   return render_template('home.html')

@app.route('/steps')
def render_steps():
    return render_template('steps.html')

@app.route('/obstaclesfaced')
def render_ftoc():
    return render_template('obstaclesfaced.html')

@app.route('/aboutus')
def render_mtokm():
   return render_template('aboutus.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0')