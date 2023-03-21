from flask import Flask, render_template
from flask import send_file
app = Flask(__name__)

@app.route('/')
def home1():
   return render_template('index.html')

@app.route('/taxonomy.json')
def downloadFile ():
    path = "taxonomy.json"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
   app.run()
