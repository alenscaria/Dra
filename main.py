import math
from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
  QTc_result = False
  if request.method == 'POST':
    form = request.form
    heart_rate = request.form['hr']
    qt_int = request.form['qt']
    print(heart_rate+"    "+qt_int)
    f = request.files['file']
    f.save(secure_filename(f.filename))
  return render_template('index.html')
  
 

if __name__ == "__main__":
  app.run(debug=True)