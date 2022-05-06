import math
from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import mysql.connector
from mysql.connector import Error

eidn=1
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
  QTc_result = False
  if request.method == 'POST':
    form = request.form
    heart_rate = request.form['hr']
    qt_int = request.form['qt']
    print(heart_rate+"    "+qt_int)

  #new
    
    mydb = mysql.connector.connect(host='localhost',
                                         database='druglist',
                                         user='root',
                                         password='1234')
      
    mycursor = mydb.cursor()
    ff="Doe"
    gg="Highway 22"

    sql = "INSERT INTO entry(eid,loc,text) VALUES (%s,%s,%s)"
    val=(eidn,heart_rate,qt_int)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")




    f = request.files['file']
    f.save(secure_filename(f.filename))
  return render_template('index.html')
  
 

if __name__ == "__main__":
  app.run(debug=True)
