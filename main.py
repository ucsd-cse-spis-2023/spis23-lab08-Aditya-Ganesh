from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def render_home():
   return render_template('home.html')

@app.route('/ctof')
def render_ctof():
    return render_template('ctof.html')

@app.route("/ctof_result")
def render_ctof_result():
   try:
      ctemp_result = float(request.args["ctemp"])
      ftemp_result = ctof(ctemp_result)
      return render_template("ctof_result.html", ctemp = ctemp_result, ftemp = ftemp_result)
   except ValueError:
      return "Sorry: Something went wrong."

@app.route('/ftoc')
def render_ftoc():
    return render_template('ftoc.html')

@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['ftemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html',
                              ftemp=ftemp_result, 
                              ctemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/mtokm')
def render_mtokm():
   return render_template('mtokm.html')

@app.route('/mtokm_result')
def render_mtokm_result():
   try:
      miles_result = float(request.args["miles_count"])
      kilometers_result = miles_to_km(miles_result)
      return render_template('mtokm_result.html',miles=miles_result, kilometers=kilometers_result)
   except ValueError:
      return "Sorry: something went wrong."
   
@app.route("/addtwo")
def render_addtwo():
   return render_template("addtwo.html")

@app.route("/addtwo_result")
def render_addtwo_result():
   try:
      a = float(request.args["num1"])
      b = float(request.args["num2"])
      return str(a + b)
   except ValueError:
      return "you dumbfuck"

def ftoc(ftemp):
   return (ftemp - 32.0) * (5.0 / 9.0)

def ctof(ctemp):
   return (9.0 / 5.0 ) * ctemp + 32.0

def miles_to_km(miles):
   return int(miles * 1.60934)

def add_numbers(a, b):
   return a + b

@app.route('/ftoc/<ftemp_str>')
def convert_ftoc(ftemp_str):
   ftemp = 0.0
   try:
      ftemp = float(ftemp_str)
      ctemp = ftoc(ftemp)
      return 'In Fahrenheit: ' + ftemp_str + ' In Celsius: ' + str(ctemp)
   except ValueError:
      return 'Sorry. Could not convert ' + ftemp_str + ' to a number'

@app.route('/ctof/<ctemp_str>')
def convert_ctof(ctemp_str):
   ctemp = 0.0
   try:
      ctemp = float(ctemp_str)
      ftemp = ctof(ctemp)
      return 'In Celsius: ' + ctemp_str + ' In Fahrenheit: ' + str(ftemp)
   except ValueError:
      return 'Sorry. Could not convert ' + ctemp_str + ' to a number'
   
@app.route('/mtokm/<miles_str>')
def convert_mtokm(miles_str):
   miles = 0.0
   try:
      miles = float(miles_str)
      km = miles_to_km(miles)
      return 'Miles: ' + miles_str + ' Kilometers: ' + str(km)
   except ValueError:
      return 'Sorry. Could not convert ' + miles_str + ' to a number'
   
@app.route('/add/<num1>/<num2>')
def add_nums(num1, num2):
   try:
      num1, num2 = int(num1), int(num2)
      return 'Sum: ' + str(num1 + num2)
   except ValueError:
      return 'Sorry. Could not add ' + num1 + ' + ' + num2

if __name__ == '__main__':
   app.run(host='0.0.0.0')
