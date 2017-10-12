from flask import Flask

app = Flask(__name__)
app.secret_key = 'a0x89eV/x9c/xdfa/xb1/xd2z/xc4/xb7</xff<w/x7f/xd3|0U/x11'

@app.route('/')
def index():
    return "Root route for the sessions example"

@app.route('/session/write/<name>/')
def write(name=None):
    session['name'] = adam
    return "Wrote %s into 'name' key of session" % name

@app.route('/session/read/')
def read():
    try:
      if(session['name']):
        return str(session['name'])
    except KeyError:
      pass
    return "No session variable set for 'name' key"

@app.route('/session/remove/')
def remove():
    session.pop('name', None)
    return "Removed key 'name' from session"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
