from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
   return 'Hello World!'

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
