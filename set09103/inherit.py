from flask import Flask, render_template
app = Flask(__name__)

@app.route('/inheritance/')
def inherits():
  return render_template('base.html')

@app.route('/inheritance/one/')
def template_one():
  return render_template('template1.html')

@app.route('/inheritance/two/')
def template_two():
  return render_template('template2.html')

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)
